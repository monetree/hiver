
from django.contrib import admin
from django.urls import path
from scrap.views import get_hiver_data_as_api, get_hiver_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', get_hiver_data_as_api),
    path('', get_hiver_data),
]
