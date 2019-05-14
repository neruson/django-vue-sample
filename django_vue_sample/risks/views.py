from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RiskType
from .serializers import RiskTypeSerializer


class RiskTypeListView(APIView):
    def get(self, request):
        risk_types = RiskType.objects.prefetch_related("fields", "fields__options")
        serializer = RiskTypeSerializer(risk_types, many=True)
        return Response(serializer.data)


class RiskTypeDetailView(APIView):
    def get_object(self, pk):
        try:
            return RiskType.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data)
