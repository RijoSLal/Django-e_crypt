from django.urls import path,include
from . import views
urlpatterns = [

    path("login/",views.login,name="login_page"),
    path("",views.signup,name="signin_page"),
    path("home/",views.home,name="app_page"),
    path("super/",views.admin,name="admin_page"),
    path("search/",views.search,name="searched"),
    path("edit/<pk>",views.edit,name="edit"),
    path("delete/<pk>",views.delete,name="delete"),
    path("logout/",views.log_out,name="logout_user")
    

]
