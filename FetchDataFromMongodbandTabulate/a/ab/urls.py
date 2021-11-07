
from django.urls import path
#from .views import homePageView
#from .views import send_json
#from .views import savedata
#from .views import showdata



from . import views


from .sumeerdata import *
urlpatterns = [
            path('', views.homePageView, name='home'),
            path('sendjson/', views.send_json, name='send_json'),
            path('savedata/', views.savedata, name='savedata'),
            path('showdata/', views.showdata, name='showdata'),
            path('devstatus/', views.devicestatus, name='devstatus'),
            path('index/',views.index, name='index'),
            ]
