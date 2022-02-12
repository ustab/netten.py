# 1-bilgisyar ile sozcuk yaristirma
import random
def bilgisayar_secimi():
    n=random.randint(1,3)
    if n==1:
        return "tas"
    elif n==2:
        return "kagit"
    else:
        return "makas"

kullanici_secimi=input("tas, kagit, makas:")
bilgisayar_secimi= bilgisayar_secimi()
print("bilgisayar:", bilgisayar_secimi)

if bilgisayar_secimi==kullanici_secimi:
      print("berabere")
elif bilgisayar_secimi=="tas" and kullanici_secimi=="kagit":
      print("siz kazandiniz")
elif bilgisayar_secimi=="kagit" and kullanici_secimi=="makas":
      print("siz kazandiniz")
elif bilgisayar secimi=="makas"and kullanici_secimi=="kagit":
      print("siz kazandiniz"
else:
      print("kaybettiniz") 

# 2-bilgisyar ile sozcuk yaristirma
import random
def bilgisayar_secimi():
    n=random.randint(1,3)
    if n==1:
        return "tas"
    elif n==2:
        return "kagit"
    else:
        return "makas"

skor_kullanici=0
skor_bilgisayar=0
while True:

kullanici_secimi=input("tas, kagit, makas:")
bilgisayar_secimi= bilgisayar_secimi()
print("bilgisayar:", bilgisayar_secimi)

if bilgisayar_secimi==kullanici_secimi:
      print("berabere")
elif bilgisayar_secimi=="tas" and kullanici_secimi=="kagit":
      skor_kullanici+=1
      print("siz kazandiniz")
elif bilgisayar_secimi=="kagit" and kullanici_secimi=="makas":
      print("siz kazandiniz")
      skor_kullanici+=1
elif bilgisayar secimi=="makas"and kullanici_secimi=="kagit":
      print("siz kazandiniz"
      skor_kullanici+=1
else:
      print("kaybettiniz") 
      skor_bilgisayar+=1

      print("siz:", skor_kullanici, "vs bilgisayar:"skor_bilgisayar)
 
if skor_kullanici==3 or skor_bilgisayar==3:
      break


if skor_bilgisayar > skor_kullanici:
    print("kaybettiniz")
else:
    print("kazandiniz")

# 3- 2-bilgisayari hileli olarak devamli kazanmasi
import random
def bilgisayar_hilelisecimi(kullanici_secimi)():
    if kullanici_secimi("tas"):
        return "kagit"
    elif if kullanici_secimi("kagit"):
        return "makas"
    else:
        return "tas"

skor_kullanici=0
skor_bilgisayar=0
while True:

kullanici_secimi=input("tas, kagit, makas:")
kullanici_secimi= bilgisayar_hilelisecimi(kullanici_secimi)
print("bilgisayar:", bilgisayar_secimi)

if bilgisayar_secimi==kullanici_secimi:
      print("berabere")
elif bilgisayar_secimi=="tas" and kullanici_secimi=="kagit":
      skor_kullanici+=1
      print("siz kazandiniz")
elif bilgisayar_secimi=="kagit" and kullanici_secimi=="makas":
      print("siz kazandiniz")
      skor_kullanici+=1
elif bilgisayar secimi=="makas"and kullanici_secimi=="kagit":
      print("siz kazandiniz"
      skor_kullanici+=1
else:
      print("kaybettiniz") 
      skor_bilgisayar+=1

      print("siz:", skor_kullanici, "vs bilgisayar:"skor_bilgisayar)
 
if skor_kullanici==3 or skor_bilgisayar==3:
      break


if skor_bilgisayar > skor_kullanici:
    print("kaybettiniz")
else:
    print("kazandiniz")

# 4- bilgisayari hileli olarak arada bir caktirmadan devamli kazanmasi
import random
def bilgisayar_hilelisecimi(kullanici_secimi)():
    if kullanici_secimi("tas"):
        return "kagit"
    elif if kullanici_secimi("kagit"):
        return "makas"
    else:
        return "tas"

skor_kullanici=0
skor_bilgisayar=0
while True:

    kullanici_secimi=input("tas, kagit, makas:")
    n=random.randit(1,2)
    if n==1:
    bilgisayar_secimi=bilgisayar_secimi()
    else n==2:
    bilgisayar_secimi= bilgisayar_hilelisecimi(kullanici_secimi)
print("bilgisayar:", bilgisayar_secimi)

if bilgisayar_secimi==kullanici_secimi:
      print("berabere")
elif bilgisayar_secimi=="tas" and kullanici_secimi=="kagit":
      skor_kullanici+=1
      print("siz kazandiniz")
elif bilgisayar_secimi=="kagit" and kullanici_secimi=="makas":
      print("siz kazandiniz")
      skor_kullanici+=1
elif bilgisayar secimi=="makas"and kullanici_secimi=="kagit":
      print("siz kazandiniz"
      skor_kullanici+=1
else:
      print("kaybettiniz") 
      skor_bilgisayar+=1

      print("siz:", skor_kullanici, "vs bilgisayar:"skor_bilgisayar)
 
if skor_kullanici==3 or skor_bilgisayar==3:
      break


if skor_bilgisayar > skor_kullanici:
    print("kaybettiniz")
else:
    print("kazandiniz")