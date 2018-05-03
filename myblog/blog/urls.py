from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	#path('', views.PostListView.as_view(), name='post_list'),
	path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
	path('<int:year>/<int:month>/<int:day>/<post>/', views.post_detail, name='post_detail'),
	path('<int:post_id>/share/', views.post_share, name='post_share'),

]