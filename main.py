import pyttsx3
import sqlite3
import random
import os

con = sqlite3.connect("kelime.db")
cursor = con.cursor()

def tablo_olustur():
	cursor.execute("CREATE TABLE IF NOT EXISTS kelimeler (id INT , anahtar TEXT , deger TEXT)")
	con.commit()

def kelime_ekle(id1 , deger1 , deger2):
	cursor.execute("INSERT INTO kelimeler VALUES (?,?,?)",(id1 , deger1 , deger2))
	con.commit()

def kelime_sil(deger1):
	cursor.execute("DELETE FROM kelimeler WHERE anahtar = ?",(deger1,))
	con.commit()

def kelimeleri_goster():
	cursor.execute("SELECT * FROM kelimeler")
	veri = cursor.fetchall()
	for i in veri:
		print("{} : {} : {}".format(i[0] , i[1] , i[2]))

def kelimeleri_say():
	cursor.execute("SELECT * FROM kelimeler")
	veri = cursor.fetchall()
	sayi = 0
	for i in veri:
		sayi +=1
	return sayi

menu = """
	[1] kelime ekle
	[2] kelime sil
	[3] kelimeleri göster
	[4] kelime sayısı
 	[5] türkçe yazma
	[6] ingilizce yazma
	[7] exit
	"""


while True:
	print(menu)
	tablo_olustur()
	istek = int(input("ne istersin : "))
	

	if istek == 1:
		os.system("cls")
		print("çıkmak için exit yaz")
		b = True
		liste = list()
		while b:

			cursor.execute("SELECT * FROM kelimeler")
			veri = cursor.fetchall()
			for i in veri:
				liste.append(i[0])

			a = kelimeleri_say()
			for i in range(1,a+1):
				if i not in liste:
					id1 = i
					break
				else:

					id1 = kelimeleri_say() + 1

			
			kelime = input("kelime gir : ")
			if kelime == "exit":
				break

			anlam = input("anlamını gir : ")
			kelime_ekle(id1 , kelime , anlam)


	if istek == 2:
		while True:
			kelime = input("silmek istediğin kelime : ")
			if kelime == "exit":
				break
			kelime_sil(kelime)
			

	if istek == 3:
		os.system("cls")
		kelimeleri_goster()
	

	if istek == 4:
		os.system("cls")
		veri = kelimeleri_say()
		print(veri)
	

	if istek == 5:
		os.system("cls")
		a = True
		print("çıkmak için exit yaz.")
		while a:
			ust_deger = kelimeleri_say()
			sayi = random.randint(1,ust_deger)
			cursor.execute("SELECT * FROM kelimeler WHERE id == ?",(sayi,))
			veri = cursor.fetchall()
			for i in veri:
				kelime = i[1]
				deger = i[2]
			sonuc = input("{}  :  ".format(kelime))
			nesne = pyttsx3.init()
			nesne.setProperty('rate',100)
			nesne.say(kelime)
			nesne.runAndWait()
			if sonuc != deger:
				print("doğru cevap : {}".format(deger))
			if sonuc == "exit":
				a = False


	if istek == 6:
		a = True
		print("çıkmak için exit yaz.")
		liste = list()
		cursor.execute("SELECT * FROM kelimeler")
		veri = cursor.fetchall()
		for i in veri:
			liste.append(i[0])
		ust_deger = max(liste)	
		while a:
			sayi = random.randint(1,ust_deger + 1)
			cursor.execute("SELECT * FROM kelimeler WHERE id == ?",(sayi,))
			veri = cursor.fetchall()
			for i in veri:
				kelime = i[2]
				deger = i[1]
			sonuc = input("{}  :  ".format(kelime))
			nesne = pyttsx3.init()
			nesne.setProperty('rate',100)
			nesne.say(deger)
			nesne.runAndWait()
			if sonuc != deger:
				print("doğru cevap : {}".format(deger))
			if sonuc == "exit":
				a = False
	

	if istek == 7:
		break


