from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
#for login 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST
        # field_name = request.POST.get('field_name')
        recipe_name = data.get('name')         #class name = data.get('html name')
        recipe_description = data.get('description')
        recipe_img = request.FILES.get('image')

        Recipe.objects.create(          #same name as in class
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_img = recipe_img,
        )

        return redirect('/recipe/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipes' : queryset}
    return render(request, 'home.html', context)



@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')



@login_required(login_url='/login/')
def update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        # field_name = request.POST.get('field_name')
        recipe_name = data.get('name')         #class name = data.get('html name')
        recipe_description = data.get('description')
        recipe_img = request.FILES.get('image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_img:
            queryset.recipe_img = recipe_img

        queryset.save()
        return redirect('/recipe/')

    context = {'recipe' : queryset}
    return render(request, 'update_recipe.html', context)





from django.contrib.auth import authenticate, login , logout
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login/')
        
        #for password
        user = authenticate(username = username , password = password)

        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipe/')
        
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/')




from django.contrib.auth.models import User
from django.contrib import messages   # use django messages for more on browser
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "User name already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully.")
        return redirect('/register/')
    
    return render(request, 'register.html')


@login_required(login_url='/login/')
def landing_page(request):
    return render(request, 'landing_page.html')
