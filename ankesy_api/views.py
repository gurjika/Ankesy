from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ankesy_api.models import Report, ScamType
from ankesy_api.serializers import ReportSerializer
# Create your views here.


class ScamTypeView(APIView):
    def get(self, request, *args, **kwargs):
        scam_types = [{'key': choice.value, "label": choice.label} for choice in ScamType]
        return Response(scam_types)
    


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    