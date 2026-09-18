class akkcclass:
    x=10

    # A constructor does not need to be called explicitly. It is called automatically when an object is created from the class.
    def __init__ (self):
        print("Welcome to DevOps Junoon")

    # when ever we create a function inside a class, it called a method.
    def testmethod (self):
        self.p=self.x*self.x
        print(self.p)

    def add(self, a, b) :
        print (a+b)

object = akkcclass()
object.testmethod()
object.add(20,30)
