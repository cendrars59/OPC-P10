from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdate
from .models import UserProductsSearch


def register(request):
    """"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f"compte utilisateur pour {username} a été créé, connectez-vous à votre compte",
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request,
                f"compte utilisateur pour {request.user.username} a été mis à jour",
            )
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdate(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'users/profile.html', context)


def listing(request):
    context = {}

    products = UserProductsSearch.get_products(request)

    paginator = Paginator(products, 6)
    # Get current page number
    page = request.GET.get('page')
    try:
        # Return only this page albums and not others
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context['products'] = products
    return render(request, 'users/user_search.html', context)
