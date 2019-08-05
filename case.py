def convert(str):
    ln = len(str)
    for i in range(ln):
        if str[i] >= 'a' and str[i] <= 'z':
            str[i] = chr(odd(str[i]) - 32)
        elif str[i] >= 'A' and str[i] <= 'Z':
            str[i] = chr(odd(str[i])= +32)      
if__name__ == "__main__":
   str = input()
   str = list(str)
   convert(str)
   str= ''.join(str)
   print(str)
