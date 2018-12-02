def field_validator(keys, data_):
    """
    Validates the submitted data are POSTed with the required fields
    :param keys:
    :param data_:
    :return:
    """
    data = {}
    for v in keys:
        if v not in data_:
            data[v] = ["This field may not be null."]
    if len(data) != 0:
        return {"success": False, "data": data}
    elif len(data) == 0:
        return {"success": True, "data": data}
