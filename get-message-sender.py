import discord

file = open("api-key","r")
if file.mode == 'r':
    token = file.read()
    apitoken = str(token)

disc = discord.Client()
message_count = {}

@disc.event
async def on_ready():
    print('We have logged in as {0.user}'.format(disc))

@disc.event
async def on_message(message):
    sender_full = str(message.author)
    sender = sender_full[:-5]
    print(str(message.content))
    print("\n")
    doc = {}
    doc["full_user"] = str(message.author)
    doc["user"] = doc["full_user"].split('#',1)[0]
    doc["content"] = str(message.content)
    doc["channel"] = str(message.channel)
    doc["mentions"] = str(message.mentions)
    doc["id"] = str(message.id)
    doc["user_id"] = str(message.author.id) 
    doc["_timestamp"] = str(message.created_at)
    print(doc)

    if sender not in message_count.keys():
        message_count[sender] = 1
    else:
        message_count[sender] = message_count[sender]+1
    print(message_count)
    print("\n\n")

disc.run(apitoken)