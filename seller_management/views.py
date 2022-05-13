from django.shortcuts import render

# Create your views here.
from rest_framework.views  import APIView
from customer_management.customer_management_controller import CustomerManagement

class CustomerProfileView(APIView):
    """CRUD View for the Customer Profile model"""


    customer_controller = CustomerManagement()

    def post(self, request):
        """Create new Customer"""

        return self.customer_controller.creat_customer_profile(request)