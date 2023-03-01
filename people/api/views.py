from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegionSerializer
from account.models import Region, Profile


class ListCities(APIView):
    def get(self, request):
        country_id = request.GET["country"]
        regions = [
            RegionSerializer(city).data
            for city in Region.objects.filter(country__id=country_id)
        ]
        return Response(regions)


class LikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        profile = Profile.objects.get(id=request.data["profile_id"])
        if profile.users_like.filter(id=request.user.id).exists():
            profile.likes -= 1
            profile.users_like.remove(request.user)
            profile.save()
            return Response({"is_liked": False})
        profile.likes += 1
        profile.users_like.add(request.user)
        profile.save()
        return Response({"is_liked": True})
