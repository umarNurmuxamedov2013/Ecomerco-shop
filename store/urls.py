from django.urls import path
from .views import index, add_product, category_products, user_login, log_out, register, detail_view

urlpatterns = [
    path("", index, name="store"),
    path("add/", add_product, name="add_product"),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('login/', user_login, name='login'),
    path('log_out/', log_out, name='log_out'),
    path('register/', register, name='register'),
    path('detail_view/<int:id>', detail_view, name="detail_view"),
]
