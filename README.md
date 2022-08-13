# used code
  ### HTML5
  ### Inline CSS
 
used dynamic template

  - code changes in .py files
    ### views.py
    in function, i have passed variable and in return i passed variable as mentioned in below code. Variable contains data that we will pass dynamically
   
   ### code<--
   
   def dynamic(request):
    customer_data = {
        "customer_details":{ "id" : 1, "name" : "customer-1" },
        "customer_users" : [
    { "user_id" : 1, "user_name" : "user-1" },
    { "user_id" : 2, "user_name" : "user-2" },]
    }
    return render(request, 'dynamic.html',{'customer_data': customer_data})
   
   ### code-->
    
   ### settings.py
    
    in settings i have passed "django.templates.context_processors". by this we can request for dynamic data in the html page
    
   ### code<--
    TEMPLATES = [
      { 'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ], }, },]
   ### code-->
    
   ### .html page
   
    we will pass the variable in {{ customer_data }} and do some logic conditions in {% for i in customer_data.items %}  after conditions we can pass the data by {{ customer_data.customer_details }}
