from django.urls import path
from . import views
app_name='todoapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.clistview.as_view(),name='cbvhome'),
    path('cbdetails/<int:pk>/',views.cdetailview.as_view(),name='cbdetails'),
    path('cbupdate/<int:pk>/',views.cupdateview.as_view(),name='cbupdate'),
    path('cbdelete/<int:pk>/',views.cdeleteview.as_view(),name='cbdelete')
]
