from django.urls import path

from . import views

urlpatterns = [
	path("", views.ProductListCreateAPIView.as_view()),
	path("<int:pk>/", views.ProductMixinView.as_view()),
	path("update/<int:pk>", views.ProductUpdateAPIView.as_view()),
	path("delete/<int:pk>", views.ProductDestroyAPIView.as_view()),
]

# update my cv

# take down cities blog