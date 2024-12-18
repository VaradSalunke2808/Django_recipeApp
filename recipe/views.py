from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

def Recipes(request):
    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('img')
        name = data.get('name')
        desc = data.get('desc')
        print(name)
        print(desc)
        print(img)
        Recipe.objects.create(name=name,desc=desc,img=img)

        return redirect('/recipe/')
    queryset = Recipe.objects.all()
    context = {'rec' : queryset}
    return render(request, 'recipe.html',context)


def deleteres(request,id):
    query = Recipe.objects.get(id=id)
    query.delete()

    return redirect('/recipe/')



