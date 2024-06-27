def remove_url_anchor(url):
    s=""
    for char in url:
        if char=="#":
            break
        s+=char
    return s     