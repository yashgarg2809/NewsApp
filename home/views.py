from django.shortcuts import render
from home.models import Contact
import requests
import json
# Create your views here.


def index(request):
    print("Visited here")
    y = request.GET.get('q','')
    url = ""
    if(y==""):
        url = ('https://newsapi.org/v2/everything?q=india&apiKey=b794fa36db5f4020b8f4630f2c54b917')
    else:
        url = ('https://newsapi.org/v2/everything?q=' + y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917')

    response = requests.get(url)

    # print(response.json())
    print(type(response.json()))
    x = response.json()
    print(x["totalResults"])

    # for articles in x["articles"]:
    #     print(articles["author"])
        
    # x = json.loads(response.json())
    # print(x["totalResults"])
    # print(type(x))



    
        

   
    # json_object = json.loads(json_raw[0])
    
    # for datas in response:
    #     print(type(datas))
    return render(request,'index.html', x)

def business(request):
    print("Visited here")
    y = request.GET.get('q','')
    if(y==""):
        url = ('https://newsapi.org/v2/top-headlines?category=business&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    else:
        url = ('https://newsapi.org/v2/everything?q='+ y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')

    response = requests.get(url)
    print(type(response.json()))
    x = response.json()

    return render(request,'index.html', x)

def sports(request):
    print("Visited here")
    y = request.GET.get('q','')
    if(y==""):
        url = ('https://newsapi.org/v2/top-headlines?category=sports&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    else:
        url = ('https://newsapi.org/v2/everything?q='+ y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    response = requests.get(url)
    
    

    x = response.json()
    
    return render(request,'index.html', x)

def technology(request):
    print(request)
    y = request.GET.get('q','')
    # page = request.GET.get('page', '1')
    if(y==""):
        url = ('https://newsapi.org/v2/top-headlines?category=technology&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    else:
        url = ('https://newsapi.org/v2/everything?q='+ y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    response = requests.get(url)
    # print(type(response.json()))
    x = response.json()

    return render(request,'index.html', x)

def entertainment(request):
    print("Visited here")
    y = request.GET.get('q','')
    if(y==""):
        url = ('https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    else:
        url = ('https://newsapi.org/v2/everything?q='+ y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    response = requests.get(url)
    print(type(response.json()))
    x = response.json()

    return render(request,'index.html', x)

def health(request):
    print("Visited here")
    y = request.GET.get('q','')
    if(y==""):
        url = ('https://newsapi.org/v2/top-headlines?category=health&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    else:
        url = ('https://newsapi.org/v2/everything?q='+ y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    response = requests.get(url)
    print(type(response.json()))
    x = response.json()

    return render(request,'index.html', x)

def science(request):
    print("Visited here")
    y = request.GET.get('q','')
    if(y==""):
        url = ('https://newsapi.org/v2/top-headlines?category=science&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    else:
        url = ('https://newsapi.org/v2/everything?q='+ y + '&apiKey=b794fa36db5f4020b8f4630f2c54b917&pageSize=100')
    response = requests.get(url)
    print(type(response.json()))
    x = response.json()

    return render(request,'index.html', x)


def newsletter(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name = name, email = email)
        contact.save()
    return render(request, 'newslet.html')



