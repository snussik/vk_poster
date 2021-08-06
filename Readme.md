# VK post publishing
Refers to: https://habr.com/ru/post/520860/

## Installing the package from git
` pip install git+https://github.com/snussik/vk_poster.git `

## Connect to VK API
1. Create a Standalone app: https://vk.com/editapp?act=create
2. In VK app settings https://vk.com/editapp use `ID приложения` of `int` type. 
3. Send request:
`https://oauth.vk.com/authorize?client_id=ID_приложения&scope=photos,wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token` & go to link.
4. In page url copy the `TOKEN`:
`https://api.vk.com/blank.html#access_token=TOKEN&expires_in=0&user_id=9999999`.
5. Get group address `club123456`.
6. Create `settings.py`:
```python
{
    "vk_ap_id" : ID_приложения,
    "token" : "TOKEN",
    "group" : "club123456",
    "v" :  5.122
}

```
7. Use like this:
```python
from vk_poster import VK
from settings import settings

if __name__ == "__main__":
    vk = VK(settings["token"], settings["v"], settings["group"])
    ph_path = './image.jpg'

    post_id = vk.quene_msg(photo=ph_path)

    if post_id != -1:
        print(post_id)
    else:
        print('Post error')


```
