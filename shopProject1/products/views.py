from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .reliaslizers import ProductSerializer, \
    ProductValidateSerializer, CategorySerializer, TagSerializer
from .models import Product, Category, Tag
from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class TagModelViewSet(ModelViewSet):  # list, create, retrieve, update, destroy
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
    pagination_class = PageNumberPagination


class CategoryListAPIView(ListCreateAPIView):  # list, create
    pagination_class = PageNumberPagination  # pagination
    queryset = Category.objects.all()  # list of data from DB
    serializer_class = CategorySerializer  # class of serializer inherited by model serializer


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):  # retreive, update, destroy
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        # Step 1. Get data from request Body
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        is_hit = request.data.get('is_hit')
        category_id = request.data.get('category_id')
        tags = request.data.get('tags')

        # Step 2. Create Product
        product = Product.objects.create(
            title=title, description=description, price=price, is_hit=is_hit,
            category_id=category_id
        )
        product.tags.set(tags)
        product.save()

        # Step 3. Return response with created product
        return Response(data={'product': ProductSerializer(product).data})


@api_view(['GET', 'PUT', 'DELETE'])
def product_item_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.is_hit = request.data.get('is_hit')
        product.category_id = request.data.get('category_id')
        product.tags.set(request.data.get('tags'))
        product.save()
        return Response(data={'product': ProductSerializer(product).data})
    else:
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        'text': 'Hello World!',
        'int': 1000,
        'bool': True,
        "float": 2.99,
        'list': [1, 2, "asdfasd"],
        "dict": {
            "text": "hello"
        }
    }
    return Response(data=dict_)