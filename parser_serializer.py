# this package can be used to parse and serialize objects of type str, int, dict
# it is done like the JSON manner


def parse_string(txt):
    """Parses plain text to 'str' object"""
    return str(txt[1:-1])


def serialize_string(s):
    """Serializes 'str' object to plain text"""
    return f'"{s}"'


def parse_number(txt):
    """Parses plain text to 'int' object"""
    return int(txt)


def serialize_number(n):
    """Serializes 'int' object to plain text"""
    return str(n)


def parse_dict(txt):
    """Parses plain text to 'dict' object"""
    pairs = txt[txt.index('{')+1:txt.rindex('}')].split(',') # need to inplement a correct split by comma
    d = {}
    for p in pairs:
        if p:
            splt = p.split(':')
            key = splt[0].strip()
            value = splt[1].strip()
            if value[0] == '{':
                value = parse_dict(value)
            d[key] = value
    return d


def serialize_dict(d):
    """Serializes 'dict' object to plain text"""
    txt = '{'
    for k in d:
        txt += f'"{k}":'
        if isinstance(d[k], dict):
            txt += serialize_dict(d[k])
        if isinstance(d[k], str):
            txt += serialize_string(d[k])
        if isinstance(d[k], int):
            txt += serialize_number(d[k])
        txt += ','
    txt += '}'
    return txt


if __name__ == '__main__':
    """some print tests"""
    s = 'abc'
    n = 357
    d = {"k1":{"k11": 'abc'},"k2": 1,"k3":{"k31":{"k311": 'abc'}}}

    plain_txt = serialize_string(s)
    print(f'serialized string: {plain_txt}')
    print(f'parsed string: {parse_string(plain_txt)}')

    plain_txt = serialize_number(n)
    print(f'serialized number: {plain_txt}')
    print(f'parsed string: {parse_number(plain_txt)}')

    plain_txt = serialize_dict(d)
    print(f'serialized dictionary: {plain_txt}')
    # print(parse_dict(plain_txt))
    

