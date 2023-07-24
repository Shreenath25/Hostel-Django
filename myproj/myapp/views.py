from django.shortcuts import render
from myapp.models import hostel
# Create your views here.


count = 0
n = 1


def view1(request):
    return render(request, "home1.html")


def view2(request):
    global count
    x = int(request.GET["nos"])
    count = x
    return render(request, "home.html")


def view3(request):
    global count, n
    n = n+1
    adar = int(request.GET["adhar"])
    nam = request.GET["name"]
    ag = int(request.GET["age"])
    addr = request.GET["addr"]
    nat = request.GET["native"]
    mob = int(request.GET["mobile"])
    record = hostel.objects.create(
        adhar=adar, name=nam, age=ag, address=addr, native=nat, mobile=mob)
    if(n <= count):
        return render(request, "home.html")
    else:
        return render(request, "home2.html")


def view4(request):
    mob = int(request.GET["mob"])
    try:
        record = hostel.objects.get(mobile=mob)
        flag = 1
        name = record.name
        return render(request, "home3.html", {"flag": flag, "name": name})
    except:
        flag = 0
        return render(request, "home3.html", {"flag": flag})


def view5(request):
    record = hostel.objects.all().values()
    return render(request, "home4.html", {"d": record})
