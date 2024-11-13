import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from Bot.UI.SelectUI import get_select_view  # select UI 모듈 가져오기
from Bot.UI.MainUI import get_main_view

load_dotenv()

bot = commands.Bot(command_prefix="#", intents=discord.Intents.all())
token = os.getenv("TOKEN")

@bot.event
async def on_ready():       # 첫 실행 시
    print(f"{bot.user.name} 로그인 성공")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))


@bot.command()
async def start(message):       # #start 명령어 실행 시 메인UI 생성
    view = get_main_view()
    await message.channel.send(embed=view.embed, view=view)

bot.run(token)
