from django.contrib import admin
from django.urls import path
from AI import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('GC',views.GC,name='GC'),
    path('emoji',views.emoji,name='emoji'),
    path('quest',views.quest,name='quest'),
    path('quote',views.quote,name='quote'),
]
