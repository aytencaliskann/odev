print("********************\nATM SİSTEMİNE HOŞGELDİNİZ\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye  = 1000 # Bakiyemiz 1000 lira olsun.

while True:
    islem = input("İşlemi giriniz:")

    if (islem == "q"):
        print("Yine bekleriz....")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar:"))

        bakiye += miktar
        print("Para yatırma işleminiz başarılı")

    elif (islem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (miktar<=bakiye ):
            bakiye-=miktar
        else:
                print("Yetersiz Bakiye")
    else:
        print("Hatalı bir tuşa bastınız tekrar deneyiniz")
