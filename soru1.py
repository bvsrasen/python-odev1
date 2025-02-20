'''
Görev 1: Kullanıcıdan iki sayı alıp, aşağıdaki işlemleri yaparak ekrana yazdıran bir Python programı yazın:
Toplama (+)
Çıkarma (-)
Çarpma (* )
Bölme (/)
Mod alma (%)
Üs alma (** )
'''

sayi1=int(input("lütfen 1.sayıyı girin: "))
sayi2=int(input("lütfen 2.sayıyı girin: "))

#Sayi1 ve sayi2 isimli iki değişken oluşturdum 
#ikisini de kullanıcıdan istedim ve string olarak aldığım için işleme sokabilmek adına bunları int a çevirdim

toplam =sayi1+sayi2
cikarma=sayi1-sayi2
carpma=sayi1*sayi2
tambolme=sayi1//sayi2
mod=sayi1%sayi2
ussu=sayi1**sayi2

#Sonra her işlem için değişken isimleri oluşturup matematiksel olarak formüllerini girdim

print(f"{sayi1} + {sayi2} = {toplam}")
print(f"{sayi1} - {sayi2} = {cikarma}")
print(f"{sayi1} * {sayi2} = {carpma}")
print(f"{sayi1} / {sayi2} = {tambolme}")
print(f"{sayi1} % {sayi2} = {mod}")
print(f"{sayi1} ** {sayi2} = {ussu}")

#Son olarak bu işlemlerin sonuçlarını printle yazdırdım
