class person:
    #def say_hello(self):
       # print("hello")
        #print(self)
    
    
    #def greet(self,name='person'):
        #return "hello {}".format(name)
    
    #def __init__(self):
        #print("hello")
    
    #def __init__(self,name):
        #print("hello, I'm {}".format(name))
        
    def __init__(self,full_name):
        self.name=full_name    
    def say_hello(self):
        print("hello, I'm {}".format(self.name))