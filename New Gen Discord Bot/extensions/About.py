import disnake
from disnake.ext import commands


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.author = 'LookAtYourSkill#8691'
        self.version = 1.0
        self.prefix = '/'

    @commands.slash_command(description='Information about the bot')
    async def about(self, inter: disnake.ApplicationCommandInteraction):
        about_embed = disnake.Embed(
            color=inter.author.color
        )
        about_embed.add_field(
            name='> Autor',
            value=f'`»` Der Bot wurde von `{self.author}` geschrieben',
            inline=False
        )
        about_embed.add_field(
            name='> Informationen',
            value=f'`»` Momentane Version: `{self.version}`\n'
                  f'`»` Momentanes Prefix: `{self.prefix}`',
            inline=False
        )
        about_embed.set_author(
            name=self.author
        )
        await inter.response.send_message(
            embed=about_embed
        )


def setup(bot):
    bot.add_cog(About(bot))
