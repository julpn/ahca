from rep_api.models import Rep
from rest_framework import serializers


class RepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = ('state', 'district', 'killed', 'debt', 'uninsured', 'name')