"""Pyparsing constant elements"""

import pyparsing

EQ = pyparsing.Literal('=').suppress()
EOL = pyparsing.LineEnd().suppress()
EMPTY_LINE = pyparsing.Literal('\n')
COMMENT = pyparsing.Regex(r"#.*").suppress()

START_OF_FILE = pyparsing.Keyword('START-OF-FILE', identChars='-')
END_OF_FILE = pyparsing.Keyword('END-OF-FILE', identChars='-')

START_OF_DATA = pyparsing.Keyword('START-OF-DATA', identChars='-')
END_OF_DATA = pyparsing.Keyword('END-OF-DATA', identChars='-')

START_OF_FIELDS = pyparsing.Keyword('START-OF-FIELDS', identChars='-')
END_OF_FIELDS = pyparsing.Keyword('END-OF-FIELDS', identChars='-')

TIMESTARTED = pyparsing.Word('TIMESTARTED').suppress()
TIMEFINISHED = pyparsing.Word('TIMEFINISHED').suppress()
