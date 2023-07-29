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
        verbose_name="Thermal Design Power(TDP)",

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


class NvidiaGPU(models.Model):
    GENERATIONS_CHOICES = (
        ('GeForce GTX9XX', ' GeForce GTX9XX'),
        ('GeForce GTX10XX', 'GeForce GTX10XX'),
        ('GeForce GTX16XX', 'GeForce GTX16XX'),
        ('GeForce RTX20XX', 'GeForce RTX20XX'),
        ('GeForce RTX30XX', 'GeForce RTX30XX'),
        ('GeForce RTX40XX', 'GeForce RTX40XX'),
    )

    series = models.CharField(
        max_length=30,
    )

    model = models.CharField(
        max_length=100,
    )

    graphics_processor = models.CharField(
        max_length=20,
    )

    architecture = models.CharField(
        max_length=20,

    )

    process_size = models.CharField(
        max_length=5,
    )

    transistors = models.CharField(
        max_length=30,
    )

    base_clock = models.PositiveIntegerField()

    boost_clock = models.PositiveIntegerField()

    memory_clock = models.PositiveIntegerField()

    memory_bus_width = models.PositiveIntegerField()

    bandwidth = models.PositiveIntegerField()

    release_date = models.DateField(
        auto_now=True,
    )

    tdp = models.PositiveIntegerField(
        verbose_name="Thermal Design Power(TDP)"

    )
    suggested_psu = models.CharField(
        max_length=10,
    )

    graphics_api_support = models.CharField(
        max_length=60,
    )

    nvidia_gpu_image = models.ImageField(
        upload_to='nvidia_gpu_images/'
    )

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()
        if self.nvidia_gpu_image:
            self.nvidia_gpu_image = self.nvidia_gpu_image.name
            self.nvidia_gpu_image = storage.save(self.nvidia_gpu_image.name, self.nvidia_gpu_image)