import discord
from discord.ui import View, Button
from discord import Embed
from Bot.Event.ClickButtonEvent import ClickButtonEvent as cbe


class MainUI(View):
    def __init__(self):
        super().__init__()

        # 능력치 부여 방식
        ability_button = Button(label="능력치 부여 방식", style=discord.ButtonStyle.primary)
        ability_button.callback = cbe.click_ability_button  # 콜백 함수 할당
        self.add_item(ability_button)

        # 등급 부여 방식
        grade_button = Button(label="등급 부여 방식", style=discord.ButtonStyle.primary)
        grade_button.callback = cbe.click_grade_button
        self.add_item(grade_button)

        # 주요 능력치 정보
        info_button = Button(label="주요 능력치 정보", style=discord.ButtonStyle.primary)
        info_button.callback = cbe.click_info_button
        self.add_item(info_button)

        # 재료가 보유한 능력치
        ingredient_button = Button(label="재료 사전", style=discord.ButtonStyle.primary.green)
        ingredient_button.callback = cbe.click_ingredient_button
        self.add_item(ingredient_button)


        # Embed 생성
        embed = Embed(
            title="코어키퍼 요리 사전",
            description="요리 정보 검색기입니다.\n\n많은 종류의 음식 재료 정보를 검색할 수 있습니다.",
            color=discord.Color.green()  # 올바른 색상 설정
        )
        embed.set_thumbnail(url="https://blog.kakaocdn.net/dn/kRl8k/btsJpe7NuHe/rVVmdRixjkb6PztMgK30X1/img.png")
        self.embed = embed


def get_main_view():
    return MainUI()
