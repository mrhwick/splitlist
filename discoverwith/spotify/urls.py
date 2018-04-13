from django.urls import path

from . import views

urlpatterns = [
	path('register/', views.go_to_spotify_for_auth),
	path('receive-redirect/', views.receive_redirect),
]