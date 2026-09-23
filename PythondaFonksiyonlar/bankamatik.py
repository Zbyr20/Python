#bankamatik uygulaması

ad = 'Ali'# değişkenler kullanmadık çünkü fonksiyon içerisinde kopyalanır




hesapA = {
    'ad' : 'Zübeyir Aslan',
    'hesapNo' : '12345678',
    'bakiye' : 3000,
    'ekHesap': 2000
}

hesapB = {
    'ad' : 'Kazım Aslan',
    'hesapNo' : '9123743',
    'bakiye' : 4000,
    'ekHesap': 10000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsin')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')
            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print("paranızı kullanabilirsiniz")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadı. Ek hesabınızda {hesap['ekHesap']} tl bulunmaktadı")
    
paraCek(hesapA, 3000)

paraCek(hesapA, 1000)

paraCek(hesapA,1000)

