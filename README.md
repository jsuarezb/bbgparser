# bbgparser

`bbgparser` aims to parse the .bbg file that Bloomberg provides you as a
response for their Data Requests and Historical Requests while using the
Bloomberg's
[Hypermedia API](https://www.bloomberg.com/professional/expertise/developer/)
(HAPI).

The content of this file looks something similar to this:

```
START-OF-FILE
# Required headers
HEADER_KEY_1=header_value_1
HEADER_KEY_2=header_value_2

START-OF-FIELDS
FIELD1
FIELD2
END-OF-FIELDS

TIMESTARTED=Mon Jan 01 00:00:00 GMT 2020
START-OF-DATA
ABC|10|1| | | | |
DEF|20|2| | | | |
END-OF-DATA
TIMEFINISHED=Mon Jan 01 00:00:00 GMT 2020
END-OF-FILE
```

## Installation

```
pip install bbgparser
```

## Getting started

```python
from bbgparser.parser import parse

result = parse(content)

for k, v in results:
    print(k, v)
```

When parsing the example above, you'll get the following output:

```
headers {'HEADER_KEY_1': 'header_value_1', 'HEADER_KEY_2': 'header_value_2'}
fields ['FIELD1', 'FIELD2']
data [['ABC', '10', '1', ' ', ' ', ' ', ' ', ''], ['DEF', '20', '2', ' ', ' ', ' ', ' ', '']]
```
