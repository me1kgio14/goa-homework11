def reverse_words(text):
    text=text.split(" ")
    reverse=""
    for i in text:
        reverse+=" "+i[::-1]
    return reverse[1:]