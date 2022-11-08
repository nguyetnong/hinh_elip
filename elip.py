import turtle
import random
r=int(input("nhap ban kinh:"))
mau=["red","blue","green","pink","brown"]
turtle.speed(10)
turtle.pensize(3)
def draw(rad):

      for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)
    #turtle.seth(-45)
cnt=0
cnt_mau=0

while cnt<50:
    turtle.color(mau[cnt_mau])
    # calling draw method
    draw(100)
    turtle.right(15)
    cnt_mau +=1
    if cnt_mau >= 5:
        cnt_mau = 0
    cnt+=1
turtle.done()
