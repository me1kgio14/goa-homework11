def solution(s):
    final=""
    for letter in s:
        if letter!=letter.upper():
            final+=letter
        elif letter==letter.upper():
            final+=" "+letter
    return final