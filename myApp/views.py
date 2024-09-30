from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Car, Manufacturer
from .forms import CarForm
# Create your views here.

def index(request):
    queryset = Car.objects.all()
    context = {"cars": queryset}
    return render(request, 'index.html', context=context)


def product(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {"car": car}
    return render(request, "product.html", context=context)

def create(request):
    if request.method == "POST":
        form_data = CarForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            av = form_data.save(commit=False)
            av.image = form_data.cleaned_data['image']
            av.save()
            return redirect(index)
    return render(request, "create.html", {"form": CarForm})