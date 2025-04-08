from django.http import JsonResponse
from .models import Product
def veiwproducts(request):
    datalist=[]
    products=Product.objects.all()
    for product in products:
        mp={
            'name':product.name,
            'price':product.price,
            'category':product.category,
            'rating':product.rating,
            'image':product.image.url if product.image else None,  # Ensure image URL is valid
            'description':product.description
        }
        datalist.append(mp)
    return JsonResponse({"products":datalist})
# Create your views here.
