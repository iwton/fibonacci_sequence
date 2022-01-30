n = int(input('Enter the number: '))
a, b, c = 0, 1, 0
temp = '1'
s = ' '
if n == 1:
    print(n)
elif n > 1:
    for i in range(n - 1):
        c = a + b
        temp += s + str(c)
        a = b
        b = c
    
print(temp)
