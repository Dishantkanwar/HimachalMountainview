from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from .views import*
from django.conf.urls.static import static
urlpatterns=[
    path('',hom),
    path('about',about),
    path('tracking',tracking),
    path('hp',hp),
    path('jk',jk),
    path('uk',uk),
    path('contact',contact),
    path('booking',bookingg),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)