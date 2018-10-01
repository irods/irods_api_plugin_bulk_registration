import jsonschema
import json

with open('example.json', 'rt') as f:
    example = json.load(f)
with open('packaging/irods_api_plugin_bulk_registration.json', 'rt') as f:
    schema = json.load(f)
jsonschema.validate(example, schema)
