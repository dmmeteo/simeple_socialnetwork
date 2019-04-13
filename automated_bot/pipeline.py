from random import randint
import requests
from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/1', backend='redis://redis:6379/1')

base = 'http://web:8000/api/v1/'
posts = '{base}posts/'.format(base=base)
login = '{base}auth-token/'.format(base=base)
signup = '{base}users/'.format(base=base)
refresh = '{base}auth-refresh/'.format(base=base)
lorem_api = 'https://baconipsum.com/api/?type=all-meat&sentences=1'
headers = {'Accept': 'application/json'}


@app.task
def start(email, max_posts, max_likes):
    data = {
        'email': email,
        'password': email[::-1]
    }
    resp = requests.post(signup, data=data)
    # run next task
    get_jwt.delay(data, max_posts, max_likes)
    return 'OK'

@app.task
def get_jwt(data, max_posts, max_likes):
    api_token = ''
    max_posts = randint(1, int(max_posts))
    max_likes = randint(1, int(max_likes))

    resp = requests.post(login, data)
    if resp.ok:
        token = resp.json()['token']
        api_token = 'Bearer {token}'.format(token=token)

        # run next tasks
        for i in range(max_posts):
            send_post.delay(api_token)
        for i in range(max_likes):
            send_like.delay(api_token)
    return 'OK'

@app.task(bind=True, max_retries=10)
def send_post(token):
    headers['Authorization'] = token
    # get lorem text from post
    resp = requests.get(lorem_api)
    [lorem] = resp.json()
    resp = requests.post(posts, headers=headers, data={'text': lorem[:256]})
    return 'OK'

@app.task
def send_like(token):
    headers['Authorization'] = token
    post_list = requests.get(posts).json()
    url = '{base}posts/{pk}/likes/'.format(
        base=base,
        pk=randint(1, post_list['count']) # find posts sub by pagination value
    )
    resp = requests.put(url, headers=headers, data={'like': True})
    return 'OK'

