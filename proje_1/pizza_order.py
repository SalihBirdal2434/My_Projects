class PizzaSiparisi:    
    def __init__(self):
        print("""Merhaba! Pizza Sipariş Uygulaması olan BirdalPizza uygulamasına hoşgeldiniz! Menümüz Aşağıdaki gibidir:
        
        ----------PİZZALAR----------

        1-Pepperoni Pizza   (89,90 TL)
        2-Mix Pizza     (99,90 TL)
        3-Vegan Pizza   (79,90 TL)
        4-Margarita Pizza   (89,90 TL)
        5-Barbekü Tavuklu Pizza (95,90 TL)


        ----------APARATLAR----------
        1-Patates   (20,90 TL)
        2-Soğan Halkası (18,90 TL)
        3-Çıtır Peynir  (20,90 TL)
        4-Mix   (22,90 TL)
        5-Kanat (29,90 TL)
        0-Aparat istemiyorum

        
        ----------İçeçekler----------

        1-Kola  (9 TL)
        2-Ayran (8 TL)
        3-Fanta (9 TL)
        4-Su    (6 TL)
        5-Meyveli Soda  (7.5 TL)
        0-İçecek istemiyorum

        """)
        self.pizza=int(input("Hangi numaradan pizza çeşidi almak istersiniz:"))
        self.aparat=int(input("Hangi numaradan aparat almak istersiniz:"))
        self.icecek=int(input("Hangi numaradan içecek almak istersiniz:"))
        self.total=0
    def pizza_hesaplama(self):
        if self.pizza==1:self.total+=89.90
        if self.pizza==2:self.total+=99.90
        if self.pizza==3:self.total+=79.90
        if self.pizza==4:self.total+=89.90
        if self.pizza==5:self.total+=95.90
    def aparat_hesaplama(self):
        if self.aparat==1:self.total+=20.90
        if self.aparat==2:self.total+=18.90
        if self.aparat==3:self.total+=20.90
        if self.aparat==4:self.total+=22.90
        if self.aparat==5:self.total+=29.90
        if self.aparat==0:self.total+=0
    def icecek_hesaplama(self):
        if self.icecek==1:self.total+=9
        if self.icecek==2:self.total+=8
        if self.icecek==3:self.total+=9
        if self.icecek==4:self.total+=6
        if self.icecek==5:self.total+=7.5
        if self.icecek==0:self.total+=0

    def hesap_tutari(self):
        print(f"""
        {self.pizza} nolu pizzanızı seçtiniz.
        {self.aparat} nolu aparatınız seçtiniz.
        {self.icecek} nolu içeceğini seçtiniz.
        Toplam Tutarınız:{self.total:.2f} TL tutmuştur.
              """)
    print(hesap_tutari)
    
p1=PizzaSiparisi()
p1.pizza_hesaplama()    
p1.aparat_hesaplama()
p1.icecek_hesaplama()
p1.hesap_tutari()

























          
