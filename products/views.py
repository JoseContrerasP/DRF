from rest_framework import authentication, generics, mixins, permissions


from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

# class ProductCreateAPIView(generics.CreateAPIView):
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer

	# def perform_create(self, serializer):
	# 	serializer.save()

class ProductDetailAPIView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
	# permission_classes = []

	def perform_create(self, serializer):
		title = serializer.validated_data.get("title")
		content = serializer.validated_data.get("content") or None

		if content is None:
			content = "puedo ver tu sombra en la luna"

		serializer.save(content=content) # que interesante tengo que pasarle el nuevo content

class ProductUpdateAPIView(generics.UpdateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_update(self, serializer):
		instance = serializer.save()
		if not instance.content:
			instance.content = instance.title

			instance.save()

class ProductDestroyAPIView(generics.DestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	# def perform_destroy(self, instance):

class ProductMixinView(
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	mixins.CreateModelMixin,
	generics.GenericAPIView
	):

	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_field = "pk"

	def get(self, request, *args, **kwargs):
		pk = kwargs.get("pk")
		# print(pk)
		if pk:
			return self.retrieve(request, *args, **kwargs)

		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
		