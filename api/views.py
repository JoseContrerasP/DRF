from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
	# instance = Product.objects.all().order_by("?").first()
	# data = {}
	# if instance:
	# 	# data = model_to_dict(instance)
	# 	data = ProductSerializer(instance).data

	if request.method == "POST":
		serializer = ProductSerializer(data = request.data)

		if serializer.is_valid():
			instance = serializer.save()
			print(instance)
			return Response(serializer.data)

	else:
		instance = Product.objects.all().order_by("?").first()
		data = {}
		if instance:
			data = ProductSerializer(instance).data

			return Response(data)
