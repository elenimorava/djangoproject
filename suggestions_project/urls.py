from django.urls import include, path
from rest_framework import routers
from .views import SuggestionViewSet, VoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'suggestions', SuggestionViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
