__author__ = "Emre METİN"

def dortgen_alan_hesapla_v1():
    print("-"*20)
    print("Kare Alan Hesaplama Aracına Hoşgeldiniz...")
    print("-"*20)

    uzun_kenar = int(input("Uzun Kenarı Giriniz :"))
    kısa_kenar = int(input("Kısa Kenarı Giriniz :"))
    sonuc = uzun_kenar*kısa_kenar
    print("Karenin Alanı :", sonuc)

    print("-"*20)

def daire_alan_hesapla_v1():
    print("-"*20)
    print("Daire Alan Hesaplama Aracına Hoşgeldiniz...")
    print("-"*20)

    yaricap = int(input("Dairenin Yarıçapını Giriniz :"))
    daire_sonuc = 3.14*yaricap**2
    print("Dairenin Alanı :", daire_sonuc)
while True:
    print("-"*20)
    print("Kare Alanı Hesapla       (1)")
    print("Daire Alanı Hesapla      (2)")
    print("-"*20)

    secim = input("Alanını Hesaplamak İstediğiniz Şekli Seçiniz :")
    if secim == "1":
        dortgen_alan_hesapla_v1()
    elif secim == "2":
        daire_alan_hesapla_v1()
    else:
        print("Seçiminiz Geçersiz. Program Sonlandırılıyor...")
        break
