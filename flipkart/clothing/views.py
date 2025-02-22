from django.shortcuts import render
from clothing.models import Product
from .forms import ProductForm
# Create your views here.
def clothing(request):
    form = ProductForm()
    pro_img = Product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm() #reset form after saving
  
    return render(request, 'clothing/fashion.html', {'pro_img': pro_img, 'form':form})
