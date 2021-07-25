from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("userlogin/", views.handlelogin, name="Login In"),
    path("logout/", views.handlelogout, name="Log out"),
    path("basicdetails/", views.basicdetails, name="basicetails"),
    path("viewbasicdetails/", views.viewbasicdetails, name="viewbasicdetails"),
    path("education/", views.education, name="education"),
    path("vieweducationdetails/", views.vieweducationdetails, name="vieweducationdetails"),
    path("editdata/<str:id>/", views.editdata, name="editdata"),
    path("editbasicdata/<str:id>/", views.editbasicdata, name="editbasicdata"),
    path("deletedata/", views.deletedata, name="deletedata"),
    path("deleteviewdata/", views.deleteviewdata, name="deleteviewdata"),

]