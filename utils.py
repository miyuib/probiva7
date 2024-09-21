def format_result(row, schema, **kwargs):
    result = ""
    for key, value in kwargs.items():
        if key in schema:
            result += value.format(**row) + " "
    return result.strip()
