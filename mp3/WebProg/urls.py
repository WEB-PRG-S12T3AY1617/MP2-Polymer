from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import Profiles.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Profiles/', include('Profiles.urls')),
    url(r'^homepage/', include('homepage.urls')),
    url(r'^login/', Profiles.views.Login),
    url(r'^register/', Profiles.views.Register),
    url(r'^logout/', Profiles.views.Logout),
    url(r'^additem/', Profiles.views.SellItem.as_view(),name='sell'),
    url(r'^profilepage/', Profiles.views.profile),
    url(r'^exchange/', Profiles.views.Exchange.as_view(), name='exchange'),
    url(r'^purchase/', Profiles.views.Purchase.as_view(), name='purchase'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)