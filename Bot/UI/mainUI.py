import discord
from discord.ui import View, Button
from discord import Embed

class mainUI(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(label="능력치 부여 방식", style=discord.ButtonStyle.primary))
        self.add_item(Button(label="등급 부여 방식", style=discord.ButtonStyle.primary))
        self.add_item(Button(label="주요 능력치 정보", style=discord.ButtonStyle.primary))
        embed = Embed(
            title="코어키퍼 요리 사전",
            description="요리 정보 검색기입니다.\n\n"
                        "많은 종류의 음식 재료 정보를 검색할 수 있습니다.",
            color=discord.Color.brand_green()
        )
        embed.set_thumbnail(url="https://blog.kakaocdn.net/dn/kRl8k/btsJpe7NuHe/rVVmdRixjkb6PztMgK30X1/img.png")

        self.embed = embed

def get_main_view():
    return mainUI()