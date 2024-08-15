import json


def json_to_sql(json_file, sql_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(sql_file, 'w') as f:
        for entry in data:
            model = entry['model']
            fields = entry['fields']

            table_name = model.split('.')[-1]  # Extract table name from model
            if not fields:
                continue  # Skip if no fields are present

            columns = ', '.join(fields.keys())
            values = ', '.join(
                "'{}'".format(str(value).replace("'", "''"))
                for value in fields.values()
            )
            sql = "INSERT INTO {} ({}) VALUES ({});\n".format(
                table_name, columns, values)
            f.write(sql)


# Usage
json_to_sql('old_data.json', 'old_data.sql')
