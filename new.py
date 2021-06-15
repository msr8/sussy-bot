from config import *
import praw

def send_msg(url, msg):
    import json
    from urllib.request import Request, urlopen
    header = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    payload = json.dumps( {'content':msg} )
    req = Request(url, data=payload.encode(), headers=header)
    urlopen(req)


webhook_url = '[CENSORED]'

reddit = praw.Reddit(client_id = client_id,
client_secret = client_secret,
username = username,
password = password,
user_agent = 'Whatever')

reply = 'Did someone say *sus* 😱😱😱 HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING AMONG US REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 AMONG US IS THE BEST FUCKING GAME 🔥🔥🔥🔥💯💯💯💯 RED IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME TO MEDBAY AND WATCH ME SCAN 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY IS NO ONE FIXING O2 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH YOUR CREWMATE? NAME EVERY TASK 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus! ❓ ❓ Where!❓ Any sus! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I think it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂 r/amongusmemes r/unexpectedamongus r/expectedamongus perfectly balanced as all things should be r/unexpectedthanos r/expectedthanos for balance'



print('\nITS UP!\n')
for comment in praw.models.util.stream_generator(reddit.inbox.mentions, skip_existing=True):
    try:
        comment.reply(reply)
        send_msg(webhook_url, f'''**Comment:** {comment.body}
**OP:** {comment.author}
**Link:** {comment.context}''')
    
    except:
        send_msg(webhook_url, f'''ERROR:\n\n**Comment:** {comment.body}
**OP:** {comment.author}
**Link:** {comment.context}''')


