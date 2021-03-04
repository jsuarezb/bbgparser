from behave import given, when, then
from bbgparser import parse


@given('the file {file}')
def step_given_the_file(context, file):
    with open(file, 'r') as file:
        context.content = file.read()


@when('parsing the file')
def step_when_parsing_the_file(context):
    context.results = parse(context.content)


@then('we get the headers')
def step_then_we_get_all_the_headers(context):
    expected_headers = {row['key']: row['value'] for row in context.table}
    assert context.results['headers'] == expected_headers


@then('we get the fields')
def step_then_we_get_all_the_fields(context):
    expected_fields = set([row['field'] for row in context.table])

    assert set(context.results['fields']) == expected_fields


@then('we get the records')
def step_then_we_get_all_the_records(context):
    expected_records = [tuple(row) for row in context.table]
    parsed_records = [tuple(row) for row in context.results['data']]

    assert set(parsed_records) == set(expected_records)
