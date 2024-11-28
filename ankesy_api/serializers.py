from datetime import datetime, timezone
from rest_framework import serializers

from ankesy_api.models import Report
from .tasks import send_email_to_parent





class ScamTypeSerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    label = serializers.CharField()


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

    

    def create(self, validated_data):
        email = validated_data['parent_email']
        flagged_data = {key: "Yes" for key, value in validated_data.items() if value is True}

        obj = Report.objects.create(**validated_data)        
        send_email_to_parent.apply_async((flagged_data, email, obj.get_type_display()))
        return obj