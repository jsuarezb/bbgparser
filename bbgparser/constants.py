import pyparsing

START_OF_FILE = pyparsing.Keyword('START-OF-FILE', identChars='-')
END_OF_FILE = pyparsing.Keyword('END-OF-FILE', identChars='-')
EQ = pyparsing.Literal('=').suppress()
EOL = pyparsing.LineEnd().suppress()
EMPTY_LINE = pyparsing.Literal('\n')
