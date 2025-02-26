def Disarium(num):
    copy = num
    pow = len(str(num))
    res = 0
    while num > 0:
        res += (num%10)**pow
        num //= 10
        pow -= 1
    if copy == res:
        return "Disarium Number"
    return "Not Disarium Number"
print(Disarium(135))