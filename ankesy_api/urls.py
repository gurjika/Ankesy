from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(prefix='reports', viewset=views.ReportViewSet, basename='report')

urlpatterns = [
    path('scam-types/', view=views.ScamTypeView.as_view(), name='scam-types')
]

urlpatterns += router.urls