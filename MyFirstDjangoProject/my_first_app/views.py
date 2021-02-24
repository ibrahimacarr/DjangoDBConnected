from django.shortcuts import render
from my_first_app.models import  User, Car

# Create your views here.
def index(request):
    user_list = {'users': User.objects.order_by('BirthDate')}
    return render(request, 'my_first_app/index.html', context=user_list)
