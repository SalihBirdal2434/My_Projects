from datetime import date
class kisi:
    zam_orani=1.1
    kisi_sayisi=0
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
        kisi.kisi_sayisi+=1

    def show_info(self):
        print(f"Ad:{self.isim},Soyad:{self.yas}")

    def bilgilerini_soyle(self): #Instance method
        return f"Ad:{self.isim},Yaş:{self.yas}"

    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi


    @classmethod
    def string_ile_olustur(cls,str_):
        isim,yas=str_.split("-")
        return cls(isim,yas)

    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili):
        return cls(isim,date.today().year-dogum_yili)


    @staticmethod
    def dogum_yili_hesapla(kisi):
        return date.today().year-kisi.yas



kisi3=kisi.string_ile_olustur("AYŞE-25")
kisi1=kisi("Salih",19)
kisi2=kisi ("Akif",50)
kisi4=kisi.dogum_yili_ile_olustur("Fatma",2001)
print(kisi.dogum_yili_hesapla(kisi1))
kisi1.show_info()
kisi2.show_info()
kisi3.show_info()
kisi4.show_info()



