from tutorials import views
from django.urls import path
 
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
    path('api/tutorials/<int:pk>', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published)
]