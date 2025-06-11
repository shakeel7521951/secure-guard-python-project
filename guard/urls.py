from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('',views.base,name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('guards/', views.guard_list, name="guards"),
    path('contact/', views.contact, name='contact'),
    path('book-now/',views.book_service,name="book_now"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout,name='logout'),
    path('myProfile/',views.myProfile,name="myProfile"),
    path('contact/', views.contact_view, name='contact'),
    path('', include('social_django.urls', namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
