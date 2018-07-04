from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# API endpoints.
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_views(), name='snippet-highlight'),
])

# Login and logout views for the browsable API.
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'), namespace='rest_framework')
]
