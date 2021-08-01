from django.urls import include, path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tenders', views.TenderViewSet)

router.register(r'buyers', views.BuyerViewSet)

router.register(r'sellers', views.SellerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]