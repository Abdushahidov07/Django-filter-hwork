from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("showvakansi/", ShowVakansi.as_view(), name="showvakansi"),
    path("createvakansi/", CreateVakansi.as_view(), name="createvakansi"),
    path("detailvakansi/<int:pk>", DetailVakansi.as_view(), name="detailvakansi"),
    path("deletevakansi/<int:pk>", DeleteVakansi.as_view(), name="deletevakansi"),
    path("updatevakansi/<int:pk>", UpdateVakansi.as_view(), name="updatevakansi"),
    path("showcotegory/", ShowCotegory.as_view(), name="showcotegory"),
    path("createcotegory/", CreateCotegory.as_view(), name="createcotegory"),
    path("detailcotegory/<int:pk>", DetailCotegory.as_view(), name="detailcotegory"),
    path("deletecotegory/<int:pk>", DeleteCotegory.as_view(), name="deletecotegory"),
    path("updatecotegory/<int:pk>", UpdateCotegory.as_view(), name="updatecotegory"),
    path("showapplication/", ShowApplication.as_view(), name="showapplication"),
    path("createapplication/", CreateApplication.as_view(), name="createapplication"),
    path("detailapplication/<int:pk>", DetailApplication.as_view(), name="detailapplication"),
    path("deleteapplication/<int:pk>", DeleteApplication.as_view(), name="deleteapplication"),
    path("updateapplication/<int:pk>", UpdateApplication.as_view(), name="updateapplication"),
]
