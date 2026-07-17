from django.urls import path
from . import views

urlpatterns = [
    # Customers
    path('customers/add/', views.customer_add),
    path('customers/', views.customer_list),
    path('customers/update/<int:id>/', views.customer_update),
    path('customers/delete/<int:id>/', views.customer_delete),
    
    # Restaurants
    path('restaurants/add/', views.restaurant_add),
    path('restaurants/', views.restaurant_list),
    path('restaurants/update/<int:id>/', views.restaurant_update),
    path('restaurants/delete/<int:id>/', views.restaurant_delete),
    
    # Foods
    path('foods/add/', views.food_add),
    path('foods/', views.food_list),
    path('foods/update/<int:id>/', views.food_update),
    path('foods/delete/<int:id>/', views.food_delete),
    
    # Cart
    path('cart/add/', views.cart_add),
    path('cart/', views.cart_list),
    path('cart/update/<int:id>/', views.cart_update),
    path('cart/delete/<int:id>/', views.cart_delete),
    
    # Orders
    path('orders/add/', views.order_add),
    path('orders/', views.order_list),
    path('orders/update/<int:id>/', views.order_update),
    path('orders/delete/<int:id>/', views.order_delete),
]
