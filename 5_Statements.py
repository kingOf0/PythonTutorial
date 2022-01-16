
# If Statement | Koşul İfadesi
# Bir kod dizisinin sadece belli bir durum gerçeklendiğinde çalıştırılması istendiğinde if statement kullanılır.
#
# if (Boolean):
#   ....
# else:
#   .....
#
# Şeklinde bir kullanımına sahip olan koşul ifadesi parantezlerinin içine aldığı Boolean değeri True yani doğru
# olduğunda bir tab içindeki komutları çalıştıracak. Eğer False yani yanlış ise else bloğunun bir tab altındaki
# komutları çalıştıracak.
#
# Aşağıdaki örnekte sayı değişkeninin değeri sıfır'a eşitse konsola "sayı sıfır." yazdırıyoruz. Değilse "Sayı sıfır
# değil." yazdırıyoruz.
def sifirMi(sayi):
    if sayi == 0:
        print("Sayı sıfır.")
    else:
        print("Sayı sıfır değil.")
