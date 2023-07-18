from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, StatisticsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )