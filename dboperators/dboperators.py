def verification_func(func):
    def inner(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        return returned_value
    return inner


@verification_func
def serializer_save(model_serializer, input_json):
    serializer_var = model_serializer(data=input_json)
    if serializer_var.is_valid(raise_exception=True):
        serializer_var.save()
    return serializer_var


@verification_func
def serializer_save_multiple(model_serializer, input_json):
    serializer_var = model_serializer(data=input_json, many=True)
    if serializer_var.is_valid(raise_exception=True):
        serializer_var.save()
    return serializer_var


@verification_func
def serializer_partial_save(model_serializer, input_json):
    serializer_var = model_serializer(data=input_json, partial=True)
    if serializer_var.is_valid(raise_exception=True):
        serializer_var.save()
    return serializer_var




def serializer_update(model_serializer, queryobj, input_json):
    serializer_var = model_serializer(queryobj, data=input_json)
    if serializer_var.is_valid(raise_exception=True):
        serializer_var.save()
    return serializer_var


def update_record(model, index, **kwargs):
    """This function is used to update records within a table identified by its Primary Key """
    modelobj = model.objects.filter(pk=index)
    modelobj.update(**kwargs)
    qs = model.objects.filter(pk=index).all()
    return qs.values()[0]