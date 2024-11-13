import discord
from discord.ui import View, Button

class ClickButtonEvent():
    async def click_ability_button(interaction: discord.Interaction):
        embed = discord.Embed(
            title="요리 능력치 부여 방식",
            description="재료 a + 재료 b + @(임의의 추가 수치)",
            color=discord.Color.dark_orange()
        )
        await interaction.response.send_message(embed=embed)

    async def click_grade_button(interaction: discord.Interaction):
        embed = discord.Embed(
            title="요리 등급 업 조건\n",
            description="요리의 등급을 올리기 위한 조건들입니다.",
            color=discord.Color.green()  # 원하는 색상 설정
        )

        # 노말 -> 레어 설명 추가
        embed.add_field(
            name="A. 노말 → 레어",
            value="음식 스킬에서 [일정 확률로 등급 업 된 요리가 나오게 해줌] 스킬",
            inline=False
        )

        # 레어 -> 에픽 설명 추가
        embed.add_field(
            name="B. 레어 → 에픽",
            value="황금작물(원예 스킬)을 재료로 사용 필요",
            inline=False
        )

        await interaction.response.send_message(embed=embed)

    async def click_info_button(interaction: discord.Interaction):
        embed = discord.Embed(
            title="주요 능력치 \n",
            color=discord.Color.gold()
        )

        embed.add_field(
            name="A. 보스",
            value="피해, 피해감소",
            inline=False
        )
        embed.add_field(
            name="B. 치명타",
            value="확률, 피해",
            inline=False
        )
        embed.add_field(
            name="C. 피해 증가",
            value="몬스터, 채굴",
            inline=False
        )
        embed.add_field(
            name="D. 공격(피해량)",
            value="근접, 원거리",
            inline=False
        )
        embed.add_field(
            name="E. 공격 속도",
            value="근접, 원거리",
            inline=False
        )
        embed.add_field(
            name="F. 그 외 옵션",
            value="이동 속도, 회피 확률, 방어력, 가시 피해, 채굴 속도",
            inline=False
        )

        await interaction.response.send_message(embed=embed)

    async def click_ingredient_button(interaction: discord.Interaction):
        await interaction.response.send_message("버튼")
