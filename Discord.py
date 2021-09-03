import discord
import random
from discord import member
from discord.ext import commands
from discord.member import Member
from music import Player
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents=intents)
random_jokes = ["Whoever said that the definition of insanity is doing the same thing over and over again and expecting different results has obviously never had to reboot a computer.", "Did you hear about the monkeys who shared an Amazon account? They were Prime mates.", "How much money does a pirate pay for corn? A buccaneer.",  "I'm a big fan of whiteboards. I find them quite re-markable.", """How do you stay warm in an empty room?
Go stand in the corner—it’s always 90 degrees.""", """Never trust math teachers who use graph paper. They're always plotting something.""", """What do you call friends who love math? Algebros""",  """Who is the leader of the Kitty Communist Party?
Chairman Meow.""", """What is the difference between capitalism and socialism?
In a capitalist society, man exploits man,  and in a socialist one, it’s the other way around.""", """If you are American inside the bathroom and when you come out the bathroom, what are you inside the bathroom? European""", """What do you call a fish with no eyes? A fsh.""", """Did you hear about the guy who invented the knock-knock joke? He apparently won the "no-bell" prize""", """What did one plate say to the other plate? Dinner is one me"""]
@client.event
async def on_ready():
    print("Let go let go let go let go let go")
@client.event
async def on_member_join(member):
    Role = 869404807566331954
    await member.add_roles(discord.Object(Role))
    print(f"{member} is a true Rager!")
@client.event
async def on_member_remove(member):
    print(f"{member} was not a true Rager after all!")
@client.command()
@commands.has_role("King Vamp")
async def free(ctx, member: discord.Member):
    Role = 869404807566331954
    await member.edit(roles = [])
    await ctx.send(f"{member} has been freed from prison!")
@client.command("creinv")
async def create_inv(ctx):
    link = await ctx.channel.create_invite(max_uses = 1)
    await ctx.send(content = str(link))
@client.command()
async def kick(ctx, member: discord.Member):
    await member.kick(reason = "Annoying")
@client.command("rr")
@commands.has_role("King Vamp")
async def remove_roles(ctx, member: discord.Member):
    await member.edit(roles = [])
@client.command()
@commands.has_role("King Vamp")
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} messages have been removed!", delete_after = 25)
@client.command()
async def joke(ctx):
    random_num = random.randint(0, (len(random_jokes)-1))
    await ctx.send(content = random_jokes[random_num])
@client.command()
async def ping(ctx):
    await ctx.send("Pong")
client.reaction_roles = []
@client.event
async def on_raw_reaction_add(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == payload.emoji.name:
            await payload.member.add_roles(client.get_guild(payload.guild_id).get_role(role_id))
            return
@client.event
async def on_raw_reaction_remove(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == payload.emoji.name:
            guild = client.get_guild(payload.guild_id)
            await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
            return
@client.command()
async def set_reaction(ctx, role: discord.Role=None, msg: discord.Message=None, emoji=None):
    if role != None and msg != None and emoji != None:
        await msg.add_reaction(emoji)
        client.reaction_roles.append((role.id, msg.id, emoji))
    else:
        await ctx.send("Invalid arguments")
async def setup():
    await client.wait_until_ready()
    client.add_cog(Player(client))
client.loop.create_task(setup())
