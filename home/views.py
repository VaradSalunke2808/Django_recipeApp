from django.shortcuts import render
from django.http import HttpResponse



peoples = [{'name':'Varad Salunke','age': 23},{'name':'Tejas Choudhari','age': 16},{'name':'Vaibhav Udhane','age': 15},{'name':'Pushpak Rane','age': 22},{'name':'Hrishi Kanade','age': 24}]

def res(request):
    return render(request,"index.html", context={'people':peoples})

def contact(request):
    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")

