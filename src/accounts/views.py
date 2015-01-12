# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forms import UserProfileForm


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.email = prof.username = form.cleaned_data['email']
            prof.save()

            messages.add_message(request, messages.INFO, u'Ваш профиль был успешно обновлен')
    else:
        form = UserProfileForm(instance=request.user)


    return render(request, 'accounts/profile.html', {'form': form, 'page_title': u'Мой профиль'})

