import datetime

import discord
from discord import app_commands
from discord.ext import commands

from model.RaptorBadge import add_raptorbadge, get_user_raptorbadge
from model.Event import get_event_by_name


class RaptorBadgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="donner_raptor_badge", description="permet de donner un raptor badge à un joueur")
    async def add_raptor_badge(self, interaction: discord.Interaction, joueur: discord.Member, description: str, nom_evenement: str):
        event = get_event_by_name(nom_evenement)
        if isinstance(event, str):
            await interaction.response.send_message(f"> erreur: \n> {event}")
            return

        raptor_badge = add_raptorbadge(event.id, joueur.id, description)
        if isinstance(raptor_badge, str):
            await interaction.response.send_message(f"> erreur: \n> {raptor_badge}")
            return

        await interaction.response.send_message("> insertion réussis!")

    @app_commands.command(name="voir_raptor_badges", description="permet de voir tous les raptor badges d'un joueur")
    async def see_raptor_badges(self, interaction: discord.Interaction, joueur: discord.Member):
        raptor_badges = get_user_raptorbadge(joueur.id)
        if isinstance(raptor_badges, str):
            await interaction.response.send_message(f"> erreur: \n> {raptor_badges}")
            return
        if not raptor_badges:
            await interaction.response.send_message("> le joueur n'as pas de raptor badges pour le moment")

        content = ""
        for badge in raptor_badges:
            date = datetime.datetime.fromtimestamp(badge.date)
            content += f"> event: {badge.event.name}\n> description: {badge.description}\n> date: {date}"
        await interaction.response.send_message(content)


async def setup(bot):
    await bot.add_cog(RaptorBadgeCog(bot))
