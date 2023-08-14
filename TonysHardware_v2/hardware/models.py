from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from TonysHardware_v2.functionality.mixins import S3ImageSaveMixin

storage = S3Boto3Storage()

DDR_RAM_TYPES_CHOICES = (
    ("DDR2", "DDR2"),
    ("DDR3", "DDR3"),
    ("DDR4", "DDR4"),
    ("DDR5", "DDR5"),
)


class RAMMemoryModel(S3ImageSaveMixin, models.Model):
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

    brand = models.CharField(
        max_length=50,
        choices=MANUFACTURER_CHOICES,
    )

    model = models.CharField(
        max_length=20,
    )

    capacity = models.PositiveIntegerField(

    )

    ram_type = models.CharField(
        max_length=10,
        choices=DDR_RAM_TYPES_CHOICES,
    )

    ram_frequency = models.CharField(
        max_length=100,
    )

    release_price = models.CharField(
        max_length=4,
        default=0,

    )

    image = models.ImageField(
        upload_to='ram_images/'
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.ram_type} {self.capacity}GB {self.ram_frequency}Mhz"


class CpuModel(S3ImageSaveMixin, models.Model):

    CPU_MANUFACTURERS_CHOICES = (
        ('Intel', "Intel"),
        ("AMD", "AMD"),
    )

    manufacturer = models.CharField(
        max_length=50,
        choices=CPU_MANUFACTURERS_CHOICES,

    )

    model = models.CharField(
        max_length=100,
    )

    cores_count = models.CharField(
        max_length=5,
    )

    base_clock = models.PositiveIntegerField()

    boost_clock = models.PositiveIntegerField()

    L1_cache = models.PositiveIntegerField()

    L2_cache = models.PositiveIntegerField()

    L3_cache = models.PositiveIntegerField()

    tdp = models.PositiveIntegerField(
        verbose_name="Thermal Design Power(TDP)",

    )

    release_price = models.CharField(
        max_length=6,
    )

    image = models.ImageField(
        upload_to='cpu_images/',
    )

    def __str__(self):
        return f'{self.manufacturer} {self.model} {self.cores_count}'


class StorageDriveModel(S3ImageSaveMixin, models.Model):
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

    release_price = models.CharField(
        max_length=6,
    )

    image = models.ImageField(
        upload_to='storage_drivers_images/'
    )

    def __str__(self):
        return f"{self.image} {self.type} {self.capacity}"


class PsuModel(S3ImageSaveMixin, models.Model):
    manufacturer_choices = (
        ('ABS', 'ABS'),
        ('MSI', 'MSI'),
        ('Antec', 'Antec'),
        ('AOpen', 'AOpen'),
        ('Apevia', 'Apevia'),
        ('AXLE', 'AXLE'),
        ('Be quiet!', 'Be quiet!'),
        ('Black Box', 'Black Box'),
        ('Cooler Master', 'Cooler Master'),
        ('Coolmax', 'Coolmax'),
        ('Corsair', 'Corsair'),
        ('Curtiss-Wright', 'Curtiss-Wright'),
        ('Deepcool', 'Deepcool'),
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

    efficiency_standard = models.CharField(
        max_length=50,
        choices=efficiency_standard_choices,
    )

    modular = models.CharField(
        max_length=50,
        choices=modular_choices,
        null=True,
    )

    connectors = models.CharField(
        max_length=200,
        null=True,
    )

    release_price = models.CharField(
        max_length=6,
        default=0,

    )

    image = models.ImageField(
        upload_to='psu_images/'
    )

    def __str__(self):
        return f"{self.manufacturer} {self.max_dc_output} {self.efficiency_standard} {self.modular}"


class NvidiaGPUModel(S3ImageSaveMixin, models.Model):
    TYPES_CHOICES = (
        ('Desktop', 'Desktop'),
        ('Laptop', 'Laptop'),
    )

    type = models.CharField(
        max_length=20,
        choices=TYPES_CHOICES
    )

    model = models.CharField(
        max_length=100,
    )

    ram_size = models.CharField(
        max_length=5,
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

    transistors_count = models.CharField(
        max_length=30,
    )

    base_clock = models.PositiveIntegerField()

    boost_clock = models.PositiveIntegerField()

    memory_bus_width = models.PositiveIntegerField()

    release_date = models.DateField()

    release_price = models.CharField(
        max_length=6,
        default=0,
    )

    tdp = models.PositiveIntegerField(
        verbose_name="Thermal Design Power(TDP)"

    )
    suggested_psu = models.CharField(
        max_length=5,
    )

    graphics_api_support = models.CharField(
        max_length=25,
    )

    image = models.ImageField(
        upload_to='nvidia_gpu_images/'
    )

    maximum_gpu_temperature = models.CharField(
        max_length=3,
        null=True
    )

    def __str__(self):
        return f'Nvidia {self.model} / {self.ram_size} ({self.type if self.type == "Laptop" else ""}'


class AMDRadeonGPUModel(S3ImageSaveMixin, models.Model):
    TYPES_CHOICES = (
        ('Desktop', 'Desktop'),
        ('Laptop', 'Laptop'),
        ('Integrated(iGPU)', 'Integrated(iGPU)'),
    )

    type = models.CharField(
        max_length=20,
        choices=TYPES_CHOICES,
    )

    model = models.CharField(
        max_length=100,
    )

    ram_size = models.CharField(
        max_length=50,
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

    transistors_count = models.CharField(
        max_length=30,
    )

    base_clock = models.PositiveIntegerField()

    boost_clock = models.PositiveIntegerField()

    memory_clock = models.PositiveIntegerField()

    memory_bus_width = models.PositiveIntegerField()

    memory_bandwidth = models.PositiveIntegerField()

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

    image = models.ImageField(
        upload_to='nvidia_gpu_images/'
    )

    maximum_gpu_temperature = models.CharField(
        max_length=5,
        null=True
    )

    price = models.CharField(
        max_length=6,
        default=0,
    )

    def __str__(self):
        return f'AMDRadeon {self.model} / {self.ram_size} ({self.type if self.type == "Laptop" else ""})'


class MotherBoardModel(S3ImageSaveMixin, models.Model):
    model = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    chipset = models.CharField(
        max_length=10,
    )

    socket = models.CharField(
        max_length=10,
    )

    supported_cpus = models.ManyToManyField(CpuModel)

    ram_type = models.CharField(
        max_length=10,
        choices=DDR_RAM_TYPES_CHOICES
    )

    ram_slots_count = models.IntegerField()

    ram_max_capacity = models.IntegerField()

    ram_max_frequency = models.IntegerField()

    PCIe_gen_support = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    slots_and_connectors = models.TextField(
        max_length=350,
        null=False,
        blank=False,
    )

    IO_connectors = models.TextField(
        max_length=350,
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='motherboard_images/',
    )

    price = models.CharField(
        max_length=5,
        default=0,
    )

#
# class IntelGPUModel(models.Model):
#     # TODO
#     pass
#
#
# class NvmeSSDModel(models.Model):
#     # TODO
#     pass
#
#
# class SataSSDModel(models.Model):
#     # TODO
#     pass
#
#
# class HDDModel(models.Model):
#     # TODO
#     pass
