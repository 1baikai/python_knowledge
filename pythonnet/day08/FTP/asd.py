class Human:
    def __init__(self,n,a):#类属性
        self.name = n
        self.age = a
        self.money = 0
        self.skill = []

    def teach(self,other,skill):
        print(self.name,"教",other.name,"学",skill)
        other.skill.append(skill)

    def work(self,m):
        print(self.name,'上班赚了',m,'元钱')
        other.money -= m
        self.money += m

    def borrow(self,other,m):
        if other.money>m:
            print(self.name,'向',other.name,'借',m,'元')
            other.money -=m
            self.money += m
        else:
            print(other.name,'没有钱借给',self.name)

    def show_info(self):
        print(self.age,self.name,self.money,','.join(self.skill))




##