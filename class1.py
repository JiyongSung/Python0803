# class1.py
#클래스를 정의
class Person:
    def__init__(self):
    self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1=Person()
p1.print()