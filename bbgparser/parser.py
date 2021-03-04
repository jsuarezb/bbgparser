"""BBG Parser.

This module provides the functionality to parse .bbg Bloomberg files.

Example:
    results = bbgparser.parse(content)
"""

import pyparsing

from .constants import (EQ, EOL, COMMENT, START_OF_FILE,
                        END_OF_FILE, START_OF_DATA, END_OF_DATA,
                        START_OF_FIELDS, END_OF_FIELDS,
                        TIMESTARTED, TIMEFINISHED)


def _headers():
    key = pyparsing.Word(pyparsing.alphanums + '_')
    val = pyparsing.Word(pyparsing.printables)
    header_line = pyparsing\
        .Group(key('key') + EQ + val('value') + EOL)

    return pyparsing\
        .OneOrMore(
            header_line
            ^ COMMENT
        ).setParseAction(lambda items: {item[0]: item[1] for item in items})


def _fields_block():
    field = pyparsing.Word(pyparsing.alphanums + '_')
    fields = pyparsing.OneOrMore(field, stopOn=END_OF_FIELDS)

    return pyparsing\
        .nestedExpr(
            START_OF_FIELDS,
            END_OF_FIELDS,
            content=fields
        ).setParseAction(list)


def _parse_data_block(row):
    return [i.split('|') for i in row]


def _data_block():
    date_time_started = pyparsing.Group(
        TIMESTARTED
        + EQ
        + pyparsing.Regex(r".*")
    )

    date_time_finished = pyparsing.Group(
        TIMEFINISHED
        + EQ
        + pyparsing.Regex(r".*")
    )

    data_line = pyparsing.Regex('.*')
    data_lines = pyparsing.OneOrMore(data_line, stopOn=END_OF_DATA)

    return pyparsing.nestedExpr(
        date_time_started,
        date_time_finished,
        content=pyparsing.nestedExpr(
            START_OF_DATA,
            END_OF_DATA,
            content=data_lines.setParseAction(_parse_data_block)
        )
    ).setParseAction(lambda x: [z for y in x for z in y])


def _parse_content(content: str) -> pyparsing.ParseResults:
    headers = _headers()
    fields_block = _fields_block()
    data_block = _data_block()

    file = pyparsing.nestedExpr(
        START_OF_FILE,
        END_OF_FILE,
        content=(
            COMMENT
            ^ headers.setResultsName('headers')
            ^ fields_block.setResultsName('fields')
            ^ data_block.setResultsName('data')
        )
    )

    return file.parseString(content)


def parse(content: str):
    """Parse .bbg content

    Args:
        content (str): The .bbg content

    Returns:
        dict: The parsed content
    """
    result = _parse_content(content)
    result = dict(result[0].items())

    return result
