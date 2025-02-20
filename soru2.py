'''
Görev 2:Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların toplamını hesaplayan bir Python programı yazın.
(For veya While döngüsü kullanın.)
'''
sayi=int(input("1 den hangi sayıya kadar toplam almak istiyorsunuz: "))
#kullanıcıdan sayıyı string aldım int a çevirdim
toplam=0
#toplama sonucunu atayabilmek için başta 0 a eşit bir değişken oluşturdum 
for i in range(1,sayi+1):
    toplam=toplam+i
#1 den sayi+1 e kadar, sayi+1 dahil olmicak şekilde 1 er 1 er artan tüm sayıları tek tek i değişkenine ata 
#sonra bunları toplama değişkeniyle sıra sıra topla dedim

print("1 den girdiğiniz sayıya kadarki tam sayıların toplamı = ",toplam)
#sonucu ekrana yazdırdım