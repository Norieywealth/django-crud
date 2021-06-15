from django.core import paginator
from django.shortcuts import redirect, render, HttpResponse
from userprofile.models import UserProfile
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from userprofile.forms import CreateUserForm
# Create your views here.


def index(request):
    return render(request, 'home.html')

def payment(request):
    return render(request, 'payment.html')

@login_required(login_url='profile:login')
def user_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not UserProfile.objects.filter(first_name=first_name, last_name=last_name).exists():
            UserProfile.objects.create(
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, 'Profile Created!')
        else:
            messages.success(request, 'User Profile Exists')
        return redirect('/profile')
    else:
        # Paginate
        profile = UserProfile.objects.all()
        paginator = Paginator(profile, per_page=5)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        count = profile.count()
        context = {

            'profiles': page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number),
            'count': count
        }

    return render(request, 'userprofile/profile.html', context)


@login_required(login_url='profile:login')
def edit_profile(request, id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not UserProfile.objects.filter(first_name=first_name, last_name=last_name).exists():
            profile = UserProfile.objects.get(id=id)
            profile.first_name = first_name
            profile.last_name = last_name
            profile.save()
            messages.success(request, 'Profile Updated')
            return redirect('/profile')
        else:
            messages.success(request, 'Profile Exists')
            profile = UserProfile.objects.get(id=id)
            context = {'profile': profile}
            # return redirect('/profile')
    else:
        profile = UserProfile.objects.get(id=id)
        context = {'profile': profile}

    return render(request, 'userprofile/edit_profile.html', context)


@login_required(login_url='profile:login')
def delete_profile(request, id):
    if request.method == 'POST':
        profile = UserProfile.objects.get(id=id)
        profile.delete()
        messages.success(request, 'Profile Deleted')
        return redirect('/profile')
    else:
        profile = UserProfile.objects.get(id=id)
        context = {'profile': profile}

    return render(request, 'userprofile/delete_profile.html', context)


def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile')
            else:
                messages.info(request, 'Username Or Password Is Incorrect')
                return redirect('/login')
            # context = {
            #     'username': username,
            #     'password': password
            # }
        else:
            return render(request, 'userprofile/login.html')
    else:
        return redirect('/profile')


def logoutPage(request):
    logout(request)
    return redirect('/')
