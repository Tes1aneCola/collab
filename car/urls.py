from django.urls import path
from .views import *



urlpatterns = [

    path('', CarListViewSet.as_view({'get':'list'}), name = 'car_list'),
    path('<int:pk>/', CarDetailViewSet.as_view({'get':'retrieve'}), name = 'car_detail'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users'),
    path('marka/', MarkaViewSet.as_view({'get':'list'}), name = 'marka'),
    path('models/', ModelViewSet.as_view({'get':'list'}), name ='models'),
    path('photos/', CarPhotosViewSet.as_view({'get':'list'}), name = 'car_photos')
]
