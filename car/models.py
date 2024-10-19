from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(max_length=13)
    last_name = models.CharField(max_length=33)
    phone_number = PhoneNumberField(region='KG')

    def __str__(self):
        return self.first_name



class Marka(models.Model):
    marka_name = models.CharField(max_length=16)


    def __str__(self):
        return self.marka_name


class Model(models.Model):
    model_name = models.CharField(max_length=22)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

class CarPhotos(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
