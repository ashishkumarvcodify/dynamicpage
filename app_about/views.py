from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request, 'about.html')

def dynamic(request):
    customer_data = {
        "customer_details":{ "id" : 1, "name" : "customer-1" },
        "customer_users" : [
    { "user_id" : 1, "user_name" : "user-1" },
    { "user_id" : 2, "user_name" : "user-2" },]
    }

    return render(request, 'dynamic.html',{'customer_data': customer_data})