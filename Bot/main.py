import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from selectUI import get_select_view  # select UI 모듈 가져오기

load_dotenv()

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
token = os.getenv("TOKEN")

# 봇이 처음으로 메시지를 받을 때 그 채널에 드롭다운을 보내도록 설정
first_message_sent = False

@bot.event
async def on_ready():       # 첫 실행 시
    print(f"{bot.user.name} 로그인 성공")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('테스트'))

@bot.event
async def on_message(message):
    global first_message_sent
    if message.author == bot.user:
        return  # 봇 자신의 메시지에는 반응하지 않음

    # 첫 메시지에 대한 응답으로 드롭다운을 보내고, 그 이후에는 반복하지 않음
    if not first_message_sent:
        await message.channel.send("드롭다운에서 옵션을 선택하세요:", view=get_select_view())
        first_message_sent = True

    await bot.process_commands(message)

bot.run(token)
