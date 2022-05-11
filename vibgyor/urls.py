from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('table/', views.table),
    # path('delete/<int:id>',views.delete),
    # path('update/<int:id>',views.update),
]