def shortword(text):
    if len(text) < 100:
        return text
    else:
        return text[:80] + '...'

def price_parser(price):
    p = str(price)
    if len(p) > 9:
        return p[:-9] + ',' + p[-9:-6] + ',' + p[-6:-3] + ',' + p[-3:]
    elif len(p) > 6:
        return p[:-6] + ',' + p[-6:-3] + ',' + p[-3:]
    elif len(p) > 3:
        return p[:-3] + ',' + p[-3:]
    else:
        return p

def barhide(value):
    tmp = value.replace('|', ', ')
    try:
        if tmp[-2:-1] == ',':
            tmp = tmp[:-2]
    except:
        pass
    return tmp