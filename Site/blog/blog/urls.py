
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post import views
from contact.views import contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('blog/', views.blog, name='blog_list'),
    path('post/<id>/', views.post, name= 'blog_details'),
    path('post/<id>/update/', views.post_update, name= 'post_update'),
    path('post/<id>/delete/', views.post_delete, name= 'post_delete'),
    path('create/', views.post_create, name= 'post_create'),
    path('search/', views.search, name= 'search'),
    path('tinymce/', include('tinymce.urls'), name= 'tinymce'),
    path('accounts/', include('allauth.urls')),
    path('contact/', include('contact.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)