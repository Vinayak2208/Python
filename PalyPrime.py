def PalyPrime(num):
    for val in range(2,num//2+1):
        if num % val == 0:
            return "Not PalyPrime"
    
    else:
        copy = num
        pow = len(str(num)) - 1
        rev = 0
        while num > 0:
            rev += (num%10)*(10**pow)
            num //= 10
            pow -= 1
        if copy == rev:
            return "PalyPrime"
        return "Not PalyPrime"
    
print(PalyPrime(131))