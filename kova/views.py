from django.shortcuts import render
def gudur(request):
    return render(request,'gudur.html',context={'name':'kova'})
# Create your views here.
