from rest_framework.views import APIView
from rest_framework.response import Response
from userprofile.models import UserProfile
from userprofile.serializers import ProfileSerializer


class ProfileList(APIView):
    def get(self, request):
        profilequery = UserProfile.objects.all()
        serializer = ProfileSerializer(profilequery, many=True)
        return Response(serializer.data)
