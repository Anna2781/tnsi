def decoupe(px, x, y, t):
    t = t//2
    for i in range(t):
        for j in range(t):
            px[x+i ,y+j], px[x+t+i ,y+j], px[x+t+i ,y+t+j], px[x+i ,y+t+j]= \
                   px[x+t+i ,y+j], px[x+t+i ,y+t+j], px[x+i ,y+t+j], px[x+i ,y+j]


def rotation_aux(px, x, y, t):
    # cas de base : t < = 1 : rien à faire !
    # cas récursif
    if t > 1 :
        decoupe(px, x, y, t)
        rotation_aux(px, x, y, t//2)
        rotation_aux(px, x+t//2, y, t//2)
        rotation_aux(px, x, y+t//2, t//2)
        rotation_aux(px, x+t//2, y+t//2, t//2)




from PIL import Image
im = Image.open("tigre.jpg")
px=im.load()
rotation_aux(px, 0,0,256 )
im.save("test.jpg")