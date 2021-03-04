def shortword(value):
    return value[:75]

def barhide(value):
    tmp = value.replace('|', ', ')
    try:
        if tmp[-2:-1] == ',':
            tmp = tmp[:-2]
    except:
        pass
    return tmp