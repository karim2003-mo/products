from django.http import JsonResponse ,  FileResponse
from .models import Product
import os
import shutil
import tempfile
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
            'description':product.description,
            'offer':product.offer if product.offer else None  # Handle offer being None 
        }
        datalist.append(mp)
    return JsonResponse({"products":datalist})
def download_db(request):
    db_path = "./db.sqlite3"  # Path to your SQLite database file 
    return FileResponse(open(db_path, "rb"), as_attachment=True, filename="db.sqlite3")
def download_media(request):
    media_path = "./media"
    
    # Create a temporary zip file
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    shutil.make_archive(temp.name, 'zip', media_path)
    
    # Serve the zip file
    return FileResponse(open(temp.name + ".zip", "rb"), as_attachment=True, filename="media.zip")
# Create your views here.
