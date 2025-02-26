def Prime(n):
    if n > 1:
        for i in range(2,n//2+1):
            if n%i == 0 :
                return "Not prime"
        else:
            return "Prime"
    return "Not Prime"

print(Prime(7))