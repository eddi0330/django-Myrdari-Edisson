from django.shortcuts import render

# Create your views here.
def view_b(request):
    return render(request,"view_b.html",context)