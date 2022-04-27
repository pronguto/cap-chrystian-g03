from app.models.exceptions.ingredient_exception import KeysError

def validate_keys(body_request: dict, expected_keys: set):
    recived_keys= set(body_request.keys())
    recived_values= set(body_request.values())
    valid_keys= []
    extra_keys= recived_keys - expected_keys

    for expected_key in expected_keys:
        for recived_key in recived_keys:
            if recived_key == expected_key:
                valid_keys.append(recived_key)

    if len(valid_keys) < len(expected_keys):
        raise KeysError(expected=expected_keys, recived= recived_keys)

    for key in extra_keys:
        body_request.pop(key, None)

    return body_request