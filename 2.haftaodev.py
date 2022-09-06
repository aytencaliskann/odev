""""
#Ödev 1-1000 arasındaki tek ve çift sayıların toplamlarını ayrı ayrı hesaplayan kod
tektp=0
cifttp=0
sayi=1
while (sayi<=1000):
    if sayi%2==0:
        print(sayi)
        cifttp+=sayi
        sayi+=1
    else:
        tektp+=sayi
        sayi+=1
print(f"tek sayıların toplamı{tektp}")
print(f"çift sayıların toplamı{cifttp}")
"""
"""
#1den kullanıcının girdiği sayıya kadar olan sayıların eğer tek ise karesini
# çift ise küpünün toplamını ayrı ayrı hesaplayan kod

tektp=0
cifttp=0
baslangic=1
bitis=int(input("bir sayı giriniz"))

while (baslangic<bitis):

    if baslangic%2==0:
               print(baslangic**3)
               cifttp+=baslangic**3
               baslangic+=1
    else:
               print(baslangic**2)
               tektp+=baslangic**2
               baslangic+=1

print(f"tek sayıların toplamı{tektp}")
print(f"çift sayıların toplamı{cifttp}")
"""
"""
#Kullanıcı giriş ekranı

kullaniciadi="aytencaliskan"
sifre="123456"
email="ayten@caliskan.com"

username=input("kullanıcı adı/ email giriniz")
password=input("şifre giriniz")

if (username== kullaniciadi or username==email ) and (password==sifre):
     print("giriş başarılı")


else:
     print(f"kullanıcı adı veya şifre hatalı")
"""
