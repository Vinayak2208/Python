def Palindrome(num):
    copy = num
    pow = len(str(num)) -1
    rev = 0
    while num > 0:
        rev += (num%10)*10**pow
        num //= 10
        pow -= 1
    if copy == rev:
        return "Palindrome"
    return "Not Palindrome"
print(Palindrome(1441))