# from django.contrib import admin
from django.urls import path
from employee_app import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('create',views.create),
    path('emp_details/<eid>',views.emp_details),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit)

]
