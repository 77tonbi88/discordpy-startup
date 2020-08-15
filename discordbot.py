import discord
import time
import random

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!kanchome":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            num = random.randint(1, 5)
            source = discord.FFmpegPCMAudio(str(num)+".mp3")
            voice_client.play(source)
            time.sleep(2)
            await voich.disconnect()
        except AttributeError:
            num = random.randint(1, 5)
            if num == 1:
                await message.channel.send("………なんのつもりだい？ " + message.author.name + "。")
            elif num == 2:
                await message.channel.send("ふわあ…" + message.author.name + "、今日はもう寝ないかい？僕もう眠いんだ…")
            elif num == 3:
                await message.channel.send("おはよう" + message.author.name + "！" + message.author.name + "は今朝もカッコイイぜ！")
            elif num == 4:
                await message.channel.send( message.author.name + "ーー！！　大事なコンサートほっぽりだして何やってんだよー！")
            elif num == 5:
                await message.channel.send("フゥ…やっとミラノに帰れるんだ…　あれ？あんなところにお菓子が落ちてるぞ。もったいないなあ…　あれ？船が動きだして…　わーーー" + message.author.name + "ーーーー!!!")


client.run("NzQzNjk3Mjc1OTI2MDg1Njgy.XzYcDw.BZrPLHkYCjGOOFTFXUmDzCDjwBk")
