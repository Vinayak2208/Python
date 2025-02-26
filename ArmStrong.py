def Armstrong(n):
    copy = n
    pow = len(str(n))
    res = 0
    while n>0 :
        res += (n%10)**pow
        print(res)
        n //= 10
    if copy == res:
        return "Armstrong"
    return "Not Armstrong"

print(Armstrong(153))
    