from django.contrib import admin
from django.urls import path, include, re_path, register_converter
from women import views
from women.views import page_not_found

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
    path('cats/<int:cat_id>', views.categories, name='cat_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    re_path(r'archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),
]


handler404 = page_not_found