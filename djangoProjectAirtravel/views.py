from .models import Traveller
from django.shortcuts import redirect, render


def index_page(request):
    data = Traveller.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('name')
        phone = request.POST.get('name')
        origin = request.POST.get('name')
        destination = request.POST.get('name')
        payment = request.POST.get('name')

        query = Traveller(name=name, email=email, phone=phone, origin=origin, destination=destination,
                          payment=payment)
        query.save()
        return redirect("/")
    return render(request, "/")
