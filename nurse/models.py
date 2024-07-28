from django.db import models
from django.utils import timezone

ovqatlanish_turi = (
    ("To'g'ri", "To'g'ri"),
    ("Noto'g'ri", "Noto'g'ri")
)
jismoniy_faolligi = (
    ('Faol', "Faol"),
    ('Nofaol', "Nofaol")
)
zararli_odat = (
    ('Mavjud', "Mavjud"),
    ('Mavjud emas', "Mavjud emas")
)
salomatlik_guruhi = (
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4")
)
soglamlashtirish = (
    ('Ambulator', "Ambulator"),
    ('Tuman', "Tuman"),
    ('Viloyat', "Viloyat"),
    ('Respublika', "Respublika")
)
davolash_chorak = (
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4")
)


class People(models.Model):
    familiyasi = models.CharField(max_length=200)
    ismi = models.CharField(max_length=200)
    sharifi = models.CharField(max_length=200)
    tugilgan_kuni = models.DateField(default=timezone.now)
    address = models.CharField(max_length=300)
    passport = models.CharField(max_length=150)
    pinfl = models.PositiveBigIntegerField()
    telefon_raqami = models.CharField(max_length=13)
    tibbiy_brigada = models.PositiveBigIntegerField()
    ovqatlanish_turi = models.CharField(max_length=150, choices=ovqatlanish_turi)
    jismoniy_faolligi = models.CharField(max_length=150, choices=jismoniy_faolligi)
    zararli_odat = models.CharField(max_length=150, choices=zararli_odat)
    vazn = models.IntegerField()
    buy = models.IntegerField()
    tvi = models.IntegerField()
    tashhisi = models.TextField()
    salomatlik_guruhi = models.CharField(max_length=150, choices=salomatlik_guruhi)
    soglamlashtirish = models.CharField(max_length=150, choices=soglamlashtirish)
    muassasa_nomi = models.CharField(max_length=200)
    davolash_chorak = models.CharField(max_length=150, choices=davolash_chorak)
    xatlov_sana = models.DateField(default=timezone.now)

    def __str__(self):
        return (f"{self.familiyasi}, "
                f"{self.ismi}, "
                f"{self.sharifi}, "
                f"{self.tugilgan_kuni}, "
                f"{self.address}, "
                f"{self.passport}, "
                f"{self.pinfl}, "
                f"{self.telefon_raqami}, "
                f"{self.tibbiy_brigada}, "
                f"{self.ovqatlanish_turi}, "
                f"{self.jismoniy_faolligi}, "
                f"{self.zararli_odat}, "
                f"{self.vazn}, "
                f"{self.buy}, "
                f"{self.tvi}, "
                f"{self.tashhisi}, "
                f"{self.salomatlik_guruhi}, "
                f"{self.soglamlashtirish}, "
                f"{self.muassasa_nomi}, "
                f"{self.davolash_chorak}, "
                f"{self.xatlov_sana}")
