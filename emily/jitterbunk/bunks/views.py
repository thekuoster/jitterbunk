from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from bunks.models import Bunk, UserProfile
from django.contrib.auth.models import User


def index(request):
    latest_bunk_feed = Bunk.objects.order_by('-time')[:10]
    user_profiles = UserProfile.objects.all()

    context = {'latest_bunk_feed': latest_bunk_feed,
               'user_profiles': user_profiles}

    return render(request, 'bunks/index.html', context)


def detail(request, user_id):
    get_object_or_404(User, pk=user_id)

    bunks_from = Bunk.objects.filter(from_user=user_id).order_by('-time')
    bunks_to = Bunk.objects.filter(to_user=user_id).order_by('-time')
    context = {'bunks_from': bunks_from,
               'bunks_to': bunks_to,
               'user': User.objects.get(pk=user_id)}
    return render(request, 'bunks/detail.html', context)


def bunk(request, user_id):
    bunker = get_object_or_404(User, pk=user_id)

    username = request.POST['bunkee']

    bunks_from = Bunk.objects.filter(from_user=user_id).order_by('-time')
    bunks_to = Bunk.objects.filter(to_user=user_id).order_by('-time')

    context = {'bunks_from': bunks_from,
               'bunks_to': bunks_to,
               'user': User.objects.get(pk=user_id)}

    # prevent the ability to bunk oneself
    if bunker.username == username:
        context['error_message'] = 'You can\'t bunk yourself!'
        return render(request, 'bunks/detail.html', context)

    try:
        bunkee = User.objects.get(username=username)
    except (KeyError, User.DoesNotExist):
        error_message = username + ' does not exist. Please try again.'
        context['error_message'] = error_message
        return render(request, 'bunks/detail.html', context)
    else:
        new_bunk = Bunk(from_user=bunker, to_user=bunkee, time=timezone.now())
        new_bunk.save()

        return HttpResponseRedirect(reverse('bunks:detail', args=(bunker.id,)))
