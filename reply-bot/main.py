from config import *
import random as r
import time as t
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

while True:
    try:
        print(f'\nSussy bot reply script is up ({t.asctime()})\n')
        for comment in praw.models.util.stream_generator( reddit.inbox.comment_replies, skip_existing = True ):

            text = process_text(comment.body)
            
            if 'u/sussy-bot-2' in comment.body:
                comment.reply(default_reply)
            elif text == 'goodbot':
                comment.reply( r.choice(good_replies) )
            elif text == 'badbot':
                comment.reply( r.choice(bad_replies) )
    except:
        print(f'error at {t.asctime()} Restarting in 5 minutes')
        t.sleep(300)
