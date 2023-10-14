from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadVisitorViewSet, AccompanyingViewSet, getAccompanyingVisitors, getLeadVisitors

router = DefaultRouter()
router.register(r'leadvisitor', LeadVisitorViewSet)
router.register(r'accompanying', AccompanyingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getAccompanyingVisitors/', getAccompanyingVisitors, name='getAccompanyingVisitors'),
    path('getLeadVisitors/', getLeadVisitors, name='getLeadVisitors')
]