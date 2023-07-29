from django.db import models
from django.db.models import CASCADE
from storages.backends.s3boto3 import S3Boto3Storage


class RAMMemory(models.Model):
    MANUFACTURER_CHOICES = {
        ('Corsair', 'Corsair'),
        ('Kingston', 'Kingston'),
        ('Crucial', 'Crucial'),
        ('G.Skill', 'G.Skill'),
        ('ADATA', 'ADATA'),
        ('Samsung', 'Samsung'),
        ('Transcend', 'Transcend'),
        ('Patriot', 'Patriot'),
        ('Mushkin', 'Mushkin'),
        ('Hynix', 'Hynix'),
        ('Micron', 'Micron'),
        ('PNY', 'PNY'),
        ('Team Group', 'Team Group'),
        ('GeIL', 'GeIL'),
        ('Apacer', 'Apacer'),
        ('Smart Modular', 'Smart Modular'),
        ('Qimonda', 'Qimonda'),
    }

    DDR_RAM_TYPES = (
        ("DDR2", "DDR2"),
        ("DDR3", "DDR3"),
        ("DDR4", "DDR4"),
        ("DDR5", "DDR5"),
    )

    RAM_FREQUENCIES = {
        'DDR2': (
            ('400Mhz', '400Mhz'),
            ('533Mhz', '533Mhz'),
            ('667Mhz', '667Mhz'),
            ('800Mhz', '800Mhz'),
            ('1066Mhz', '1066Mhz'),
        ),

        'DDR3': (
            ('800Mhz', '800Mhz'),
            ('1066Mhz', '1066Mhz'),
            ('1333Mhz', '1333Mhz'),
            ('1600Mhz', '1600Mhz'),
            ('1866Mhz', '1866Mhz'),
            ('2133Mhz', '2133Mhz'),
        ),

        'DDR4': (
            ('1600Mhz', '1600Mhz'),
            ('1866Mhz', '1866Mhz'),
            ('2133Mhz', '2133Mhz'),
            ('2400Mhz', '2400Mhz'),
            ('2666Mhz', '2666Mhz'),
            ('2933Mhz', '2933Mhz'),
            ('3200Mhz', '3200Mhz'),
        ),

        'DDR5': (
            ('3200Mhz', '3200Mhz'),
            ('3600Mhz', '3600Mhz'),
            ('4000Mhz', '4000Mhz'),
            ('4800Mhz', '4800Mhz'),
            ('5000Mhz', '5000Mhz'),
            ('5120Mhz', '5120Mhz'),
            ('5333Mhz', '5333Mhz'),
            ('5600Mhz', '5600Mhz'),
            ('6400Mhz', '6400Mhz'),
            ('7200Mhz', '7200Mhz'),
        ),

    }
    brand = models.CharField(
        max_length=50,
        choices=MANUFACTURER_CHOICES,
    )

    ram_type = models.CharField(
        max_length=10,
        choices=DDR_RAM_TYPES,
    )

    ram_frequency = models.CharField(
        max_length=100,
    )

    ram_image = models.ImageField()

    def get_ram_type_and_frequency(self):
        return self.RAM_FREQUENCIES.get(self.ram_type, ())

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()
        if self.ram_image:
            self.ram_image.name = self.ram_image.name
            self.profile_picture = storage.save(self.ram_image.name, self.ram_image)
