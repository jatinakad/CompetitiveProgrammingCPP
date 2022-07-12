#by reversing a string
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
print(isPalindrome(s))

#2 iterative
def Palin(st):

    for i in range(0,int(len(st)/2)):
        if st[i] != s[len(st)-i-1]:
            return False
    return True
                   
st = "malayalam"
ans = Palin(st)
if(ans):
    print("yes")
else:
    print("no")

#visualisation of reversing
x = "malayalac"
 
w = ""
for i in x:
    w = i + w
 
print(w)
print(i)

#Tree recursion
def fun(n):
 
    if (n > 0):
     
        print(n, end=" ")
         
        # Calling once
        fun(n - 1)
         
        # Calling twice
        fun(n - 1)
     
 
print(fun(3))
# Driver code
# print(fun(3))

#Using flag variable

# Python program to check
# if a string is palindrome
# or not
st = 'malayalam'
j = -1
flag = 0
# print(st[j])
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("NO")
else:
    print("Yes")