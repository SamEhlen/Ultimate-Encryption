from PIL import Image
import random

def encrypt(msg, pasw, img):
    im = Image.open(img, "r")
    pix = list(im.getdata())
    pixa=[]
    alphabet = "~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    I = 0
    i = 0
    while i < len(msg) or i < len(pasw):
        try:
            md = alphabet.index(msg[i])
        except Exception as e:
            md = 0
        try:
            pd = alphabet.index(pasw[i])
        except Exception as e:
            pd = 0
        i += 1
        nextI = random.randint(0, 255)
        pix[I] = (md, pd, nextI)
        pixa.append([md, pd, nextI])
        I = nextI
    pix[I] = (0,0,0)
    im2 = Image.new(im.mode, im.size)
    im2.putdata(pix)
    im2.save(img)

def decrypt(paswI, img):
    im = Image.open(img, "r")
    alphabet = "~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    pix = list(im.getdata())
    i = 0
    nextI = 0
    pasw = []
    msg = []
    while (pix[i] != (0,0,0)):
        msg.append(pix[i][0])
        pasw.append(pix[i][1])
        i = pix[i][2]

    msgT = [alphabet[x] for x in msg]
    paswT = [alphabet[x] for x in pasw]

    if paswI == ("".join(paswT).strip("~")):
        print("".join(msgT).strip("~"))
