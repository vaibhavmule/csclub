from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('job/', include('jobboard.urls')),
    path('blog/', include('blog.urls')),
]
