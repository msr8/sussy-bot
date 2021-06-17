from config import *
import praw

def process_text(x):
    allowed_chars = 'qwertyuiopasdfghjklzxcvbnm'
    ret = ''
    temp = x.lower()
    for char in temp:
        if char in allowed_chars:
            ret += char
    return ret
    

reddit = praw.Reddit(client_id = client_id,
client_secret = client_secret,
username = username,
password = password,
user_agent = 'Whatever')

print('\nSussy bot reply script is up\n')
for comment in praw.models.util.stream_generator( reddit.inbox.comment_replies, skip_existing = True ):

    text = process_text(comment.body)
    print(text)

    if text == 'goodbot':
        comment.reply(good_reply)
    elif text == 'badbot':
        comment.reply(bad_reply)
