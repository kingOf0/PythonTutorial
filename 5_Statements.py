# Statements | İfadeler
# todo
#
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


# Elif Statement
# Kendisinden önceki statementların hepsinin False olduğu durumda kendi içindeki boolean değeri True ise içindeki kodu
# çalıştırır.
#
# Program kendinden sonraki diğer statementları kontrol etmez. ardı ardına eklenen if, elif ve else
# statementlardan herhangi birisi çalıştğında program sonraki statementları kontrol etmez.
#
def yasKontrol(yas):
    if yas > 18:
        print("Yaşın 18'ten büyük")
    elif yas == 18:  # yas <= 18 && yas == 18 durumudur.
        print("18 yaşındasın")
    else:  # yas < 18 && yas != 18 durumudur.
        print("18 yaşından küçüksün")
