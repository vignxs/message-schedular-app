from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MessageEventViewSet
from django.views.generic import TemplateView


app_name = "core"


# Create a router for API endpoints
router = DefaultRouter()
router.register(r'schedule', MessageEventViewSet, basename='message-event')

urlpatterns = [
    path('api/', include(router.urls)),
    path("", TemplateView.as_view(template_name="core/index.html"))

]
