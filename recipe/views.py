from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Tag, Ingredient
from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, 
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    serializer_class=serializers.TagSerializer
    queryset=Tag.objects.all()


class IngredientViewSet(BaseRecipeAttrViewSet):
    serializer_class=serializers.IngredientSerializer
    queryset=Ingredient.objects.all()