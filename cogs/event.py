import discord
from discord import app_commands
from discord.ext import commands

from model.Event import insert_event, get_all_events, get_event_by_name, update_event, delete_event


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="creer_un_evenement", description="permet de créer un évènement")
    async def create_event(self, interaction: discord.Interaction, nom: str, description: str, date: str):
        result = insert_event(nom, description, date)
        if isinstance(result, str):
            await interaction.response.send_message(f"> erreur: \n> {result}\n")
            return

        await interaction.response.send_message("insertion réussis!")

    @app_commands.command(name="voir_les_evenements", description="permet de voir tous les évènements")
    async def see_all_events(self, interaction: discord.Interaction):
        result = get_all_events()
        if isinstance(result, str):
            await interaction.response.send_message(f"> erreur: \n> {result}\n")
            return

        content = ""
        for event in result:
            content += f"> nom: {event.name}\n> description: {event.description}\n> date: {event.date}`"

        if not content:
            await interaction.response.send_message("> pas encore d'évènements pour le moment")
            return

        await interaction.response.send_message(content)

    @app_commands.command(name="modifier_un_evenement", description="permet de modifier un évènement")
    async def edit_event(self, interaction: discord.Interaction, nom_actuel: str, nom: str = None, description: str = None, date: str = None):
        result = get_event_by_name(nom_actuel)
        if isinstance(result, str):
            await interaction.response.send_message(f"> erreur: \n> {result}")
            return

        result = update_event(result.id, nom or result.name, description or result.description, date or result.date)
        if isinstance(result, str):
            await interaction.response.send_message(f"> erreur: \n> {result}")
            return

        await interaction.response.send_message("> message modifié avec succès")

    @app_commands.command(name="supprimer_un_evenement", description="permet de supprimer un évènement")
    async def delete_event(self, interaction: discord.Interaction, nom: str):
        result = get_event_by_name(nom)
        if isinstance(result, str):
            await interaction.response.send_message(f"> erreur: \n> {result}")
            return

        result = delete_event(result.id)
        if isinstance(result, str):
            await interaction.response.send_message(f"> erreur: \n> {result}")
            return

        await interaction.response.send_message("> message supprimé avec succès")


async def setup(bot):
    await bot.add_cog(EventCog(bot))
