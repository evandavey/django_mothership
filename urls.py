from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^mothership/', include('mothership.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^notification/', include('notification.urls')),
)

urlpatterns+=patterns('',

(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
#(r'^profiles/', include('profiles.urls')),
#url(r"^ratings/", include("agon_ratings.urls")),
)

urlpatterns+=patterns('',
#    url(r'^openbudgetapp/', include('openbudgetapp.urls'), name='openbudget'),
)

urlpatterns+=patterns('',
    url(r'^bankdownloads/', include('bankdownloads.urls'), name='bankdownloads'),
)

urlpatterns+=patterns('',
    url(r'^recipemonkeyapp/', include('recipemonkeyapp.urls'), name='recipemonkey'),
)

#urlpatterns+=patterns('',
#    url(r'^openportfolioapp/', include('openportfolioapp.urls'), name='openbudget'),
#)


#from haystack.views import SearchView, search_view_factory
#from haystack.forms import ModelSearchForm

#urlpatterns+=patterns('',
#    url(r'search/', include('haystack.urls'), name='search'),
#)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
