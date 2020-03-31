from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import time

from .utils import get_friend_list, get_user_pic_link


@login_required
def friend_list(request):
    """
    Get user uid and receive user pic and name and list of 5 random friends
    from vk api
    """
    user = User.objects.get(username=request.user)
    social = request.user.social_auth.get(provider='vk-oauth2')
    token = social.extra_data["access_token"]
    token_exp = social.extra_data['auth_time'] + social.extra_data['expires']
    if token_exp <= int(time.time()):
        return render(request, 'registration/login.html')
    user_pic = get_user_pic_link(social.uid, token)
    friends = get_friend_list(social.uid, token, 5)
    return render(request, 'vkapp/friend_list.html', {"user": user,
                                                      "user_pic": user_pic,
                                                      'friends': friends})
