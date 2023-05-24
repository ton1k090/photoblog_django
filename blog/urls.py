from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from config import settings
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.BlogView.as_view(), name='post_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)