from django.shortcuts import render
from userinfo.models import User
# Create your views here.
def index(request):
    return render(request,'userinfo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user': user_list}
    return render(request,'userinfo/user.html',context=user_dict)