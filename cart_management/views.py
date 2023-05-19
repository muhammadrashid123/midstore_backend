import json
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.core.serializers.json import DjangoJSONEncoder

from cart_management.models import Cart, Checkout
from cart_management.serializer import CartSerializer, CheckoutSerializer
from utils.response_utils import create_message, create_response
from authentication.views import ExpiringTokenAuthentication
from utils.encoders import CustomJSONEncoder

# Create your views here.


class CartAPIViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [ExpiringTokenAuthentication, BasicAuthentication]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def list(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_
        """
        
        try:
            id = request.GET.get('id', None)
            if id:
                self.queryset = self.queryset.get(pk=id)
            serialized_data = self.get_serializer(self.queryset, many=True)
            response= serialized_data.data
            return create_response(create_message(response, 1000), 200)
        except ObjectDoesNotExist as e:
            message = f"Cart item with {id} does not exit."
            return create_response(create_message([], 1001, message), 401)
        except Exception as e:
            message = str(e)
            return create_response(create_message([], message ,1001), 500)
        
    def create(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_
        """
        try:
            data = request.data
            data["user_token"] = request.user.auth_token.pk
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            data = serializer.data 
            return create_response(create_message(data, 320), 201)
        except ValidationError as e:
            return create_response(create_message([], 1001, str(e)), 400)
        except IntegrityError as e:
            return create_response(create_message([], 1001, str(e)), 500)
        except Exception as e:
            return create_response(create_message([], 1001, str(e)), 500)
    
    def update(self, request, pk=None):
        
        mandatory_key = ["id"]
        try:
            # Retrieve the object and perform any necessary validation
            id = request.data.get("id", None)
            if id:
                data = request.data
                data["user_token"] = request.user.auth_token.pk
                instance = Cart.objects.get(uuid=id)
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)

                # Save the updated object
                serializer.save()

                # Return a success response
                data = serializer.data
                return create_response(create_message(data, 321), 201)
            return create_response(create_message([mandatory_key],100), 400)
        except ValidationError as e:
            return create_response(create_message([], 1001, str(e)), 400)
        except ObjectDoesNotExist as e:
            message = f"Cart item with {id} does not exit."
            return create_response(create_message([], 1001, message), 401)
        except Exception as e:
            return create_response(create_message([], 1001, str(e)), 500)
        
    def destroy(self, request, pk=None):
        mandatory_key = ["ids"]
        try:
            ids = request.data.get('ids', None)
            if ids:
                if not isinstance(ids, list):
                    return create_response(create_message([],323), 400)
                # Retrieve the object to be deleted
                instance = self.queryset.filter(uuid__in=ids)
                # Delete the object
                instance.delete()
                # Return a success response
                return create_response(create_message([], 322), 201)
            return create_response(create_message([mandatory_key],100), 400)
        except ObjectDoesNotExist as e:
            message = f"Cart item with {id} does not exit."
            return create_response(create_message([], 1001, message), 401)
        except Exception as e:
            return create_response(create_message([], 1001, str(e)), 500)
        
class CheckoutAPIView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[BasicAuthentication, ExpiringTokenAuthentication]
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.all() 
    
    def create(self, request, *args, **kwargs):
        mandatory_key = ["payment_method"]
        product_LIST = []
        amount = 0
        try:
            payment_method = request.data.get("payment_method", None)
            if payment_method:
                user_token = request.user.auth_token.pk
                product_obj = Cart.objects.filter(user_token=user_token)
                for pro in product_obj:
                    product = {}
                    product["product_name"] = pro.product.title
                    product["product_price"] = float(pro.product.price)
                    amount += float(pro.product.price)
                    product_LIST.append(product)
                payload = {"user": request.user.pk, "cart_products":product_LIST, "amount":amount, "payment_method":payment_method}
                serializer = self.get_serializer(data=payload)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                resposne_data = serializer.data
                message = f"Checkout for {request.user.email} created successfully. "
                return create_response(create_message(resposne_data, 321, message), 201)
            return create_response(create_message([mandatory_key],100), 400)
        except ValidationError as e:
            return create_response(create_message([], 1001, str(e)), 400)
        except IntegrityError as e:
            return create_response(create_message([], 1001, str(e)), 500)
        except Exception as e:
            return create_response(create_message([], 1001, str(e)), 500)
            
            