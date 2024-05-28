import discord
from discord import app_commands
from discord.ext import commands

from model.RaptorBadge import add_raptorbadge
from model.Event import get_event_by_name


class RaptorBadgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="donner_raptor_badge", description="permet de donner un raptor badge à un joueur")
    async def add_raptor_badge(self, interaction: discord.Interaction, joueur: discord.Member, description: str, nom_evenement: str):
        event = get_event_by_name(nom_evenement)
        if isinstance(event, str):
            await interaction.response.send_message(f"erreur: ```python\n{event}\n```")
            return

        raptor_badge = add_raptorbadge(event.id, joueur.id, description)
        if isinstance(raptor_badge, str):
            await interaction.response.send_message(f"erreur: ```python\n{raptor_badge}\n```")
            return

        await interaction.response.send_message("insertion réussis!")


"""
    @app_commands.command(name="voir_les_evenements", description="permet de voir tous les évènements")
    async def see_all_events(self, interaction: discord.Interaction):
        result = get_all_events()
        if isinstance(result, str):
            await interaction.response.send_message(f"erreur: ```python\n{result}\n```")
            return

        content = ""
        for event in result:
            content += f"```nom: {event.name}\ndescription: {event.description}\ndate: {event.date}```"

        await interaction.response.send_message(content)

    @app_commands.command(name="modifier_un_evenement", description="permet de modifier un évènement")
    async def edit_event(self, interaction: discord.Interaction, nom_actuel: str, nom: str = None, description: str = None, date: str = None):
        result = get_event_by_name(nom_actuel)
        if isinstance(result, str):
            await interaction.response.send_message(f"erreur: ```python\n{result}\n```")
            return

        result = update_event(result.id, nom or result.name, description or result.description, date or result.date)
        if isinstance(result, str):
            await interaction.response.send_message(f"erreur: ```python\n{result}\n```")
            return

        await interaction.response.send_message("message modifié avec succès")

    @app_commands.command(name="supprimer_un_evenement", description="permet de supprimer un évènement")
    async def delete_event(self, interaction: discord.Interaction, nom: str):
        result = get_event_by_name(nom)
        if isinstance(result, str):
            await interaction.response.send_message(f"erreur: ```python\n{result}\n```")
            return

        result = delete_event(result.id)
        if isinstance(result, str):
            await interaction.response.send_message(f"erreur: ```python\n{result}\n```")
            return

        await interaction.response.send_message("message supprimé avec succès")
"""


async def setup(bot):
    await bot.add_cog(RaptorBadgeCog(bot))
