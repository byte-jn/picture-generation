from PIL import Image
import random

print("Wie viel Kaos soll es geben")
cause = input()

if cause == "":
    cause = 1
else:
    cause = int(cause)

print("Wie groß soll das Bild sein?(240p/360p/480p/720p/1080p/1440p/4k/8k)")
pie = input()
if pie == "240p":
    width = 426
    height = 240
    p = 2
elif pie == "360p":
    width = 640
    height = 360
    p = 2
elif pie == "480p":
    width = 854
    height = 480
    p = 2
elif pie == "720p":
    width = 1280
    height = 720
    p = 3
elif pie == "1080p":
    width = 1920
    height = 1080
    p = 4
elif pie == "1440p":
    width = 2560
    height = 1440
    p = 5
elif pie == "4k":
    width = 3840
    height = 2160
    p = 10
    pie = "2160p(4k)"
elif pie == "8k":
    width = 7680
    height = 4320
    p = 14
    pie = "4320p(8k)"
elif pie != "":
    p = 1
    width = int(pie)
    height = int(pie)
else:
    p = 1
    pie = 1
    width = 255
    height = 255

# Variablen Werte
x = 0
y = 0
z = 0
r = random.randint(0,255)
b = random.randint(0,255)
g = random.randint(0,255)

# Variablen Nachtragung
rg = r
gg = g
bg = b
a = p
c = p
e = p
f = p
XMotion = True

Bild = Image.new('RGB', (width, height), (255, 255, 255, 0))
while True:
    z = z + 1
    print("X: "+str(x+1)+" Y: "+str(y+1), " Durchlauf: " + str(z))
    Bild.putpixel((x, y), (r, g, b, 0))

    if XMotion == True:
        if x == width-1:
            XMotion = False
            if y == height-1:
                break
            else:
                y = y + 1
        else:
            x = x + 1

    elif XMotion == False:

        if x == -1:
            XMotion = True
            if y == height-1:
                break
            else:
                y = y + 1
        else:
            x = x - 1


    for i in range(0, cause):
        rr = random.randint(0, 2)
        if rr == 2:
            r = r + 1
        elif rr == 0:
            r = r - 1

        if r < 0:
            r = r + 2
        elif r > 255:
            r = r - 2

        rr = random.randint(0, 2)
        if rr == 2:
            b = b + 1
        elif rr == 0:
            b = b - 1

        if b < 0:
            b = b + 2
        elif b > 255:
            b = b - 2

        rr = random.randint(0, 2)
        if rr == 2:
            g = g + 1
        elif rr == 0:
            g = g - 1

        if g < 0:
            g = g + 2
        elif g > 255:
            g = g - 2


Bild.show()
Bild.save("Bild" + ".png")
