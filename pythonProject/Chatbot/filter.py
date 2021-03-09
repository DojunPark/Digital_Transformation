def shortword(text):
    if len(text) < 50:
        return text
    else:
        return text[:50] + '...'