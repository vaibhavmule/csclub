from django.contrib import admin
from django.urls import include, path

from blog.views import post_detail, post_by_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('job/', include('jobboard.urls')),
    path('blog/', include('blog.urls')),
    path('<username>/<slug:slug>/', post_detail, name='post_detail'),
    path('<username>/', post_by_user, name='post_by_user'),
]
