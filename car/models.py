from django.db import models


class Marka(models.Model):
    marka_name = models.CharField(max_length=16)


    def __str__(self):
        return self.marka_name


class Model(models.Model):
    model_name = models.CharField(max_length=12)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name = models.CharField(max_length=25)
    year = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=16)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    STATUS_CHOICES=(
        ('левый', 'Левый'),
        ('правый', 'Правый')
    )
    steering_wheel = models.CharField(choices=STATUS_CHOICES, max_length=20)

    BOX_CHOICES=(
        ('автомат', 'Автомат'),
        ('механика', 'Механика')
    )
    box = models.CharField(choices=BOX_CHOICES, max_length=10)
    CONDITION_CHOICES=(
        ('новый', 'Новый'),
        ('б/у', 'Б/У')
    )
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=10)
    volume= models.FloatField()
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    have = models.BooleanField(default=True)

    def __str__(self):
        return self.car_name
