from django.shortcuts import render

# Create your views here.


def friend_list(request):
    friends = ["Masha", "Kate", "Ann"]
    return render(request, 'vkapp/friend_list.html', {'friends': friends})
