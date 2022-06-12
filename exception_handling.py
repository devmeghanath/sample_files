

a=input('enter the first number --->')
b=input('enter the second number --->')

try:
    c=int(a)/int(b)
except ZeroDivisionError as e:
    print('error occured',e)
    c=None
except TypeError as v:
    print(type(v).__name__)
    c=None
except Exception as b:
    print('error occured',b)
    c=None

print(c)
