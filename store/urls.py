from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.store, name='index' ),
    path('aboutMe/', views.aboutMe, name='aboutMe' ),
    path('experience/', views.experience, name='experience' ),
    path('writeMeAMessage/', views.writeMeAMessage, name='writeMeAMessage' )
]