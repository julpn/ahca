from rep_api.models import Rep
from rest_framework import serializers
from rest_framework.permissions import AllowAny


class RepSerializer(serializers.ModelSerializer):
    permission_classes = (AllowAny,)
    class Meta:
        model = Rep
        fields = ('state', 'district', 'killed', 'debt', 'uninsured', 'name')