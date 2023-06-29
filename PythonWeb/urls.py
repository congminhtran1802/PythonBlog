from django.contrib import admin
from django.urls import path,include
from theme.views import change_theme
urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch_theme/', change_theme,name='change_theme'),
    path('', include('home.urls')),
    path('blogadmin', include('blog.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]