"""
Module for VK API to get user data
"""
import requests
from string import Template


VERSION = '5.103'


def get_url(target, uid):
    """
    Return url to vk api depending on target
    :param target: 'users' to request user's info,
                    'friends' to request user's friends
    :param uid: user id in vk social net
    :return: url to vk api
    """
    url_template = Template('https://api.vk.com/method/$target.get?user_id'
                            '=$uid')
    return url_template.substitute(target=target, uid=str(uid))


def get_params(access_token: str, target_params: dict) -> dict:
    """
    Return parameters for request to vk api
    :param access_token: session token
    :param target_params: parameters for specific request
    :return: dict of params for url
    """
    base_params = {'access_token': access_token, "v": VERSION}
    base_params.update(target_params)
    return base_params


def get_friend_list(uid: str, access_token: str, count: int):
    """
    Return list of random friends in vk social net for specific user
    :param uid: user id in vk social net
    :param access_token: session token
    :param count: number of friends
    :return: list of user's friends
    """

    url = get_url("friends", uid)

    target_params = {
        'order': 'random',
        'count': count,
        'name_case': 'nom',
        'fields': ['photo_50']
    }
    params = get_params(access_token, target_params)

    response = requests.get(url, params=params)

    friend_list = response.json()["response"]["items"]

    return friend_list


def get_user_pic_link(uid: str, access_token: str):
    """
    Return url for large user's avatar
    :param uid: user id in vk social net
    :param access_token: session token
    :return: url
    """

    url = get_url('users', uid)

    target_params = {'fields': ['photo_200']}

    params = get_params(access_token, target_params)

    response = requests.get(url, params=params)

    user_pic_link = response.json()["response"][0]["photo_200"]

    return user_pic_link
