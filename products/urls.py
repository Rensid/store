from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='index'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
]
