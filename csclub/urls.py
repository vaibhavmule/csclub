from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from blog.views import post_detail, post_by_user, BlogSitemap
from jobboard.views import jobs_by_employer, companies, JobSitemap
from page.views import signup, handler404

sitemaps = {
    'blog': BlogSitemap,
    'job': JobSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/singup/', signup, name='signup'),
    path('', include('page.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('job/', include('jobboard.urls')),
    path('blog/', include('blog.urls')),
    path('companies/', companies, name='companies'),
    path('companies/<slug:slug>/', jobs_by_employer, name='jobs_by_employer'),
    path('@<username>/<slug:slug>/', post_detail, name='post_detail'),
    path('@<username>/', post_by_user, name='post_by_user'),
]

handler404 = 'page.views.handler404'
