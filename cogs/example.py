import discord
from discord.ext import commands
from discord import Embed, Color

import requests
import lxml.html

class Example(commands.Cog):
    """
    Represents a Cog for DEV.BG webinar example.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=('num?',))
    async def test(self, ctx, num: int):
        """
        The main command which handles the code execution process.
        """
        await ctx.send(f"The number entered {num}")


    async def test(self, ctx, num):
        number = 0
        number += 1
        await ctx.send(f"The number entered {number}")


    @commands.command()
    async def jobs(self, ctx, key: str, count: int):
        """
        """
                
        res = requests.get(f'https://dev.bg/company/jobs/{key}/')
        doc = lxml.html.fromstring(res.content)
        job_ads = doc.xpath('//*[@id="jobs"]/div')
        embed=discord.Embed(title="Dev.BG Jobs", url=f'https://dev.bg/company/jobs/{key}/', description="Обяви за работа с ", color=0x0059ff)
        
        for job in job_ads[:count]:
            title = job.cssselect('.h3-style3')[0].text_content().strip()
            link = job.cssselect('.h3-style3 a')[0].get("href").strip()
            info = job.cssselect('.small-txt')[0].text_content().strip()

            embed.add_field(name=title, value=f"[Линк]({link}) | {info}", inline=False)

        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Example(bot))