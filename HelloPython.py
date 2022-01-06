# Bu bir yorum satırıdır. Yorum satırları '#' ile başlar. Python, bu satırları görmezden gelir.
"""
  Birden fazla satırdan oluşacak yorum satırları üç adet " arasına alınır
  Bu yorum satırları genellikle dökümantasyonlarda kullanılır.
"""

# Değişkenler
#  Bir veriyi hafızada depolamak için değişkenleri kullanırız. Değişken isimlendirmede bir kaç kural
#  vardır. Örneğin bir değişken ismi sayı veya özel işaretler ile başlayamaz veya pythondaki bazı özel anlamlara gelen kelimelerden
#  oluşamaz.

# Değişken Tanımlamak:
#  'değişken_ismi = değer' şeklinde kullanılır. Buna 'assign' veya 'assignment' yani 'atama' denir.
# Aşağıda x adında bir değişken oluşturup bunun değerini 5 olarak atadık.
x = 5

# Matematik
#  Python'da bir çok cebirsel ifade beklendiği gibi çalışır. Örneğin '+' işareti iki veriyi toplayacaktır.
#  Bu toplama sayılarda üstüne ekleme, metinlerde ardına ekleme şeklindedir.
y = x + 2  # y'nin değeri 4 olacaktır. Çünkü x'in değeri 2 olduğunda 2 + 2 = 4 dür.
#
# Bazı aritmetik operatörler aşağıda verilmiştir:
#
# Addition | Toplama
#  İki sayısal değeri toplar.
#  10 + 1 => 11
#
# Substraction | Çıkarma
#  İki sayısal değeri çıkarır.
#  10 - 2 => 8
#
# Multiplication | Çarpma
#  İki sayısal değeri çarpar.
#  10 * 3 => 30
#
# Division | Bölüm
#  İki sayısal değeri böler. Dikkat! Bölüm değeri her zaman float (kesirli sayı) türündedir!
#  10 / 2 => 5.0
#  12 / 5 => 2.4
#
# Integer Division  | Tam Sayı Bölümü
#  İki sayısal değeri böler. Dikkat! Bölüm değeri her zaman integer (tam sayı) türündedir!
#  10 / 2 => 5
#  12 // 5 => 2
#
# Modulus | Modül
#  Matematikteki 'kalan bulma' operatörüdür.
#  11 % 3 => 3
#
# Pow(er) | Kuvvet Alma
#  2 ** 3 => 8
#  4 ** 2 => 16
#  5 ** -1 => 0.2


# Veri Türleri Her bir verinin bir türü vardır.
#  Veri türleri, veri üzerinde işlem yapmamızı kolaylaştırır. Veriler ile bir işlem yapılırken genellikle aynı tür
#  olmaları gerekir. Örneğin karekökünü almak sayılarda kullanılan bir işlev iken bir metnin karekökünü almayı
#  beklemeyiz.
#
# Bazı veri türleri aşağıda verilmiştir.
#
# Integer | Tam Sayı
#  Kısaca 'int' olarak da bilinir. Tam sayıları ifade eder.
#
# Float | Ondalıklı Sayı Floating Point 'yani Kayan Noktalı Sayı' olarak da bilinir. Fractional numbers yani kesirli
#  (rasyonel) sayıları ifade eder.
#
# Aşağıda 'pi' adında bir değişken tanımladık ve değerini '3.14' olarak atadık.
# Dikkat! matematikteki pi sayısının gerçek değeri 3.14 değildir!
pi = 3.14
#
# Boolean | Boole Cebiri
#  True (doğru) ve yanlış (false) mantıksal ifadelerini belirtir.
#  True ve False büyük-küçük harf'e duyarlıdır. Yani true ya da false şeklinde bir kullanım yoktur.
#
#  Aşağıda 'z' adında bir değişken oluşturduk ve bu değişkenin değerini True yani Doğru olarak atadık.
z = True
#
# String | Metin
#  Yazı, dizgi, katar gibi isimleri de vardır. Harflerden oluşan bir diziyi ifade eder.
#  Girilen değer `'` veya `"` içerisine alınmalıdır.
#
# Aşağıda üç adet değişken oluşturduk ve bu değişkenlerin değerini sırasıyla "ibrahim", "kingOf0" ve "c" olarak atadık.
isim = "ibrahim"
nick = 'kingOf0'
harf = 'c'


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
    return cevap
# Burada olan return fonksiyondan hangi değeri döndürdüğümüzü bildiriyor. 
# Şimdi ise bu fonksiyon için örnek kullanım göstermeliyiz:
print(topla(5,6))
# Burada olan '5,6' sayıları fonksiyonda sırayla istenen 'sayi1,sayi2'-dir.
# Bunun sonucunda '11' sayısını yazdırmış olacağız.
# Burada print() fonksiyonunu kullanarak fonksiyondan geri döndürülen değeri yazdırabiliriz. Tabii ki, geri döndürülen değeri bir değişkene de verebiliriz.

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


