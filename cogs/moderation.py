"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.3.0
"""

import os
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class Moderation(commands.Cog, name="moderation"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="rules", description="Posts the server rules in the current channel"
    )
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def rules(self, context: Context) -> None:
        """
        Posts the rules
        """
        color = 0x4687f0
        embed = discord.Embed(
            title="1. Follow Discord TOS, and you must be 14+ to join.",
            description="""
This also applies to DM advertising to others!
If you are an age regressor, we ask that you do not come onto the server while regressed for your own safety. Discord can be a very dangerous place for someone young, so for the safety of members we ask that if you are regressed, that you go offline until you are not. 
Systems must have either a co-fronter or not be online if they are regressed/as littles under 14- all actions made by systems are their responsibility, and so we ask those with the proper maturity or supervision to be in chat for the safety of the little and other members. If they are not accompanied, they will be asked to be offline until safely monitored.
""",
            color=color,
        )
        await context.send(embed=embed)
        embed = discord.Embed(
            title="2. Be respectful and kind. Posess good faith in conversation.",
            color=color,
        )
        await context.send(embed=embed)

        embed = discord.Embed(
            title="3. No NSFW content.",
            description="""
This is an SFW server. NSFW content will be removed and banned, including public sexual flirting. 
Artistic nudity is allowed, but pornographic material is strictly prohibited. 
Have an appropriate username, banner, and profile. Failure to comply results in an immediate ban. 
            """,
            color=color,
        )
        await context.send(embed=embed)

        embed = discord.Embed(
            title="4. This is an English speaking space.",
            description="""
While all of us wish we spoke something else, we do not. We ask for the sake of communication and clarity that conversations remain in English.
We have no tolerance for people who use non-English words to obscure slurs and insults directed at other members.
Languages are fine if quoted, such as Latin, Greek, etc., when discussing demonolatry, hellenism, etc, in history. We ask you not to speak in Latin in chats, even though that is impressive.
                """,
            color=color,
        )
        await context.send(embed=embed)

        embed = discord.Embed(
            title="5. Absolutely no Discrimination",
            description="""
No discrimination, period. We accept all ethnicities, races, genders, and sexualities here. 
This extends to antisemitism, racism, transphobia, sexism, homophobia, etc., and colonial rhetoric, such as anti-Palestinian racism and supporting the British empire. 
                """,
            color=color,
        )
        await context.send(embed=embed)

        embed = discord.Embed(
            title="6. Respect the staff team and their decisions.",
            description="""
Respect the moderation team and staff, we are just people doing this in their free time, and here to keep the server running smoothly.
This is a discord, not a democracy. We strive for fairness but this is a discord server. Touching grass is something people should do. 
                """,
            color=color,
        )
        await context.send(embed=embed)

        embed = discord.Embed(title="7. Spoiler and CW sensitive content.", color=color)
        await context.send(embed=embed)

        embed = discord.Embed(
            title="8. Keep age roles clear, do not lie about your age.", color=color
        )
        await context.send(embed=embed)

        embed = discord.Embed(
            title="9. Absolutely no appropriation",
            description="""
We have a strict anti appropriation policy- including closed practices, misrepresentations of cultures, and bastardized depictions of other cultures or faiths.
Respect other people's practices. If it is dangerous or appropriating, go ahead and say something and/or bring it up to staff. Otherwise please be mindful and respectful of the practice individual pagans and witches hold.
Cultural Appropriation is not about whether or not entities can “consent” to being approached or cultural sharing, it is about a specific power imbalance between the in-group and out group.
For example, Native American religions are closed because they were colonised and thus prosecuted, with Native American Religions only allowed to be legally practised by Natives in 1978.

Commonly appropriated practices & entities are: Lilith, white sage, Hebrew in gentile contexts, Jewish mysticism in Medieval thought, aspects of Goetia and planetary magic, Kabbalah, Hebrew in planetary sigils, etc.
""",
            color=color,
        )
        await context.send(embed=embed)

        embed = discord.Embed(
            title="10. Do not speak on banned subjects.",
            description="""
Banned subjects are not allowed to be discussed. You can discuss them lightly within #discussion-and-thoughts but any and all promotion of them or deep details of it will be removed and are not allowed.

No promoting /heavy details of the topics below :
 - Indigo Children
 - Starseed
 - Divinekin of any type (including godshards, demonkin, yokaikin, angelkin, deitykin, reincarnations/incarnates, etc) (not including systems with demonkin and angelkin)
 - Black/White Magic (in that, the division between Black
 - Godspousal (allowed to be mentioned/discussed about, but not incredibly graphic or in depth because we are an sfw server-you can talk about it, just not in depth being the one doing it.)
 - Magic = bad and White Magic = good (is harmful and has racist connotations)
 - Reality Shifting/Jumping
 - Nonconsensual Love Spells towards specific people
 - Westernized/Bastardized Tulpas
 - "Spiritual Psychosis"
This is a no syscourse space (excluding topics such as system hopping as that is not supported in this server). We want this server to be a safe space that's not dissolving into arguments and frustrations, and people's mental health and history and all should remain a matter between you and qualified professionals. Trauma is between your physiatrist and you- staff is not professionals, and we do not want this to be a place of argument.
the reason in which these rules exist are for very good reasons, and if staff asks you to stop speaking of it, do so.
""",
            color=color,
        )

        await context.send(embed=embed)

        embed = discord.Embed(
            description="""
You can go to verify in #verification if you are not already by filling out the pinned form! with the proper required roles as well. 
And the most important, and last but not least, just be chill and have a good time. This is a space to learn, discuss, and have fun. ❤️
                """,
            color=color,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="kick",
        description="Kick a user out of the server.",
    )
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @app_commands.describe(
        user="The user that should be kicked.",
        reason="The reason why the user should be kicked.",
    )
    async def kick(
        self, context: Context, user: discord.User, *, reason: str = "Not specified"
    ) -> None:
        """
        Kick a user out of the server.

        :param context: The hybrid command context.
        :param user: The user that should be kicked from the server.
        :param reason: The reason for the kick. Default is "Not specified".
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                description="User has administrator permissions.", color=0xE02B2B
            )
            await context.send(embed=embed)
        else:
            try:
                embed = discord.Embed(
                    description=f"**{member}** was kicked by **{context.author}**!",
                    color=0xBEBEFE,
                )
                embed.add_field(name="Reason:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"You were kicked by **{context.author}** from **{context.guild.name}**!\nReason: {reason}"
                    )
                except:
                    # Couldn't send a message in the private messages of the user
                    pass
                await member.kick(reason=reason)
            except:
                embed = discord.Embed(
                    description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",
                    color=0xE02B2B,
                )
                await context.send(embed=embed)

    @commands.hybrid_command(
        name="nick",
        description="Change the nickname of a user on a server.",
    )
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    @app_commands.describe(
        user="The user that should have a new nickname.",
        nickname="The new nickname that should be set.",
    )
    async def nick(
        self, context: Context, user: discord.User, *, nickname: str = None
    ) -> None:
        """
        Change the nickname of a user on a server.

        :param context: The hybrid command context.
        :param user: The user that should have its nickname changed.
        :param nickname: The new nickname of the user. Default is None, which will reset the nickname.
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        try:
            await member.edit(nick=nickname)
            embed = discord.Embed(
                description=f"**{member}'s** new nickname is **{nickname}**!",
                color=0xBEBEFE,
            )
            await context.send(embed=embed)
        except:
            embed = discord.Embed(
                description="An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="ban",
        description="Bans a user from the server.",
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @app_commands.describe(
        user="The user that should be banned.",
        reason="The reason why the user should be banned.",
    )
    async def ban(
        self, context: Context, user: discord.User, *, reason: str = "Not specified"
    ) -> None:
        """
        Bans a user from the server.

        :param context: The hybrid command context.
        :param user: The user that should be banned from the server.
        :param reason: The reason for the ban. Default is "Not specified".
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    description="User has administrator permissions.", color=0xE02B2B
                )
                await context.send(embed=embed)
            else:
                embed = discord.Embed(
                    description=f"**{member}** was banned by **{context.author}**!",
                    color=0xBEBEFE,
                )
                embed.add_field(name="Reason:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"You were banned by **{context.author}** from **{context.guild.name}**!\nReason: {reason}"
                    )
                except:
                    # Couldn't send a message in the private messages of the user
                    pass
                await member.ban(reason=reason)
        except:
            embed = discord.Embed(
                title="Error!",
                description="An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to ban.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)

    @commands.hybrid_group(
        name="warning",
        description="Manage warnings of a user on a server.",
    )
    @commands.has_permissions(manage_messages=True)
    async def warning(self, context: Context) -> None:
        """
        Manage warnings of a user on a server.

        :param context: The hybrid command context.
        """
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                description="Please specify a subcommand.\n\n**Subcommands:**\n`add` - Add a warning to a user.\n`remove` - Remove a warning from a user.\n`list` - List all warnings of a user.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)

    @warning.command(
        name="add",
        description="Adds a warning to a user in the server.",
    )
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        user="The user that should be warned.",
        reason="The reason why the user should be warned.",
    )
    async def warning_add(
        self, context: Context, user: discord.User, *, reason: str = "Not specified"
    ) -> None:
        """
        Warns a user in his private messages.

        :param context: The hybrid command context.
        :param user: The user that should be warned.
        :param reason: The reason for the warn. Default is "Not specified".
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        total = await self.bot.database.add_warn(
            user.id, context.guild.id, context.author.id, reason
        )
        embed = discord.Embed(
            description=f"**{member}** was warned by **{context.author}**!\nTotal warns for this user: {total}",
            color=0xBEBEFE,
        )
        embed.add_field(name="Reason:", value=reason)
        await context.send(embed=embed)
        try:
            await member.send(
                f"You were warned by **{context.author}** in **{context.guild.name}**!\nReason: {reason}"
            )
        except:
            # Couldn't send a message in the private messages of the user
            await context.send(
                f"{member.mention}, you were warned by **{context.author}**!\nReason: {reason}"
            )

    @warning.command(
        name="remove",
        description="Removes a warning from a user in the server.",
    )
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        user="The user that should get their warning removed.",
        warn_id="The ID of the warning that should be removed.",
    )
    async def warning_remove(
        self, context: Context, user: discord.User, warn_id: int
    ) -> None:
        """
        Warns a user in his private messages.

        :param context: The hybrid command context.
        :param user: The user that should get their warning removed.
        :param warn_id: The ID of the warning that should be removed.
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        total = await self.bot.database.remove_warn(warn_id, user.id, context.guild.id)
        embed = discord.Embed(
            description=f"I've removed the warning **#{warn_id}** from **{member}**!\nTotal warns for this user: {total}",
            color=0xBEBEFE,
        )
        await context.send(embed=embed)

    @warning.command(
        name="list",
        description="Shows the warnings of a user in the server.",
    )
    @commands.has_guild_permissions(manage_messages=True)
    @app_commands.describe(user="The user you want to get the warnings of.")
    async def warning_list(self, context: Context, user: discord.User) -> None:
        """
        Shows the warnings of a user in the server.

        :param context: The hybrid command context.
        :param user: The user you want to get the warnings of.
        """
        warnings_list = await self.bot.database.get_warnings(user.id, context.guild.id)
        embed = discord.Embed(title=f"Warnings of {user}", color=0xBEBEFE)
        description = ""
        if len(warnings_list) == 0:
            description = "This user has no warnings."
        else:
            for warning in warnings_list:
                description += f"• Warned by <@{warning[2]}>: **{warning[3]}** (<t:{warning[4]}>) - Warn ID #{warning[5]}\n"
        embed.description = description
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="purge",
        description="Delete a number of messages.",
    )
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @app_commands.describe(amount="The amount of messages that should be deleted.")
    async def purge(self, context: Context, amount: int) -> None:
        """
        Delete a number of messages.

        :param context: The hybrid command context.
        :param amount: The number of messages that should be deleted.
        """
        await context.send(
            "Deleting messages..."
        )  # Bit of a hacky way to make sure the bot responds to the interaction and doens't get a "Unknown Interaction" response
        purged_messages = await context.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            description=f"**{context.author}** cleared **{len(purged_messages)-1}** messages!",
            color=0xBEBEFE,
        )
        await context.channel.send(embed=embed)

    @commands.hybrid_command(
        name="hackban",
        description="Bans a user without the user having to be in the server.",
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @app_commands.describe(
        user_id="The user ID that should be banned.",
        reason="The reason why the user should be banned.",
    )
    async def hackban(
        self, context: Context, user_id: str, *, reason: str = "Not specified"
    ) -> None:
        """
        Bans a user without the user having to be in the server.

        :param context: The hybrid command context.
        :param user_id: The ID of the user that should be banned.
        :param reason: The reason for the ban. Default is "Not specified".
        """
        try:
            await self.bot.http.ban(user_id, context.guild.id, reason=reason)
            user = self.bot.get_user(int(user_id)) or await self.bot.fetch_user(
                int(user_id)
            )
            embed = discord.Embed(
                description=f"**{user}** (ID: {user_id}) was banned by **{context.author}**!",
                color=0xBEBEFE,
            )
            embed.add_field(name="Reason:", value=reason)
            await context.send(embed=embed)
        except Exception:
            embed = discord.Embed(
                description="An error occurred while trying to ban the user. Make sure ID is an existing ID that belongs to a user.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="archive",
        description="Archives in a text file the last messages with a chosen limit of messages.",
    )
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        limit="The limit of messages that should be archived.",
    )
    async def archive(self, context: Context, limit: int = 10) -> None:
        """
        Archives in a text file the last messages with a chosen limit of messages. This command requires the MESSAGE_CONTENT intent to work properly.

        :param limit: The limit of messages that should be archived. Default is 10.
        """
        log_file = f"{context.channel.id}.log"
        with open(log_file, "w", encoding="UTF-8") as f:
            f.write(
                f'Archived messages from: #{context.channel} ({context.channel.id}) in the guild "{context.guild}" ({context.guild.id}) at {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n'
            )
            async for message in context.channel.history(
                limit=limit, before=context.message
            ):
                attachments = []
                for attachment in message.attachments:
                    attachments.append(attachment.url)
                attachments_text = (
                    f"[Attached File{'s' if len(attachments) >= 2 else ''}: {', '.join(attachments)}]"
                    if len(attachments) >= 1
                    else ""
                )
                f.write(
                    f"{message.created_at.strftime('%d.%m.%Y %H:%M:%S')} {message.author} {message.id}: {message.clean_content} {attachments_text}\n"
                )
        f = discord.File(log_file)
        await context.send(file=f)
        os.remove(log_file)


async def setup(bot) -> None:
    await bot.add_cog(Moderation(bot))
