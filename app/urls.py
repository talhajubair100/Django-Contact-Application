from django.urls import path
from . import views


urlpatterns = [
#    path('', views.home, name="home"),
    path('', views.HomePageView.as_view(), name="home"),
#    path('detail/<int:contact_id>', views.detail, name="detail"),
    path('detail/<int:pk>', views.ContactDeatilView.as_view(), name="detail"),
    path('search/', views.search, name="search"),
    path('contacts/create', views.ContactCreateView.as_view(), name="create"),
    path('contacts/update/<int:pk>', views.ContactUpdateView.as_view(), name="update"),
    path('contacts/delete/<int:pk>', views.ContactDeleteView.as_view(), name="delete"),
    path('signup/', views.SingUpView.as_view(), name="signup"),

]