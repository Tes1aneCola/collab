from .models import *
from rest_framework import viewsets, generics, status
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import CarFilter



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer



class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer



class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer



class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    search_fields = ['car_name']
    ordering_fields = ['year']



class CarDetailViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer



class CarPhotosViewSet(viewsets.ModelViewSet):
    queryset = CarPhotos.objects.all()
    serializer_class = CarPhotosSerializer

