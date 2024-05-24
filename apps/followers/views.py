from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.followers.models import Follower
from apps.followers.serializers import FollowerSerializer, UserSerializer

User = get_user_model()

@api_view(['GET'])
def followers_list(request):
  user_id = request.GET.get('user_id')
  if not user_id:
    return Response({'error': 'user_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

  try:
    user = User.objects.get(pk=user_id)
  except User.DoesNotExist:
    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
  
  followers = Follower.objects.filter(user=user).select_related('follower')
  serializer = FollowerSerializer(followers, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def following_list(request):
  user_id = request.GET.get('user_id')
  if not user_id:
    return Response({'error': 'user_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

  try:
    user = User.objects.get(pk=user_id)
  except User.DoesNotExist:
    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
  
  following = Follower.objects.filter(follower=user).select_related('user')
  serializer = UserSerializer([relation.user for relation in following], many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)
