z =100
x =100
c =100
def setup():
    size(1000,1000)
def draw():
    clear()
    global z,x,c
    imv=loadImage("spak.jpg")
    image(imv,z,800,z,100)
    imv=loadImage("bbb.png")
    image(imv,500,x,100,100)
    z +=1
    x +=3
    c +=1
