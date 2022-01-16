# Fonksiyonlar
#  Bir işlevi yapmak için tanımladığımız adımlar bütününe fonksiyon denir. Fonksiyonlar
def myFunction():
    pass


# şeklinde tanımlanır. Buradaki 'def' keyword'ü (anahtar kelimesi) bir fonksiyon tanımlayacağımızı belirtirken
# 'myFunction' ise bu fonksiyonun ismidir. fonksiyonların yapacağı işlevleri 'bir tab içeri' yazarız. Şuan
# fonksiyonumuzun herhangi bir işlev yapmasını istemediğimizden 'pass' anahtar kelimesini kullandık.

# Fonksiyon Parametreleri Fonksiyonlarımızın çalışması için onlara bir değer vermemiz gerekebilir. Örneğin bir
# sayının karesini alacak fonksiyona, karesini almasını istediğimiz sayıyı vermemiz gerekecektir. Fonksiyon
# parametreleri, fonksiyonun isminden sonra açtığımız parantezin içine yazılır. Eğer ki birden fazla parametre alacak
# ise, bunları ',' ile ayırmamız gerekir.

def karesiniAl(sayi):
    pass

# Dikkat! Fonksiyonumuza 'pass' yazdığımız için şimdilik herhangi bir şey yapmayacaktır.

# Örnek fonksiyon:
def topla(sayi1,sayi2):
    cevap = sayi1 + sayi2
    print(cevap)
# Şimdi ise bu fonksiyon için örnek kullanım göstermeliyiz:
topla(5,6)
# Burada olan '5,6' sayıları fonksiyonda sırayla istenen 'sayi1,sayi2'-dir.
# Bunun sonucunda '11' sayısını yazdırmış olacağız.
# Burada print() fonksiyonunu kullanarak '11' yazdırmış oluyoruz.

# Print fonksiyonu Python'ın içinde önceden tanımlanmış fonksiyonlar bulunmaktadır. 'print' fonksioyonu da en temel
# fonksiyonlardan birisidir. Print fonksiyonu, konsola çıktı vermemizi sağlar. Print fonksiyonuna paremetre olarak,
# konsola çıkmasını istediğimiz değerleri gireriz. Eğer birden fazla değer girecek isek bunları ',' ile ayırabiliriz
# çüknü print fonksiyonu birden fazla parametre alabilen bir fonksiyondur.
print("Selam!")  # => konsola 'Selam!' yazacaktır.
print("Selam", "ben", "ibrahim")  # => konsola 'Selam ben ibrahim' yazacaktır çünkü print fonksiyonu varsayılan olarak
# parametreler arasını ' ' (boşluk) ile tamamlar. Buna 'seperator' (ayırıcı) diyoruz. Print fonksiyonun seperator'unu
# değiştirmek için 'sep' adında bir parametre daha tanımlayabiliriz. Örneğin parametrelerin ', ' ile doldurulmasını
# istiyorsak 'sep=", "' yazabiliriz.
print("elma", "armut", "vişne", "kabak", sep=', ')  # => Konsola 'elma, armut, vişne, kabak' yazacaktır.


# Araştırma Önerisi: print fonksiyonun 'end' parametresini araştırınız.

# Return Deyimi Fonksiyonlar kara kutu gibi çalışır. Girdi alır işlem yapar ve çıktı üretirler. Bu çıktının başka
# bir fonksiyon ve yordamlarda kullanılabilmesi için return deyimini kullanırız.
# Yukarıda tanımladığımız karesiniAl() fonksiyonunu return deyimi ile tamamlayalım.

def karesiniAl(y):
    return y * y


# Print fonksiyonunu kullanarak karesiniAl() fonksiyonumuzun çıktısını ekrana yazdıralım.
print(karesiniAl(2))  # => Ekrana 4 çıktısını verir.


# Bazı Ön tanımlı fonksiyonlar
# //todo
#
# str
# //todo
#
#
# int
# //todo
#
#
# float
# //todo
#
#
# bool
# //todo
#
#
#