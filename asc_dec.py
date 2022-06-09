
def parameters(numbers,strings):
    if strings=='asc':
        print(sorted(numbers))
        
    elif strings=='desc':
        print(sorted(numbers,reverse=True))
    else:
        print('none')



parameters([4,6,7,5,9],"f")



