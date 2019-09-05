import random
import urllib.request
def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://images.unsplash.com/photo-1457301547464-91995555cd25?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=ca3e6701b2e2c7d01bdfcb92ce1a9a10&auto=format&fit=crop&w=773&q=80")
download_web_image('https://images.unsplash.com/photo-1488893441583-0054a3aca255?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=29f6a0b66263e875ad246d4d57aac130&auto=format&fit=crop&w=752&q=80')