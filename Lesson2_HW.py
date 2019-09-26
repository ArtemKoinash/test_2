#task 1.1
q = "asdfghjk"
str.isnumeric(q)
#task 1.2
w = "How are you filling...., darling?"
str.count(w, ' ')
#task 1.3
str.count(w, '.')
#task 1.4
e = "Homework"
str.center(e, 100)
#task 1.5
r = "hey dude, whats up"
str.title(r)

#task 2.1
math.hypot(179, 971)
#task 2.2
x = 65
print(x // 10)
#task 2.3 (я нашел в интернете несколько решений в одну сторку "sum(int(digit) for digit in str(number))" и "sum(map(int, str(number)))". Но я не до конца понимаю как они функционаруют, поэтому написал ниже показан вариант до которого я дошел сам. Он не такой изящный конечно, но вроде работает 
speed = input('Enter number with 3 digits: ')
speed = str(speed)
a = speed[0]
b = speed[1]
c = speed[2]
a1 = int(a)
b1 = int(b)
c1 = int(c)
summa = a1 + b1 +c1
print(summa)
#task 2.4 
n = 11
n1 = n + 2 - n%2
print(n1)
#task 2.5
a = 61984.54987
print(a%1)
#task 2.6
x = float(input('enter float: '))
f = str(x % 1)
print(f[2])
# task 3 
year = input("Enter a year:  ")
year = int(year)
if year % 4 != 0 or (year % 400 != 0 and year % 100 == 0):
    print("no")
else:
    print("yes")
#task 4 
a = float(input("Enter side a:  "))
b = float(input("Enter side b:  "))
c = float(input("Enter side c:  "))
if a < b + c and b < a + c and c < a + c:
    print('yes')
else:
    print('no')
#task 5 с этим заданием к сожалению мне доволе сильно помог интернет, сам додуматься не смог
a = float(input("Enter number a:  "))
b = float(input("Enter number b:  "))
c = float(input('Enter number c:  '))
if a >= b and a >= c and b >= c:
    print(c, b, a)
elif a <= b and a >= c and b >= c:
    print(c, a, b)
elif a <= b and a <= c and b <= c:
    print(a, b, c)
elif a >= b and a >= c and b <= c:
    print(b, c, a)
elif a >= b and a <= c and b <= c:
    print(b, a, c)
else:
    print(a, c, b)
#task 6
a = int(input("Enter number one:  "))
b = int(input("Enter number two:  "))
c = int(input("Enter number three:  "))
if a == b == c:
    print('3')
elif a == b or b == c or a == c:
    print('2')
else:
    print('0')