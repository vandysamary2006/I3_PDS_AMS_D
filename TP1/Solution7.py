def digit_sum(n):
    """Add up the digits of a whole number."""
    n=abs(n)

    total = 0
    while n > 0:
        total += n % 10   #last digit
        n//=10            #deop the last digit
    return total

def reverse_digits(n):
    """Reverse the digits of a whole number 1234->4321"""
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10    
    return result

def is_palindrome(n):
    return n == reverse_digits(n)
    

print(digit_sum(1991))
print(reverse_digits(2001))
print(is_palindrome(1991))