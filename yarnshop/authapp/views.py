from django.shortcuts import render, HttpResponseRedirect
from .forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse
from .forms import ShopUserRegisterForm
from .forms import ShopUserEditForm


def login(request):
    title = 'вход'
    header = 'Вход в систему'

    login_form = ShopUserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('index'))

    content = {'title': title, 'login_form': login_form, 'header': header, 'next': next}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    return HttpResponseRedirect(reverse('index'))


def edit(request):
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'
    header = 'Регистрация пользователя'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form, 'header': header}

    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'
    header = 'Редактирование профиля'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form, 'header': header}

    return render(request, 'authapp/edit.html', content)
