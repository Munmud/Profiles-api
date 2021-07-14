from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')

# because of model don't need base_name
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)), 
]
