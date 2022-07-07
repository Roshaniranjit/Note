from django.urls import path
from .views import form,index,create,base,update_form,update,delete

urlpatterns = [
    path('form/',form ,name='form-page'),
    path('index/' ,index ,name='index-page'),
    path('create/',create ,name='create-page'),
    path('base/<int:id>/',base ,name='base-page'),
    path('updateform/<int:id>/',update_form ,name='update_form-page'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    
    
    
    
    
]
