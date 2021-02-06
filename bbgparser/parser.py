import pyparsing

from .constants import EQ, EOL, START_OF_FILE, END_OF_FILE


comment = pyparsing.Regex(r"#.*").suppress()


def _headers():
    key = pyparsing.Word(pyparsing.alphanums + '_')
    val = pyparsing.Word(pyparsing.printables)
    headerLine = pyparsing.Group(key('key') + EQ + val('val') + EOL)
    return pyparsing.OneOrMore(
        headerLine
        | comment
    ).setParseAction(lambda x: {item['key']: item['val'] for item in x})


def _fieldsBlock():
    START_OF_FIELDS = pyparsing.Keyword('START-OF-FIELDS', identChars='-')
    END_OF_FIELDS = pyparsing.Keyword('END-OF-FIELDS', identChars='-')
    fields = pyparsing.Word(pyparsing.alphanums + '_')
    return pyparsing.nestedExpr(
        START_OF_FIELDS,
        END_OF_FIELDS,
        content=pyparsing.OneOrMore(fields, stopOn=END_OF_FIELDS)
    ).setParseAction(lambda x: [item for sublist in x for item in sublist])


def _parseDataBlock(x):
    return [i.split('|') for i in x]


def _dataBlock():
    TIMESTARTED = pyparsing.Word('TIMESTARTED').suppress()
    date_time_started = pyparsing.Group(
        TIMESTARTED
        + EQ
        + pyparsing.Regex(r".*")
    )

    TIMEFINISHED = pyparsing.Word('TIMEFINISHED').suppress()
    date_time_finished = pyparsing.Group(
        TIMEFINISHED
        + EQ
        + pyparsing.Regex(r".*")
    )

    START_OF_DATA = pyparsing.Keyword('START-OF-DATA', identChars='-')
    END_OF_DATA = pyparsing.Keyword('END-OF-DATA', identChars='-')

    dataLine = pyparsing.Regex('.*')
    dataLines = pyparsing.OneOrMore(dataLine, stopOn=END_OF_DATA)

    return pyparsing.nestedExpr(
        date_time_started,
        date_time_finished,
        content=pyparsing.nestedExpr(
            START_OF_DATA,
            END_OF_DATA,
            content=dataLines.setParseAction(_parseDataBlock)
        )
    ).setParseAction(lambda x: [z for y in x for z in y])


def _parse_content(content: str) -> pyparsing.ParseResults:
    headers = _headers()
    fieldsBlock = _fieldsBlock()
    dataBlock = _dataBlock()

    file = pyparsing.nestedExpr(
        START_OF_FILE,
        END_OF_FILE,
        content=(
            pyparsing.OneOrMore(
                headers.setResultsName('headers')
                ^ fieldsBlock.setResultsName('fields')
                ^ dataBlock.setResultsName('data')
                ^ comment
            )
        )
    )

    return file.parseString(content)


def parse(content: str):
    return _parse_content(content)[0].items()
