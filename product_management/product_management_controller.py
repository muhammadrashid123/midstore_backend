"""
Controller class for products management

"""


import uuid

from django.http import request
from product_management.models import Category
from product_management.serializers import CategoryReadSerializer, CategoryWriteSerializer, CategoryProductsReadSerializer
from rest_framework import serializers
from utils.response_utils import create_message, create_response
from utils.request_utils import get_query_param_or_default
from django.db import transaction
from product_management.serializers import (ProductsWriteSerializer,ProductsReadSerializer)
from product_management.models import Products

import logging
import traceback

class CategoryController:
    """Controller class for products category management"""

    def add_category(slef,request):
        """create an category """

        try:
            # Get mutable copy of request.data
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "title"

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=CategoryWriteSerializer(data=payload)
            if serialized.is_valid():
                category=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized = CategoryReadSerializer(category)

            return create_response(create_message([serialized.data],313), 201)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)



    def get_category(self, request):
        """Fetch all products category details """

        try:
            payload=request.data.copy()
            # if get single product
            if  get_query_param_or_default(request,"uuid",None):
                category=Category.objects.filter(uuid=get_query_param_or_default(request,"uuid",None)).first()

                if not category:
                    return create_response(create_message([], 314), 404)

                category_serialized = CategoryReadSerializer(category)
                product_obj =  Products.objects.filter(category=get_query_param_or_default(request, 'uuid', None)).all()
                
                serialized = CategoryProductsReadSerializer(product_obj, many=True)

                data = {
                'uuid': category_serialized.data['uuid'],
                'title': category_serialized.data['title'],
                'image': category_serialized.data['image'],
                'created_at': category_serialized.data['created_at'],
                'updated_at': category_serialized.data['updated_at'],
                'parent_category_uuid': category_serialized.data['parent_category_uuid'],
                'products_list': serialized.data
             }

                return create_response(create_message(data, 1000), 200)
            else:
                # if show all  product categories
                category =Category.objects.all().order_by("created_at")

                if not category:
                     return create_response(create_message([], 314), 404)

                serialized = CategoryReadSerializer(category,many=True)

                return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)



    def update_category(self,request):
        """Update product category information"""
        try:
            # Get mutable copy of request payload
            payload=request.data.copy()
            # contact_number is mandatory in query params
            if not get_query_param_or_default(request, "uuid", None):
                return create_response(create_message([], 105), 400)
                
            category=Category.objects.filter(uuid=get_query_param_or_default(request, "uuid",None)).first()
            # If category does not exist
            if not category:
                return create_response(create_message([],314),404)
            # uuid cannot be updated
            payload.pop("uuid",None)


            serialized = CategoryWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(category, serialized.validated_data)
                    read_serialized = CategoryReadSerializer(category)

            return create_response(create_message(read_serialized.data, 315), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)],1002),500)



    def delete_category(self, request):
        """Delete product category by id"""

        try:

            # uuid is mandatory in query params
            if not get_query_param_or_default(request, "uuid", None):
                return create_response(create_message([], 316), 400)

            category = Category.objects.filter(
                uuid=get_query_param_or_default(request, "uuid", None)
            ).first()

            # If product category does not exist
            if not category:
                return create_response(create_message([], 314), 404)

            category.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)

class ProductsController:
    """Controller class for products management"""

    def create_product(self, request):
        """Create an product"""

        try:
            # Get mutable copy of request.data
            payload = request.data.copy()
            # Mandatory keys in the request payload
            mandatory_keys = [
                "title",
                "image",
                "price",

            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)


            serialized=ProductsWriteSerializer(data=payload)
            if serialized.is_valid():
                product=serialized.save()

            # There were errors while serializing the payload
            else:
                return create_response(create_message([serialized.errors],102),400)


            serialized = ProductsReadSerializer(product)

            return create_response(create_message([serialized.data],310), 201)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)



    def get_products(self, request):
        """Fetch all products details"""

        try:


            payload=request.data.copy()

            # if get single product
            if  get_query_param_or_default(request,"uuid",None):

                product=Products.objects.filter(uuid=get_query_param_or_default(request,"uuid",None)).first()

                if not product:
                    return create_response(create_message([], 311), 404) #product not found

                serialized = ProductsReadSerializer(product)

                return create_response(create_message([serialized.data], 1000), 200)
            else: # all products
                products =Products.objects.all().order_by("created_at")


            if not products:
                return create_response(create_message([], 311), 404)

            serialized = ProductsReadSerializer(products,many=True)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)


    def update_product(self,request):
        """Update product information"""

        try:

            # Get mutable copy of request payload
            payload=request.data.copy()

            # uuid is mandatory in form data
            if not get_query_param_or_default(request, "uuid",None):
                return create_response(create_message([], 317),400)

            product=Products.objects.filter(uuid=get_query_param_or_default(request,"uuid",None)).first()
            # If uuid does not exist
            if not product:
                return create_response(create_message([],311),404)
            # guid cannot be updated
            payload.pop("uuid",None)


            serialized = ProductsWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():

                with transaction.atomic():
                    serialized.update(product, serialized.validated_data)
                    read_serialized = ProductsReadSerializer(product)

            return create_response(create_message(read_serialized.data, 312), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)],1002),500)



    def delete_product(self, request):
        """Delete product by id"""

        try:

            # uuid is mandatory in query params
            if not get_query_param_or_default(request, "uuid", None):
                return create_response(create_message([], 317), 400)

            product = Products.objects.filter(
                uuid=get_query_param_or_default(request, "uuid", None)
            ).first()

            # If product does not exist
            if not product:
                return create_response(create_message([], 311), 404)

            product.delete()

            return create_response(create_message([], 1000), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)






