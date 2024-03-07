from django.urls import path
from . import views
urlpatterns = [
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("ttmhome",views.ttmhome,name="ttmhome"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkchangepassword,name="changepassword"),
    path("logout",views.logout,name="logout")

]