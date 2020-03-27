from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .utils import get_friend_list, get_user_pic_link


@login_required
def friend_list(request):
    user = User.objects.get(username=request.user)
    social = user.social_auth.get(provider='vk-oauth2')
    token = social.extra_data["access_token"]
    user_pic = get_user_pic_link(social.uid, token)
    friends = get_friend_list(social.uid, token, 5)
    return render(request, 'vkapp/friend_list.html', {"user": user,
                                                      "user_pic": user_pic,
                                                      'friends': friends})
