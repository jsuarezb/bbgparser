Feature: Parse BBG file

Scenario: Extracting headers
  Given the file fixtures/wellformed_file.bbg
   When parsing the file
   Then we get the headers
     | key | value |
     |RUNDATE|20210301|
     |FIRMNAME|dl792847|
     |PROGRAMNAME|getdata|
     |REPLYFILENAME|sxiePxLastDataReq.bbg|
     |PROGRAMFLAG|daily|
     |TIME|0500|
     |USERNUMBER|15429575|
     |SN|811339|
     |WS|0|
     |BASICTAX|YES|
     |CAPSTRUCT|YES|
     |CLOSINGVALUES|YES|
     |COLTAG|YES|
     |CORPSTRUCT|YES|
     |CREDITRISK|YES|
     |DEFAULTRISK|YES|
     |DERIVED|YES|
     |ESTIMATES|YES|
     |FUNDAMENTALS|YES|
     |HISTORICAL|YES|
     |IFRS9SPPI|YES|
     |INVSTPROT|YES|
     |MIFIR|YES|
     |PRICING|YES|
     |REGCBE|YES|
     |REGCFID|YES|
     |REGCOMP|YES|
     |REGECL|YES|
     |REGFVHL|YES|
     |REGHQLA|YES|
     |REGLQA|YES|
     |REGPRICEUNCERTAINTY|YES|
     |REGSOLVENCY|PACKAGED|
     |REGSSFA|YES|
     |REGTRANSPARENCY|YES|
     |SECMASTER|YES|
     |USWHLDTAX|YES|
     |VOL_SURFACE|YES|

Scenario: Extracting fields
  Given the file fixtures/wellformed_file.bbg
    When parsing the file
    Then we get the fields
      | field   |
      | PX_LAST |

Scenario: Extracting records
  Given the file fixtures/wellformed_file.bbg
    When parsing the file
    Then we get the records
      | ISIN         | error_code | records | var1       | empty_column |
      | EU0009658442 | 0          | 1       | 271.740000 |              |
