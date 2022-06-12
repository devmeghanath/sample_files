f=open('conversation.txt','r')
s=open('ouput.txt','a')


for read in f:
    splited=read.split(' ')
    s.write(read+'has'+'--->'+str(len(splited)))

f.close()
s.close()

