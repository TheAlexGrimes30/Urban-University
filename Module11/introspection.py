def introspection_info(obj):
    obj_type = type(obj).__name__

    all_attributes = dir(obj)

    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]

    obj_module = obj.__class__.__module__

    additional_properties = {}

    if isinstance(obj, (int, float, complex)):
        additional_properties['real'] = getattr(obj, 'real', None)
        additional_properties['imag'] = getattr(obj, 'imag', None)
    elif isinstance(obj, (list, tuple, set, frozenset, dict)):
        additional_properties['length'] = len(obj)
    elif isinstance(obj, str):
        additional_properties['length'] = len(obj)
        additional_properties['isalpha'] = obj.isalpha()
        additional_properties['isdigit'] = obj.isdigit()

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'additional_properties': additional_properties
    }

    return info


number_info = introspection_info(42)
print(number_info)

list_info = introspection_info([1, 2, 3])
print(list_info)
