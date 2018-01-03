
class test(int):
    def __new__(cls, value,unit):
        obj=super().__new__(cls,value)
        obj.unit=unit
        print("__new__")
        return obj
    def __init__(self,value,unit):
        print("__init__")

a=test(1,"cm")
print(a,a.unit)