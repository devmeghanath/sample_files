
vowels=input('enter the words==>')

def counter(vowels):
    new=sorted(vowels)
    count=0
    for i in new:
        if i=='a' or i=='e' or i=='i' or i== 'o' or i=='u':
            count+=1
    print(count)

counter(vowels)