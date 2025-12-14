# 1
class Oquvchi:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.fanlar = []

    def fan_qosh(self, fan):
        self.fanlar.append(fan)

    def malumot(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Fanlar: {', '.join(self.fanlar)}"

o1 = Oquvchi("Ali", 16)

o1.fan_qosh("Matematika")
o1.fan_qosh("Informatika")

print(o1.malumot())



# 2
class Telefon:
    def __init__(self, brend, model, batareya):
        self.brend = brend
        self.model = model
        self.batareya = batareya 

    def batareya_korsat(self):
        return f"Batareya: {self.batareya}%"

    def zaryadla(self, foiz):
        self.batareya += foiz
        if self.batareya > 100:
            self.batareya = 100

t1 = Telefon("Samsung", "A51", 45)

print(t1.batareya_korsat())
t1.zaryadla(30)
print(t1.batareya_korsat())
