import turtle
fred = turtle.Turtle()
fred.color("red")
arr=["red","yellow","blue","purple","black"]
# for i in range(0,360):
#     fred.color(arr[i%len(arr)])
#     fred.right(i)
#     fred.forward(i)

fred.forward(100)
fred.back(50)
fred.right(90)
fred.forward(100)
for i in range(0,180):
    fred.right(1)
    fred.forward(1)
fred.color("white")
fred.forward(170)
fred.color("red")
for i in range(0,360):
    fred.right(1)
    fred.forward(1)