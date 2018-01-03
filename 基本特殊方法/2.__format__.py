'''
格式化输出

'''
class test:
    def __init__(self):
        self.name="format"
        self.value="hello"
    def display(self):
        print("tell {0} {1}!".format(self.name,self.value))
    def display1(self):
        print("{name} tell me {value} !".format(name=self.name,value=self.value))
    def __format__(self, format_spec):
        if format_spec=="":
            return str(self)
        rs=format_spec.replace("%n",self.name).replace("%v",self.value)
        rs=rs.replace("%%","%")
        return rs

t=test()
t.display()
t.display1()
print("I will tell {0:%n %v} !".format(t))
width=10
st={"No.1":1,"No.2":2}
for hand,count in st.items():
    print("{hand}{count:{width}d}".format(hand=hand,count=count,width=width))
