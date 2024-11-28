from rest_framework import serializers

from ankesy_api.models import Report



class ScamTypeSerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    label = serializers.CharField()


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'