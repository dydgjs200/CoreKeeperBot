import discord
from discord.ui import Select, View

class MySelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="옵션 1", description="첫 번째 옵션입니다", value="option1"),
            discord.SelectOption(label="옵션 2", description="두 번째 옵션입니다", value="option2"),
            discord.SelectOption(label="옵션 3", description="세 번째 옵션입니다", value="option3"),
        ]
        super().__init__(placeholder="옵션을 선택하세요...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"당신이 선택한 옵션: {self.values[0]}")

def get_select_view():
    view = View()
    view.add_item(MySelectMenu())
    return view
