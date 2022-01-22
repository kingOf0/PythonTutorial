# Matematik
#  Python'da bir çok cebirsel ifade beklendiği gibi çalışır. Örneğin '+' işareti iki veriyi toplayacaktır.
#  Bu toplama sayılarda üstüne ekleme, metinlerde ardına ekleme şeklindedir.
x = 2
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
z = x * y  # x = 2, y = 4 olduğundan z = 8 olacaktır.
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
x = z // y + 1  # z = 8, y = 4 olduğundan x = 8 // 5 işlemi gerçelşeşecektir. 8 / 5 = 1.6, fakat tam bölüm veri türünü
# koruyarak integer / integer'dan integer elde edecek ve 1.6 float'ını integer'a çevirecektir. Yani sonuç 1 dir.
#
# Modulus | Modül
#  Matematikteki 'kalan bulma' operatörüdür.
#  11 % 3 => 2
#
# Pow(er) | Kuvvet Alma
#  2 ** 3 => 8
#  4 ** 2 => 16
#  5 ** -1 => 0.2
