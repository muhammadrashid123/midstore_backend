from django.shortcuts import render

<<<<<<< Updated upstream
# Create your views here.
"""
All view related to the products management

"""

from product_management.product_management_controller import ProductsController,CategoryController
from rest_framework.views import APIView


class CategoryView(APIView):
    """CRUD Api view for the products Category"""
    category_controller=CategoryController()

    def post(self,request):

        return self.category_controller.add_category(request)

    def get(self,request):

        return self.category_controller.get_category(request)


    def patch(self,request):

        return self.category_controller.update_category(request)

    def delete(self,request):

        return self.category_controller.delete_category(request)


class ProductsView(APIView):
    """CRUD Api view for the products"""

    products_controller = ProductsController()

    def post(self, request):
        """Create a product"""

        return self.products_controller.create_product(request)

    def get(self,request):
        """get all products"""

        return self.products_controller.get_products(request)

    def patch(self,request):
        """update all products"""

        return self.products_controller.update_product(request)

    def delete(self,request):
        """delete all products"""

        return self.products_controller.delete_product(request)


=======
from rest_framework.views import APIView

from product_management.product_management_controller import CategoryController, ProductController


class CategoryView(APIView):

    category_controller_obj = CategoryController()

    def post(self, request):
        """ Create a Category"""

        return self.category_controller_obj.create_category(request)

class ProductView(APIView):
    """CRUD View for the Product model"""

    product_controller_obj = ProductController()

    def post(self, request):
        """Create new User"""

        return self.product_controller_obj.create_product(request)

    def patch(self, request):
        """Update a User"""

        return self.product_controller_obj.update_product(request)

    def get(self, request):
        """Get details of a User"""

        return self.product_controller_obj.get_product_details(request)

    def delete(self,request):
        """Delete existing User"""

        return self.product_controller_obj.delete_product(request)
>>>>>>> Stashed changes
