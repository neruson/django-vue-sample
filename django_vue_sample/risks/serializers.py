from rest_framework.serializers import ModelSerializer

from .models import RiskType, CustomField, CustomFieldOption


class CustomFieldOptionSerializer(ModelSerializer):
    class Meta:
        model = CustomFieldOption
        fields = ("value",)


class CustomFieldSerializer(ModelSerializer):
    options = CustomFieldOptionSerializer(many=True, read_only=True)

    class Meta:
        model = CustomField
        fields = ("id", "name", "field_type", "options")


class RiskTypeSerializer(ModelSerializer):
    fields = CustomFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = ("id", "name", "fields")
