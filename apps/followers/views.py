from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.followers.serializers import UserSerializer

User = get_user_model()

class FollowerListView(APIView):
  def get(self, request, user_id):
    try:
      user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    followers = user.followers.all().select_related('follower')
    serializer = UserSerializer([f.follower for f in followers], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class FollowingListView(APIView):
  def get(self, request, user_id):
    try:
      user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    following = user.users.all().select_related('user')
    serializer = UserSerializer([f.user for f in following], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
