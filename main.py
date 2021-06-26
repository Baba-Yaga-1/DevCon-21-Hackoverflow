
import discord
from discord import activity
import requests
import json
import jokeApi
import bored
import fakeUser

bot = discord.Client()
url = 'https://api.covid19india.org/data.json'

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

@bot.event
async def on_ready():
    print("I have logged in "+str(bot.user))

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return

    if message.content.startswith('$hello bot'):
        await message.channel.send('Hey User!')

    if message.content.startswith('$Check_covid'):
        channel = message.channel
        current_day= json.loads(requests.get(url).content)
        data = current_day['cases_time_series'][-1]
        await message.channel.send('Daily confirmed cases in India :'+data['dailyconfirmed'])
    
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$joke'):
        joke = jokeApi.get_joke()
        print(joke)

        if joke == False:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])

    if message.content.startswith('$bored'):
        activity = bored.get_stuff()
        print(activity)

        if activity == False:
            await message.channel.send("Couldn't get activity from API. Try again later.")
        else:
            await message.channel.send(activity)

    if message.content.startswith('$fakeUserInfo'):
        user = fakeUser.get_user()
        print(user)

        if user == False:
            await message.channel.send("Couldn't get user info from API. Try again later.")
        else:
            await message.channel.send(user)

bot.run('ODU4MjA3MzY1ODk1MDI4Nzc3.YNax5A.uSjfBK73MX5rnRFSian8j3Qpt2Y')