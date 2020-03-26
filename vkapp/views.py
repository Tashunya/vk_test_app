from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests


# def login(request):
#     return render(request, 'registration/login.html')


@login_required
def friend_list(request):
    user = User.objects.get(username=request.user)
    social = user.social_auth.get(provider='vk-oauth2')
    token = social.extra_data["access_token"]
    user_url = f'https://api.vk.com/method/users.get?user_id={social.uid}'
    response = requests.get(user_url, params={'access_token': token,
                                              "v": "5.103",
                                              "fields": ["photo_200"]})
    user_pic = response.json()["response"][0]["photo_200"]
    friends_url = f'https://api.vk.com/method/friends.get?user_id={social.uid}'
    response = requests.get(friends_url, params={'access_token': token,
                                              'v': '5.103',
                                              "order": "random",
                                              "count": 5,
                                              "name_case": 'nom',
                                              "fields": ["city", "photo_50"]})
    friends = response.json()["response"]["items"]
    return render(request, 'vkapp/friend_list.html', {"user": user,
                                                      "user_pic": user_pic,
                                                      'friends': friends})
