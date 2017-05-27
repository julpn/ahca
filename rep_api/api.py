from rest_framework.generics import (
    ListAPIView
)
from rep_api.serializers import RepSerializer
from rep_api.models import Rep
from django.http import HttpResponse, JsonResponse

class RepApi(ListAPIView):
    serializer_class = RepSerializer

    def get(self, request):
        rep_name = request.query_params.get('rep')
        rep = Rep.objects.get(name=rep_name)
        serializer = RepSerializer(rep)
        return JsonResponse(serializer.data, safe=False)