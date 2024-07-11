from PIL import Image

print("Wie groß soll das Bild sein?(240p/360p/480p/720p/1080p/1440p/4k/8k)")
p=input()
width = 255
height = 255
if p == "240p":
    width = 426
    height = 240
elif p == "360p":
    width = 640
    height = 360
elif p == "480p":
    width = 854
    height = 480
elif p == "720p":
    width = 1280
    height = 720
elif p == "1080p":
    width = 1920
    height = 1080
elif p == "1440p":
    width = 2560
    height = 1440
elif p == "4k":
    width = 3840
    height = 2160
elif p == "8k":
    width = 7680
    height = 4320

#Variablen Werte
x = 0
y = 0
z = 0
color = input("Welche Farbe soll es sein...")
if color == "lila":
    r=255
    b=255
    g=0
elif color == "rot":
    r=255
    b=0
    g=0
elif color == "blau":
    r=0
    b=255
    g=0
elif color == "gelb":
    r=255
    b=0
    g=255
elif color == "green":
    r=0
    b=0
    g=255
elif color == "cyan":
    r=0
    b=255
    g=255
else: 
    r=255
    b=255
    g=0

#Variablen Nachtragung
rg=r
gg=g
bg=b
forward=True
forward2=True

Bild = Image.new('RGB', (width, height), (255, 255, 255, 0))
while True:
    z=z+1
    print("X: "+str(x)+" Y: "+str(y)," Durchlauf: "+ str(z))
    if x == width:
        x=0
        r=rg
        if b == 0: forward2 = False
        elif b == 255: forward2 = True
        if forward2 == True:
            y = y + 1
            b = b - 1
        elif forward2 == False:
            y = y + 1
            b = b + 1
        if y == height:
           break
    if r == 0:forward = False
    elif r == 255: forward = True
    if forward == True:
        Bild.putpixel((x, y), (r, g, b, 0))
        x = x + 1
        r = r - 1
    elif forward == False:
        Bild.putpixel((x, y), (r, g, b, 0))
        x = x + 1
        r = r + 1
Bild.show()
Bild.save("Bild.png")
