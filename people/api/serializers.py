from rest_framework.serializers import ModelSerializer
from account.models import Region


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ("title", "id")
