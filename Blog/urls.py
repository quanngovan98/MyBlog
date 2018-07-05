from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.list, name='list'),# mặc định sẽ show hết post ra
    path('contact.html/', views.contact, name='contact'),#đặt mấy trang này ở trên là để ưu tiên
    path('about.html/', views.about, name='about'),
    path('archive.html/', views.archive, name='archive'),
    path('<categorypost>/', views.postcategory, name='postcategory'),#tìm post theo category
    path('<category>/<slugifytitle>/', views.postid, name='postid'),#tìm post theo slugifytitle
]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)