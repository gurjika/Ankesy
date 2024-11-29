from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ankesy_api.models import Report, ScamType
from ankesy_api.serializers import ReportSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
# Create your views here.


class ScamTypeView(APIView):
    def get(self, request, *args, **kwargs):
        scam_types = [{'key': choice.value, "label": choice.label} for choice in ScamType]
        return Response(scam_types)
    


class ReportViewSet(CreateModelMixin, GenericViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer



class ListReportViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(parent_email=self.request.user.email)
    