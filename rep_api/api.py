from rest_framework.generics import (
    ListAPIView
)
from rep_api.serializers import RepSerializer
from rep_api.models import Rep
from django.http import JsonResponse
from django.http import Http404

class RepApi(ListAPIView):
    serializer_class = RepSerializer

    def get(self, request):
        rep_name = request.query_params.get('rep')
        try:
            rep = Rep.objects.get(last_name__iexact=rep_name)
        except Rep.DoesNotExist:
            raise Http404
        serializer = RepSerializer(rep)
        return JsonResponse(serializer.data, safe=False)