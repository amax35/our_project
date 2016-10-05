import vk


def getPhotos(login, passwd):
    session = vk.AuthSession(app_id='5645063',
    user_login=login,
    user_password=passwd,
    scope='messages,photos')
    print(session)

    api = vk.API(session)
    profiles = api.users.get(user_ids=api.account.getProfileInfo().get("screen_name"))
    print (profiles)
    photos = api.photos.get(owner_id=profiles[0].get("uid"),
    album_id = "saved",
    count = 1000,
    photo_sizes = 1)
    arr = []
    for photo in photos:
        lst = photo.get('sizes')[len(photo.get('sizes')) - 1]
        arr.append(lst.get('src'))
    return arr    
    

arr = getPhotos('gt515ru@gmail.com', 'I27mVnAuq7O51SmpjgfcIMj2')
print (len(arr))