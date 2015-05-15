from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    
    # import blog.urls into the main url ('')
    url(r'^blog/', include('blog.urls')),
]
