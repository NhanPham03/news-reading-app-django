from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.articles.models import Article
from apps.categories.serializers import ArticleSerializer
from apps.categories.enums import Category

@api_view(['GET'])
def articles_by_category(request, category_name):
  category_value = None
  for category in Category:
    if category.name.lower() == category_name.lower():
      category_value = category.value
      break

  if category_value is None:
    return Response({'error': 'Invalid category name'}, status=status.HTTP_400_BAD_REQUEST)
  
  articles = Article.objects.filter(category=category_value)
  serializer = ArticleSerializer(articles, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)
