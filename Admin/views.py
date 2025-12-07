from django.shortcuts import render, redirect
from Admin.models import Product

# Create your views here.
def admin(request):
    products = Product.objects.all()
    return render(request, 'admin.html', {'products':products})



def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Product.objects.create(name=name, price=price, description=description)
        return redirect('admin')
    return render(request, 'add_item.html')

