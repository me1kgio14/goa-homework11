def is_triangle(a, b, c):
    if a+b>c and a+c>b and c+b>a:
        return True
    else:
        return False