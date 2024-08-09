from django.urls import path
from . views import productclassview

urlpatterns = [
    path('product', productclassview.as_view()),
    path('product/<int:pk>', productclassview.as_view()),

]