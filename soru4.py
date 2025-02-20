'''
Görev 4: Kullanıcıdan alınan bir metni ters çeviren ve ekrana yazdıran bir Python programı yazın. (Döngü kullanarak yapın.)
'''

metin=input("ters çevirilecek metni yazın: ")
#kullanıcıdan ters çevirilcek metni alıyorum

tersmetin=""
#ters çevirilcek metinin harflerini tek tek atayıp birleştirebilceğim boş bir string değişkeni tanımlıyorum
for harf in metin:
    tersmetin= harf+tersmetin #her harf başa eklencek

print(tersmetin)
