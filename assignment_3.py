
# Q1
def diff(n):
    return abs(n-17)*2 if n>17 else 17-n
print(diff(25))

# Q2
def range(n): return 100<=n<=1000 or n==2000
print(range(999))

# Q3
def reverse(s): return s[::-1]
print(reverse("robot"))

# Q4
def case_count(s):
    d={"UPPER":0,"LOWER":0}
    for c in s:
        if c.isupper(): d["UPPER"]+=1
        elif c.islower(): d["LOWER"]+=1
    return d
print(case_count("Tutor"))

# Q5
def unique_list(l): return list(set(l))
print(unique_list([1,2,2,3]))

# Q6
def even_list(L): return [x for x in L if x%2==0]
print(even_list([1,2,3,4,5]))

# Q7
def outer():
    def inner(): print("Inner called")
    inner()
outer()

# Q8
def student(name,age,course): print(name,age,course)
student("Sudiksha",19,"Python")

# Q9
def move_robot(pos,dirn):
    x,y=pos
    if dirn=="up": return (x,y+1)
    if dirn=="down": return (x,y-1)
    if dirn=="left": return (x-1,y)
    if dirn=="right": return (x+1,y)
print(move_robot((0,0),"up"))

# Q10
def classify_temp(t):
    if t<=15: return "Cold"
    elif t<=30: return "Moderate"
    else: return "Hot"
print(classify_temp(20))

# Q11
def goal_reached(path):
    x=y=0
    for step in path:
        if step=="up": y+=1
        if step=="down": y-=1
        if step=="left": x-=1
        if step=="right": x+=1
    return (x,y)==(2,0)
print(goal_reached(["up","up","right","right"]))

# Q12
class Student:
    def init(self,id,name): self.student_id=id; self.student_name=name; self.student_class=""
    def display(self): print(self.student_id,self.student_name,self.student_class)

# Q13
s1=Student(1,"Ronak"); s2=Student(2,"Aman")
s1.student_class="10"; s2.student_class="12"
s1.display(); s2.display()

# Q14
import math
class Circle:
    def __init__(self,r): self.r=r
    def area(self): return math.pi*self.r**2
    def perimeter(self): return 2*math.pi*self.r
c=Circle(5)
print(c.area(),c.perimeter())

# Q15
class String:
    def __init__(self): self.s=""
    def get_String(self): self.s=input("Enter string: ")
    def print_String(self): print(self.s.upper())
str1=String(); str1.get_String(); str1.print_String()

# Q16
class Robot:
    def __init__(self,name): self.name=name; self.battery=100; self.task=None
    def perform_task(self,task): self.task=task; self.battery-=10; print(f"{self.name} doing {task}")
    def recharge(self): self.battery=100
    def status(self): print(self.name,self.task,self.battery)

r=Robot("R2D2")
r.perform_task("Cleaning")
r.status()
r.recharge()
r.status()