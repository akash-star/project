from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='blog'



urlpatterns = [
     path ('', views.blog, name="blog"),
     path('contact/', views.contact, name="contact"),
     path('<int:course_id>/', views.course_detail, name="course_detail"),
     path('curr/', views.curr, name="curr"),
     path('tech/', views.tech, name="tech"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)