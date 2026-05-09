'''static function to use any class Function without any object or with object'''
'''And onething we can not use self with these static mathod '''

class Math:
    def __init__(self):
        self.num1=0
        self.num2=0
    @staticmethod
    def add(n,i):
        return (n+i)

print(Math.add(3,4))
a=Math()
print(a.add(6,8))
a.show()