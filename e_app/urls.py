from django.urls import path

from . import views

app_name='e_app'
urlpatterns=[
    path('',views.all_products,name="all_products"),
    path('<slug:slug>',views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/',views.category, name='category_list'),

]