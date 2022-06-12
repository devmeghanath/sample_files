f=open('data.txt','r')

s=f.read()
import json

book=json.loads(s)
print(book)

for items in book:
    print(book[items])