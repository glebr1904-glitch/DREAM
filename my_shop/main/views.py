from django.shortcuts import render
from products.models import Category,Product

def index(request):
    categories=Category.objects.all()
    context={
        
        "title":"Главная страница",
        "header1":"ДРИМ  ",
        "header2":"Cветодиодная продукция YOULED ",
        "header3":"Освещение и Трековые системы ",
        "categories":categories,  

    }
    return render(request,'main/index.html', context)


def about(request):
    context={
        'title':'О нас',
        'about':"Мы занимаемся продажей и установкой потолков и тихих стен. Чтобы приобрести их переходите в каталог и выбирайте товар."

    }
    return render(request,'main/about.html',context)