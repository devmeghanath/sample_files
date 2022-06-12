
class Human():
    def __init__(self,n,o):
        
        self.name=n
        self.occupation=o



    def do_Work(self):
        if self.occupation == "actor":
            print(self.name,'is a actor')

        elif self.occupation == "tenis":
            print(self.name,"is a player")

    def speak(self):
        print(self.name,'says hey how are u')



define_name=input('enter your name-->')
define_occupation=input('enter your occupation-->')


define_name=Human(define_name,define_occupation)
define_name.do_Work()
define_name.speak()