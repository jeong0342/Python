class Athlete:
    def __init__(self, value='Jane'):
        self.thing = value
    def getAthlete(self):
        return self.thing


a = Athlete()
a.getAthlete()
print(a.getAthlete())
b=Athlete('Holy')
Athlete.__init__(a,'Holy')
b.getAthlete()
print(b.getAthlete())


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def innerPrint(self, infor):
        print(infor, self.x, self.y)

pt1 = Point()
print('Point01 Class',pt1.x, ',',pt1.y)
pt2 = Point(3,5)
print('Point02 Class',pt2.x,',',pt2.y)
pt2.innerPrint('Point02 InnerPrint:')