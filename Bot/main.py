import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
token = os.getenv("TOKEN")

# 로그인
@bot.event
async def on_ready():
    print(f"{bot.user.name} 로그인 성공")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # 봇 자신의 메시지에는 반응하지 않음

    await message.channel.send(message.content)  # 입력한 메시지를 다시 리턴
    await bot.process_commands(message)  # 명령어 처리를 위해 필요

bot.run(token)