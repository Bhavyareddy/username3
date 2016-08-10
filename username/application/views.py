from django.shortcuts import render,HttpResponse
from application.models import Usename


# Create your views here.
def Creat(request):
	return render(request,'change.html')
def change(request):
	user = request.POST.get('user')
	password = request.POST.get('pwd')
	o = Usename(username = user,password = password)
	if o.password == request.POST.get('pwd'):
		if request.POST.get('npwd') == request.POST.get('npwd1'):
			o.password = request.POST.get('npwd')
			o.save()
			print request.POST.get('user')
			print request.POST.get('pwd')
			print request.POST.get('npwd')
			print request.POST.get('npwd1')
			return HttpResponse("password correct")
		else:
			return HttpResponse("new password and confirm new password are not equal")
	else:
		return HttpResponse("password incorrect")