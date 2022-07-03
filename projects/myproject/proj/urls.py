from django.urls import path
from . import views
from .views import render_pdf_view,CustomerListView,customer_render_pdf_view








app_name='proj'

urlpatterns=[
    path('',CustomerListView.as_view(), name='customer-list-view'),
    path('test/',render_pdf_view, name='test-view'),
    path('pdf/<pk>',customer_render_pdf_view, name='customer-pdf-view'),
    path ("counter", views.counter, name = "counter"),
    path('register',views.register, name="register"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path("",views.sidebar, name="sidebar"),
   
    
    
]