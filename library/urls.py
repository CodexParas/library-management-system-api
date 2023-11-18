from django.urls import path, include
from library.views import BookViewset, UserViewset
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'book',BookViewset)
router.register(r'user',UserViewset)

urlpatterns = [
    path('',include(router.urls))
]