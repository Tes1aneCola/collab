from .models import *
from rest_framework import  serializers



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id', 'first_name', 'last_name', 'phone_number']


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ['marka_name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Car
        fields = ['car_name', 'user', 'price', 'year', 'box','date']


class CarDetailSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    model = ModelSerializer()
    date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Car
        fields = ['car_name', 'user','year', 'description', 'price', 'color',  'model', 'steering_wheel',
                  'box', 'condition', 'volume', 'date', 'have']


class CarPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = '__all__'


