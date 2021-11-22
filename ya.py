import requests
token = ''
url = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }


def create_folder(folder):
    params = {
        'path': folder
        }
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


def check_status(folder_name):
    params = {
        'path': folder_name
    }
    response = requests.get(url, headers=headers, params=params)
    return response.status_code


if __name__ == '__main__':

    path_to_file = 'folder'
    result = create_folder(path_to_file)
    res = check_status(path_to_file)
    print(result)
    print(res)
