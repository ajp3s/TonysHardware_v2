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

    ram_image = models.ImageField(
        upload_to='ram_images/'
    )

    def get_ram_type_and_frequency(self):
        return self.RAM_FREQUENCIES.get(self.ram_type, ())

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()
        if self.ram_image:
            self.ram_image.name = self.ram_image.name
            self.ram_image = storage.save(self.ram_image.name, self.ram_image)


class Cpu(models.Model):
    CPU_MANUFACTURERS_CHOICES = (
        ('Intel', "Intel"),
        ("AMD", "AMD"),
    )

    manufacturer = models.CharField(
        max_length=50,
        choices=CPU_MANUFACTURERS_CHOICES
    )

    model = models.CharField(
        max_length=50,
    )

    cores_count = models.CharField(
        max_length=150,
    )

    base_clock = models.PositiveIntegerField()

    boost_clock = models.PositiveIntegerField()

    L1_cache = models.PositiveIntegerField()

    L2_cache = models.PositiveIntegerField()

    L3_cache = models.PositiveIntegerField()

    tdp = models.PositiveIntegerField(
        verbose_name="Thermal Design Power(TDP)"
    )

    cpu_image = models.ImageField(
        upload_to='cpu_images/'
    )

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()
        if self.cpu_image:
            self.cpu_image.name = self.cpu_image.name
            self.cpu_image = storage.save(self.cpu_image.name, self.cpu_image)


class StorageDrive(models.Model):
    manufacturer_choices = (
        ('Adata', 'Adata'),
        ('Corsair', 'Corsair'),
        ('Crucial', 'Crucial'),
        ('Gigabyte Aorus', 'Gigabyte Aorus'),
        ('HP', 'HP'),
        ('Intel', 'Intel'),
        ('Kingston', 'Kingston'),
        ('Micron', 'Micron'),
        ('Pioneer', 'Pioneer'),
        ('PNY', 'PNY'),
        ('Samsung', 'Samsung'),
        ('SanDisk', 'SanDisk'),
        ('Seagate', 'Seagate'),
        ('Western Digital', 'Western Digital'),
        ('Axle', 'Axle'),
        ('BIOSTAR', 'BIOSTAR'),
        ('G.SKILL', 'G.SKILL'),
        ('Plextor', 'Plextor'),
        ('Verbatim', 'Verbatim'),
        ('Viking', 'Viking'),
    )

    types_choices = (
        ('nvme m.2 SSD', 'nvme m.2 SSD'),
        ('HDD', 'HDD'),
        ('2.5 sata SSD', '2.5 sata SSD'),
    )

    manufacturer = models.CharField(
        max_length=50,
        choices=manufacturer_choices,
    )

    type = models.CharField(
        max_length=50,
        choices=types_choices,
    )

    capacity = models.CharField(
        max_length=50,
    )

    drive_image = models.ImageField(
        upload_to='storage_drivers_images/'
    )

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()

        if self.drive_image:
            self.drive_image.name = self.drive_image.name
            self.drive_image = storage.save(self.drive_image.name, self.drive_image)


class Psu(models.Model):
    manufacturer_choices = (
        ('ABS', 'ABS'),
        ('Antec', 'Antec'),
        ('AOpen', 'AOpen'),
        ('Apevia', 'Apevia'),
        ('AXLE', 'AXLE'),
        ('Be quiet!', 'Be quiet!'),
        ('Black Box', 'Black Box'),
        ('Cooler Master', 'Cooler Master'),
        ('Coolmax','Coolmax'),
        ('Corsair','Corsair'),
        ('Curtiss-Wright','Curtiss-Wright'),
        ('Deepcool','Deepcool'),
        ('Delta Electronics', 'Delta Electronics'),
        ('Dynapower USA', 'Dynapower USA'),
        ('Eaton', 'Eaton'),
        ('Emerson Network Power', 'Emerson Network Power'),
        ('EVGA', 'EVGA'),
        ("Foxconn", 'Foxconn'),
        ("G.SKILL", 'G.SKILL'),
        ("LIAN LI", 'LIANLI'),
        ('NZXT', 'NZXT'),
        ('Phanteks', 'Phanteks'),
        ('Qualstar', 'Qualstar'),
        ('RIOTORO', 'RIOTORO'),
        ('Rosewill', 'Rosewill'),
        ('Seasonic', 'Seasonic'),
        ('SIIG', 'SIIG'),
        ('Shuttle', 'Shuttle'),
        ('Supermicro', 'Supermicro'),
        ('TDK', 'TDK'),
        ('Thermaltake', 'Thermaltake'),
        ('UMEC', 'UMEC'),
        ('Vertiv', 'Vertiv'),
        ('XFX', 'XFX'),
    )

    efficiency_standard_choices = (
        ('80 Plus', '80 Plus'),
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
        ('Titanium', 'Titanium'),
    )

    modular_choices = (
        ('Fully modular', 'Fully modular'),
        ('Semi-modular', 'Semi-modular'),
        ('Non-modular', 'Non-modular'),
    )

    manufacturer = models.CharField(
        max_length=50,
        choices=manufacturer_choices,
        null=True,

    )

    max_dc_output = models.PositiveIntegerField()

    efficiency_standard = efficiency_standard_choices

    modular = models.CharField(
        max_length=50,
        choices=modular_choices,
        null=True,
    )

    connectors = models.TextField(
        max_length=200,
        null=True,
    )

    psu_image = models.ImageField(
        upload_to='psu_images/'
    )

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()
        if self.psu_image:
            self.psu_image = self.psu_image.name
            self.psu_image = storage.save(self.psu_image.name, self.psu_image)


