def emirp(num):
    rev = 0
    copy = num
    pow = 10**(len(str(num))-1)
    while num > 0:
        rev += (num % 10)*pow
        pow //= 10
        num //= 10
    if copy != rev:
        if rev > 1 and copy > 1:
            for val in range(2,copy//2+1):
                if copy % val == 0:
                    return "Not Emirp"
            else:
                for val in range(2,rev//2 + 1):
                    if rev % val == 0:
                        return "Not Emirp"
                return "Emirp Number"
        return "Not Emirp Number"
    return "Not EMirp Number"
print(emirp(17))
