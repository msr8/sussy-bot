from config import *
import time as t
import praw

def send_msg(url, msg):
    import json
    from urllib.request import Request, urlopen
    header = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    payload = json.dumps( {'content':msg} )
    req = Request(url, data=payload.encode(), headers=header)
    urlopen(req)


reddit = praw.Reddit(client_id = client_id,
client_secret = client_secret,
username = username,
password = password,
user_agent = 'Whatever')


while True:
    try:
        print(f'\nITS UP! ({t.asctime()})\n')

        for comment in praw.models.util.stream_generator(reddit.inbox.mentions, skip_existing=True):
            try:
                comment.reply(reply)
                send_msg(webhook_url, f'''**Comment:** {comment.body}\n**OP:** {comment.author}\n**Link:** {comment.context}''')
            
            except Exception as e:
                send_msg(webhook_url, f'''__**ERROR:**__\n\n```\n{e}```\n**Comment:** {comment.body}\n**OP:** {comment.author}\n**Link:** {comment.context}''')
    except:
        print(f'error at {t.asctime()} Restarting in 5 minutes')
        t.sleep(300)

