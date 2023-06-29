from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.contact, name='contact'),
    path('blog/<int:id>/', views.blog_detail,name='blog_detail'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)