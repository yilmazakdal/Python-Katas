def find_the_needle(haystack, needle):
    new_list = []

    for key, value in haystack.items():
        if type(value) == str and needle in value:
            new_list.append(key)
        elif type(value) == dict:
            # Recursively call find_the_needle for nested dictionaries
            nested_keys = find_the_needle(value, needle)
            if nested_keys:
                nested_keys_with_prefix = [f"{key}.{nested_key}" for nested_key in nested_keys]
                new_list.extend(nested_keys_with_prefix)
    return new_list