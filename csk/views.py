from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'Sahana','course':'Django'}
    return render(request,'dhoni.html',context=d)