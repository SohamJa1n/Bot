import discord
import requests
import json


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith("$justinspam"):
        for i in range(25):
            await message.channel.send("justin")
    if message.content.startswith("$jacob"):
            for i in range(25):
                await message.channel.send("Jacob")
    elif message.content.startswith("$callum"):
        for i in range(25):
            await message.channel.send("Callum")
    elif message.content.startswith("$justin"):
            for i in range(25):
                await message.channel.send("Justin")
    elif message.content.startswith("$soham"):
            for i in range(25):
                await message.channel.send("Soham")
        

client.run("MTAwMjQ5NDUyNjM5NDQ4NjgxNA.GUwNMG.AGFkYRlFWSibHTf6PQluEBjVea1ZhqETL-q6HQ")