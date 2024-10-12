import pgzrun
import random
WIDTH=700
HEIGHT=700
def draw():
    rect=Rect((70,100),(200,200))
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    screen.draw.rect(rect,(r,g,b))
pgzrun.go()