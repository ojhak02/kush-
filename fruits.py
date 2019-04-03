a=["apple","mango","grapes"]
for z in a  :
    print(z)
a.append("kiwi")
print(a)
a.remove("apple")
print(a)
if "mango" in a:
        print("yes it does")
a[0]="gauava"
print(a)
print(len(a))
x=456
x=a.copy()
print(x)
y=(a.count("apple"))
print(y)
print(a[2])

b=("123","xyz","abc")
print(b[1])
print(b*3)
print(len(b))

c={"bike","car","train"}
c.add("superbike")
print(c)
c.remove("car")
print(c)
c.pop()
print(c)

d={"bike","car","train"}
e={"csk","kkr","rcb"}
d.update(e)
print(d)
z=d.difference(e)
print(z)
d.intersection(e)
print(d)
d.difference_update(e)
print(d)
            

