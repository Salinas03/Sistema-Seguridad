import json

def is_valid_json(variable):
    try:
        json_object = json.loads(variable)
        return True
    except (json.JSONDecodeError, TypeError):
        return False
