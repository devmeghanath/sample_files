book={}


book['bob']={
    'name':'bob',
    'address':'101,street',
    'phn':855554655666
}
book['sam']={
    'name':'sam',
    'address':'121,street',
    'phn':54654545454
}
print(book)
import json

data=json.dumps(book)

with open('data.txt',"w") as f:
    f.write(data)






