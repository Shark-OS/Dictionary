import pgzrun
import random
WIDTH=700
HEIGHT=700
w=200
h=200
def draw():
    global w,h,x,y
    for i in range(3):
        rect=Rect((200,200),(w,h))
        w=w+50
        h=h+50
        rect.center=200,200

    
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        screen.draw.rect(rect,(r,g,b))
pgzrun.go()