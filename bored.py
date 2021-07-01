

import requests

URL = 'https://www.boredapi.com/api/activity'


def __check_valid_response_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_stuff():
    request = requests.get(URL)
    data = __check_valid_response_code(request)

    return data