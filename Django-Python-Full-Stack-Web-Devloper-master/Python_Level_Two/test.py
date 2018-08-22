class Emp():
    def __init__(self):
        s2 = 'hello'
        print('EMP class constructor')

    def fun1(self):
        self.s1 = 's1 var'
        # s2 = 's2 var in fun1'
        # return self.s1
        print('fun1 ')

    def fun2(self):
        # print(self.s1)
        s2 = 's2 var in fun2'
        print( self.s1)
        return s2


class Sal(Emp):


    def __init__(self):
        Emp.__init__(self)
        print('Sal class constructor called')

    def fun3(self):
        print('sal fun2 called')
a = Emp()
a.fun1()
a.fun2()

# e = Sal()
# e.fun2()
# e.fun1()
