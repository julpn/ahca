from django.http import JsonResponse
from django.http import Http404
from django.db.models.functions import Concat
from django.db.models import Q
from rest_framework.generics import ListAPIView

from random import randint

from rep_api.serializers import RepSerializer
from rep_api.models import Rep

class RepApi(ListAPIView):
    serializer_class = RepSerializer

    def get(self, request):
        rep_name = request.query_params.get('rep')
        try:
            queryset = Rep.objects.annotate(search_name=Concat('first_name', 'last_name'))
            rep = queryset.filter(Q(last_name__iexact=rep_name) | Q(search_name__iexact=rep_name))[0]
        except IndexError:
            raise Http404
        serializer = RepSerializer(rep)
        return JsonResponse(serializer.data, safe=False)


class RandomRepApi(ListAPIView):
    serializer_class = RepSerializer

    def get(self, request):
        all_reps = Rep.objects.all()
        count = all_reps.count()
        random_index = randint(0, count - 1)
        rep = all_reps[random_index]
        serializer = RepSerializer(rep)
        return JsonResponse(serializer.data, safe=False)
