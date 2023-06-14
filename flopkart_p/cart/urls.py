from django.urls import path
from . import views
app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('minus/<int:product_id>/', views.minus_cart, name='minus_cart'),
    path('delete/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
]
