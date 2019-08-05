def power(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return false
                n = n // 2
    return true
if(power(int(input()))):
    print('yes')
else:
    print('no')
