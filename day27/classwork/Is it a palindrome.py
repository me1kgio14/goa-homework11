def is_palindrome(s):
    s=s.lower()
    length=len(s)
    if length==1:
        return True
    
    elif s==s[::-1]:
        return True
    else:
        return False
