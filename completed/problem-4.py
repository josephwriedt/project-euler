# Largest Palindrome Number

def is_palindrome(x: int):
    s = str(x)
    return s == s[::-1]

def has_three_digit_multiples(num: int):
    for i in reversed(range(100, 1000)):
        if num%i == 0 and (num/i)//100 != 0 and (num/i)//100 < 10:
            return i, int(num / i)
    
    return ()

# max number of digits three digit numbers can make = 6

for i in reversed(range(1,1000000)):
    if is_palindrome(i):
        if (t := has_three_digit_multiples(i)):
            print("Palindrome:", i)
            print("Multiples:", t)
            break


# I really like this solution
# Format of 6-digit palindrome: abccba where a,b,c < 10
# 100000a  + 10000b + 1000c + 100c + 10b + a
# Combing Factors: 100001a + 10010b + 1100c
# Factoring: 11(9091a + 910b + 100c)

