#python class study (간단한 계산기)
class FourCal: #클래스
    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class MoreFourCal(FourCal): #상속
    def pow(self):
        result = self.first ** self.second
        return result
class SafeFourCal(FourCal): #상속
    def div(self): #오버라이딩
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
x,y=map(int,input().split())
a = MoreFourCal(x,y)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())