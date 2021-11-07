
from django.urls import path
from .views import homePageView
from .views import send_json
from .views import savedata
urlpatterns = [
            path('', homePageView, name='home'),
            path('sendjson/', send_json, name='send_json'),
            path('savedata/', savedata, name='savedata'),
            ]
