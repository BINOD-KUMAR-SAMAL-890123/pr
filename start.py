num=int(input("num:"))
if num%2==0:
    print("even")
else:
    print('odd')
    
    
def palindrome(word):
    return word == word[::-1]
print(palindrome("bibi"))
