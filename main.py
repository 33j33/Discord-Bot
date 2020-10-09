from discord.ext import commands
import asyncio
import discord
import aiohttp
import time
import datetime
import os
from webserver import keep_alive

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

embed_global = discord.Embed(title='Error Message', color=discord.Color.red())
embed_global.add_field(name='--', value='--')



@bot.event
async def on_ready():
    channel = bot.get_channel(590062663615250432)
    await channel.send(f"Bot {bot.user} is ready!")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)



@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')


@bot.command(name='invite_link')
async def create_invite_link(ctx):
    perm = discord.permissions.Permissions.all()
    invite_link = discord.utils.oauth_url(client_ID, permissions=perm)
    await ctx.send(f"Invite Link for the bot: \n" f"{invite_link}")


@bot.command(name='hello')
async def send_greetings(ctx):
    await ctx.send(f"Hello {ctx.author}, How's your day going?")


@bot.command(name='help', description='help_command', pass_context=True)
async def send_help_commands(ctx):
    embed = discord.Embed(
        title="HELP",
        description="The lists of commands this bot can perform",
        color=discord.Color.blurple())
    embed.add_field(name="!hello", value="Greets the user", inline=False)
    embed.add_field(
        name='!ping',
        value='Pings the bot to return its latency',
        inline=False)
    embed.add_field(name="!invite_link", value='Creates an invite for the Bot. Using this link the bot can be added to any server', inline=False)
    embed.add_field(
        name='!user_info <username>',
        value='Returns the user information',
        inline=False)
    embed.add_field(
        name='!have_i_been_pawned <account>',
        value=
        'This command checks whether your account has been compromised in any data breach.',
        inline=False)
    embed.add_field(name='!s_url <long url>', value="Returns the short url for the long url you pass to it", inline=False)
    embed.add_field(name='!newsletter_', value="Display the commands to set your news_letter", inline=False)    
    embed.add_field(
        name='!weather_',
        value='Display all the weather commands this bot can execute',
        inline=False)
    embed.add_field(
        name='!space_',
        value='Display all the space related commands this bot can execute',
        inline=False)
    embed.add_field(
        name='!fun_',
        value='Display all the fun commands this bot can execute',
        inline=False)
    embed.add_field(
        name='!finance_',
        value='Display all the finance related commands this bot can execute',
        inline=False)
    embed.add_field(
        name='!aqi_',
        value='Display all the commands to find Air Quality Index '
        'and Pollution markers for a location')
    await ctx.send(ctx.message.channel, embed=embed)


@bot.command(name='newsletter_')
async def send_news_letter_commands(ctx):
    embed = discord.Embed(title="NEWSLETTER - Create your own newsletter",
                          description="The following are the commands to set and receive your newsletter",
                          inline=False)
    embed.add_field(name="!news_sources [,sources]",
                    value="Sets the news sources for your newsletter."
                          "You can find the list of sources to select from, at this URL: https://newsapi.org/sources", inline=False)
    embed.add_field(name="!newsletter", value="Sends you your newsletter according to the sources you have set", inline=False)
    embed.set_thumbnail(url="http://d6vsczyu1rky0.cloudfront.net/31605_b/wp-content/uploads/2016/07/Newsletter-logo.jpg")
    await ctx.send(embed=embed)

@bot.command(
    name='weather_',
    description='The weather commands this bot can execute',
    pass_context=True)
async def send_weather_commands(ctx):
    embed = discord.Embed(
        title="!weather - WEATHER COMMANDS",
        description="The weather commands this bot can execute",
        color=discord.Color.blurple())
    embed.add_field(
        name="!weather <name of the place>",
        value=
        "Sends you detailed weather report of the place you pass along with the command",
        inline=False)
    embed.add_field(
        name="!weather_zip <zip code>[,country code]",
        value=
        "Sends you detailed weather report of the place for the zip code you pass along with the command",
        inline=False)
    embed.add_field(
        name='!weather_geoloc <latitude> <longitude>',
        value=
        'Sends you detailed weather report of the place for coordinates you pass along with the command',
        inline=False)
    embed.add_field(
        name='!weather_nearby <latitude> <longitude> <count>',
        value='Sends you the weather report of tha places nearby'
        ' the place for the coordinates you pass along with the command',
        inline=False)
    await ctx.send(embed=embed)


@bot.command(
    name='space_',
    description='The space related commands this bot can execute',
    pass_context=True)
async def send_space_commands(ctx):
    embed = discord.Embed(
        title="!space - SPACE COMMANDS",
        description="The space related commands this bot can execute",
        color=discord.Color.blurple())
    embed.add_field(
        name="!apod",
        value="Sends you the Astronomy Picture of the Day (APOD) by NASA",
        inline=False)
    embed.add_field(
        name="!people_in_space",
        value=
        "Sends you the number and names of people in space at this momemt",
        inline=False)
    embed.add_field(name="!spacex_launch <latest/next>",
                    value="Sends you the latest and upcoming launch details of SpaceX depending upon the argument you pass",
                    inline=False)    
    embed.add_field(
        name='!iss_position',
        value='Send you the coordinats of International Space Station(ISS) - '
        'the current ISS location over earth',
        inline=False)
    embed.add_field(
        name='!iss_pass_times <latitude> <longitude> <altitude>',
        value='Sends you the number of times ISS will pass over our heads'
        ' at the current location you pass along with the command',
        inline=False)
    await ctx.send(embed=embed)


@bot.command(
    name='fun_',
    description='The fun things this bot can do',
    pass_context=True)
async def send_fun_commands(ctx):
    embed = discord.Embed(
        title="!fun - FUN COMMANDS",
        description="The fun things this bot can do",
        color=discord.Color.blurple())
    embed.add_field(
        name="!memes",
        value="Sends you the hottest and funniest memes",
        inline=False)
    embed.add_field(
        name="!programming_memes",
        value="Sends you the geekiest programming related memes",
        inline=False)
    embed.add_field(
        name='!history_memes',
        value='Send the best of historical jokes and memes',
        inline=False)
    embed.add_field(
        name='!aww',
        value='Sends you Things that make you go AWW! -- '
        'like puppies, cats, bunnies, babies, and so on',
        inline=False)
    embed.add_field(
        name='!data_is_lit',
        value=
        'Sends you the most interesting visual representations of data: Graphs, charts, maps',
        inline=False)
    embed.add_field(
        name='!maps_are_lit', value='Sends you interesting maps', inline=False)
    embed.add_field(
        name='!earth_is_lit',
        value='Sends the pics of most stunning places on Earth',
        inline=False)
    embed.add_field(
        name='!quotes',
        value='Sends you thoughtful, inspiring or funny quotes',
        inline=False)
    embed.add_field(
        name='!wallpapers',
        value='Sends you amazing wallpapers for your PC',
        inline=False)
    embed.add_field(
        name='!facts',
        value='Sends you most intriguing and surprising fun facts',
        inline=False)
    embed.add_field(
        name='!news',
        value='Sends you popular world news items of the day',
        inline=False)
    await ctx.send(ctx.message.channel, embed=embed)


@bot.command(name='finance_', description='finance_command', pass_context=True)
async def send_finance_commands(ctx):
    embed = discord.Embed(
        title="!finance: Commands related to Finance",
        description="",
        color=discord.Color.blurple())
    embed.add_field(
        name="!forex <base currency code>",
        value=
        "Sends you the exchange rate of the currency passed, for all major currencies",
        inline=False)
    embed.add_field(
        name='!forex <base currency code> [, target currency codes]',
        value=
        'Sends you the exchange rate for the based currency and target currencies you pass',
        inline=False)
    embed.add_field(
        name='!convert <amount> <base currency code> <, target currency code>',
        value=
        'Send you the amount converted into the target currencies you pass',
        inline=False)
    embed.add_field(
        name='!coin_info <coin> <target currency>',
        value=
        'Send you the information about the coin in the target currency you mention',
        inline=False)
    embed.add_field(
        name='!coin_exchanges <coin> <target currency>',
        value=
        'Sends you the top 3 markets and their exchanges for the coin, currency pair',
        inline=False)
    embed.add_field(
        name='!coin_list <target_currency> <order>',
        value=
        'Sends you the list of coins in the descending order of rank or volume'
        ' with their price information in target currency',
        inline=False)
    await ctx.send(ctx.message.channel, embed=embed)


@bot.command(name='aqi_', description='aqi_command', pass_context=True)
async def send_aqi_commands(ctx):
    embed = discord.Embed(
        title="!aqi: Air Quality Index",
        description="The list of commands to find Air Quality Index"
        " and Pollution markers for the place you mention",
        color=discord.Color.blurple())
    embed.add_field(
        name="!aqi <latitude> <longitude>",
        value="Sends the AQI and pollution level for the coordinates you pass",
        inline=False)
    embed.add_field(
        name='!aqi_stations <name of the place>',
        value=
        'Send you the list of Pollution Detection Stations in the place you pass',
        inline=False)
    await ctx.send(ctx.message.channel, embed=embed)


@bot.command(name='user_info', pass_context=True)
async def user_info(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(
            title="Write the username along with the command",
            description="!user_info username#3455",
            color=discord.Color.blurple())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="USER INFO FOR: {}".format(user.display_name),
            colour=discord.Color.blue())
        embed.add_field(
            name="Username:", value=("`{}`".format(user.name)), inline=False)
        embed.add_field(
            name="User Discriminator",
            value=("`{}`".format(user.discriminator)),
            inline=True)
        pfp = user.avatar_url
        embed.set_thumbnail(url=pfp)
        embed.add_field(
            name="User ID:", value=("`{}`".format(user.id)), inline=False)
        embed.add_field(
            name="User Status:",
            value=("`{}`".format(user.status)),
            inline=True)
        embed.add_field(
            name="User Highest Role:",
            value=("`{}`".format(user.top_role)),
            inline=False)
        embed.add_field(
            name="User Joined this server on:",
            value=("`{}`".format(user.joined_at)),
            inline=True)
        embed.add_field(
            name="User Joined Discord on:",
            value=("`{}`".format(user.created_at)),
            inline=True)
        embed.add_field(
            name="User is a robot?",
            value=("`{}`".format(user.bot)),
            inline=True)
        embed.add_field(
            name="User Nickname:",
            value=("`{}`".format(user.display_name)),
            inline=True)
        await ctx.send(embed=embed)


# =================================================== QUOTE ===================================================== #

bot.deque_list_quote = []
bot.counter_quote = 0


@bot.command(name='quotes', pass_context=True)
async def send_quote(ctx):
    bot.deque_list_quote = await set_quote()
    bot.counter_quote += 1
    if bot.counter_quote >= len(bot.deque_list_quote):
        bot.counter_quote = 0
    await ctx.send(f"{bot.deque_list_quote[bot.counter_quote]}")
    


async def set_quote():
    epoch = time.time()
    quote_at = str(int(epoch) - 129600 * 10)
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "http://api.pushshift.io/reddit/submission/search?subreddit="
                "quotes&score=>100&sort_type=score&after=" + quote_at) as resp:
            data = await resp.json()
            list_of_quotes = []
            for i in data["data"]:
                list_of_quotes.append(i["title"])
            return list_of_quotes


# ====================================================== FACT - TIL ================================================ #

bot.deque_list = []
bot.counter = 0
bot.counter_fact = 0

@bot.command(name='facts', pass_context=True)
async def send_fact(ctx):
    bot.deque_list = await set_fact()
    bot.counter_fact += 1
    if bot.counter_fact >= len(bot.deque_list):
        bot.counter_fact = 0
    await ctx.send(f"{bot.deque_list[bot.counter_fact][0]}\n"
                   f"{bot.deque_list[bot.counter_fact][1]}")


async def set_fact():
    epoch = time.time()
    fact_at = str(int(epoch) - 129600 * 10)
    async with aiohttp.ClientSession() as session:
        url = "http://api.pushshift.io/reddit/submission/search?subreddit=todayilearned&score=>10000" \
              "&over_18='false'&sort_type=score&after=" + fact_at + "&sort=desc"
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_facts = []
            for i in data["data"]:
                list_of_facts.append([i["title"], i['url']])
            return list_of_facts


# ========================================== NEWS ================================================================== #

bot.deque_list_news = []
bot.counter_news = 0
@bot.command(name='news', pass_context=True)
async def send_news(ctx):
    bot.deque_list_news = await set_news()
    if bot.counter_news >= len(bot.deque_list_news):
        bot.counter_news = 0
    bot.counter_news += 2
    await ctx.send(
        f"{bot.counter_news - 1}. {bot.deque_list_news[bot.counter_news - 1][0]}\n"
        f"Source: {bot.deque_list_news[bot.counter_news - 1][1]}\n"
        f"{bot.counter_news}. {bot.deque_list_news[bot.counter_news][0]}\n"
        f"Source: {bot.deque_list_news[bot.counter_news][1]}")


async def set_news():
    epoch = time.time()
    news_at = int(epoch) - 129600 * 4
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=worldnews&score=>1000&after=" + str(
        news_at) + "&sort_by=score"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_news = []
            for i in data["data"]:
                list_of_news.append([i["title"], i['url']])
            return list_of_news


# ================================================ PROGRAMMING HUMOR (MEMES) ======================================== #
bot.deque_list_p_memes = []
bot.counter_p_memes = 0


@bot.command(name='programming_memes', pass_context=True)
async def send_p_memes(ctx):
    bot.deque_list_p_memes = await set_p_memes()
    if bot.counter_p_memes >= len(bot.deque_list_p_memes):
        bot.counter_p_memes = 0
    bot.counter_p_memes += 1
    await ctx.send(
        f"{bot.counter_p_memes}. {bot.deque_list_p_memes[bot.counter_p_memes][0]}\n"
        f"Source: {bot.deque_list_p_memes[bot.counter_p_memes][1]}")


async def set_p_memes():
    epoch = time.time()
    ph_at = int(epoch) - 129600 * 6
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=ProgrammerHumor&score=>1000" \
          "&sort_by=score&sort=desc&after=" + str(ph_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_p_memes = []
            for i in data["data"]:
                list_of_p_memes.append([i["title"], i['url']])
            return list_of_p_memes


# ================================================= HISTORY MEMES ================================================== #
bot.deque_list_h_memes = []
bot.counter_h_memes = 0


@bot.command(name='history_memes', pass_context=True)
async def send_h_memes(ctx):
    bot.deque_list_h_memes = await set_h_memes()
    if bot.counter_h_memes >= len(bot.deque_list_h_memes):
        bot.counter_h_memes = 0
    bot.counter_h_memes += 1
    await ctx.send(
        f"{bot.counter_h_memes}. {bot.deque_list_h_memes[bot.counter_h_memes][0]}\n"
        f"Source: {bot.deque_list_h_memes[bot.counter_h_memes][1]}")


async def set_h_memes():
    epoch = time.time()
    h_at = int(epoch) - 129600 * 6
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=HistoryMemes&score=>3000" \
          "&sort_by=score&sort=desc&after=" + str(h_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_h_memes = []
            for i in data["data"]:
                list_of_h_memes.append([i["title"], i['url']])
            return list_of_h_memes


# ================================================ MEMES (Misc) ===================================================== #
bot.deque_list_memes = []
bot.counter_memes = 0


@bot.command(name='memes', pass_context=True)
async def send_memes(ctx):
    bot.deque_list_memes = await set_memes()
    if bot.counter_memes >= len(bot.deque_list_memes):
        bot.counter_memes = 0
    bot.counter_memes += 1
    await ctx.send(
        f"{bot.counter_memes}. {bot.deque_list_memes[bot.counter_memes][0]}\n"
        f"Source: {bot.deque_list_memes[bot.counter_memes][1]}")


async def set_memes():
    epoch = time.time()
    meme_at = int(epoch) - 129600 * 15
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=Memes&score=>5000" \
          "&sort_by=score&sort=desc&after=" + str(meme_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_memes = []
            for i in data["data"]:
                list_of_memes.append([i["title"], i['url']])
            return list_of_memes


# ================================================ EVIL BUILDINGS ================================================= #

bot.deque_list_eb = []
bot.counter_eb = 0


@bot.command(name='evil_buildings', pass_context=True)
async def send_eb(ctx):
    bot.deque_list_eb = await set_eb()
    if bot.counter_eb >= len(bot.deque_list_eb):
        bot.counter_eb = 0
    bot.counter_eb += 1
    await ctx.send(f"Source: {bot.deque_list_eb[bot.counter_eb][1]}")


async def set_eb():
    epoch = time.time()
    eb_at = int(epoch) - 129600 * 12
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=evilbuildings&score=>500" \
          "&sort_by=score&sort=desc&after=" + str(eb_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_evil_buildings = []
            for i in data["data"]:
                list_of_evil_buildings.append([i["title"], i['url']])
            return list_of_evil_buildings


# ================================================= AWW ========================================================== #

bot.deque_list_aww = []
bot.counter_aww = 0


@bot.command(name='aww', pass_context=True)
async def send_aww(ctx):
    bot.deque_list_aww = await set_aww()
    if bot.counter_aww >= len(bot.deque_list_aww):
        bot.counter_aww = 0
    bot.counter_aww += 1
    await ctx.send(
        f"{bot.counter_aww}. {bot.deque_list_aww[bot.counter_aww][0]}\n"
        f"Source: {bot.deque_list_aww[bot.counter_aww][1]}")


async def set_aww():
    epoch = time.time()
    aww_at = int(epoch) - 129600 * 10
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=aww&score=>5000" \
          "&sort_by=score&sort=desc&after=" + str(aww_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_data = []
            for i in data["data"]:
                list_of_data.append([i["title"], i['url']])
            return list_of_data


# ======================================DATA is LIT =============================================================== #

bot.deque_list_data = []
bot.counter_data = 0


@bot.command(name='data_is_lit', pass_context=True)
async def send_data_is_lit(ctx):
    bot.deque_list_data = await set_data_is_lit()
    if bot.counter_data >= len(bot.deque_list_data):
        bot.counter_data = 0
    bot.counter_data += 1
    await ctx.send(
        f"{bot.counter_data}. {bot.deque_list_data[bot.counter_data][0]}\n"
        f"Source: {bot.deque_list_data[bot.counter_data][1]}")


async def set_data_is_lit():
    epoch = time.time()
    data_at = int(epoch) - 129600 * 5
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=dataisbeautiful&score=>1000" \
          "&sort_by=score&sort=desc&after=" + str(data_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_data = []
            for i in data["data"]:
                list_of_data.append([i["title"], i['url']])
            return list_of_data


# ====================================== MAPS are LIT ============================================================= #
bot.deque_list_map = []
bot.counter_map = 0


@bot.command(name='maps_are_lit', pass_context=True)
async def send_map(ctx):
    bot.deque_list_map = await set_map()
    if bot.counter_map >= len(bot.deque_list_map):
        bot.counter_map = 0
    bot.counter_map += 1
    await ctx.send(
        f"{bot.counter_map}. {bot.deque_list_map[bot.counter_map][0]}\n"
        f"Source: {bot.deque_list_map[bot.counter_map][1]}")


async def set_map():
    epoch = time.time()
    map_at = int(epoch) - 129600 * 12
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=MapPorn&score=>1000" \
          "&sort_by=score&sort=desc&after=" + str(map_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_maps = []
            for i in data["data"]:
                list_maps.append([i["title"], i['url']])
            return list_maps


# =================================== EARTH is LIT ================================================================ #

bot.deque_list_earth = []
bot.counter_earth = 0


@bot.command(name='earth_is_lit', pass_context=True)
async def send_earth(ctx):
    bot.deque_list_earth = await set_earth()
    if bot.counter_earth >= len(bot.deque_list_earth):
        bot.counter_earth = 0
    bot.counter_earth += 1
    await ctx.send(
        f"{bot.counter_earth}. {bot.deque_list_earth[bot.counter_earth][0]}\n"
        f"Source: {bot.deque_list_earth[bot.counter_earth][1]}")


async def set_earth():
    epoch = time.time()
    ep_at = int(epoch) - 129600 * 12
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=EarthPorn&score=>1000" \
          "&sort_by=score&sort=desc&after=" + str(ep_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_earth_images = []
            for i in data["data"]:
                list_earth_images.append([i["title"], i['url']])
            return list_earth_images


# ======================================================= WALLPAPERS ============================================ #

bot.deque_list_wp = []
bot.counter_wp = 0


@bot.command(name='wallpapers', pass_context=True)
async def send_wallpapers(ctx):
    bot.deque_list_wp = await set_wallpapers()
    if bot.counter_wp >= len(bot.deque_list_wp):
        bot.counter_wp = 0
    bot.counter_wp += 1
    await ctx.send(
        f"{bot.counter_wp}. {bot.deque_list_wp[bot.counter_wp][0]}\n"
        f"Source: {bot.deque_list_wp[bot.counter_wp][1]}")


async def set_wallpapers():
    epoch = time.time()
    wp_at = int(epoch) - 129600 * 12
    url = "http://api.pushshift.io/reddit/search/submission/?subreddit=wallpapers&score=>200" \
          "&sort_by=score&sort=desc&after=" + str(wp_at)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            list_of_wallpapers = []
            for i in data["data"]:
                list_of_wallpapers.append([i["title"], i['url']])
            return list_of_wallpapers


# ======================================== WEATHER ============================================================= #


@bot.command(name='weather', pass_context=True)
async def send_weather(ctx, *, name):
    store_weather_data = await produce_weather_data(name=name)
    embed = discord.Embed(
        title=f"Weather Data for {name}", color=discord.Color.blurple())
    if len(store_weather_data) != 0:
        current_temp = round(
            (store_weather_data["current_temperature"] - 273.15), 4)
        min_temp = round((store_weather_data["minimum Temperature"] - 273.15),
                         4)
        max_temp = round((store_weather_data["maximum Temperature"] - 273.15),
                         4)
        current_pressure = store_weather_data["current_pressure"]
        current_humidity = store_weather_data["current_humidity"]
        weather_description = store_weather_data["weather_description"]
        wind_speed = store_weather_data["wind speed"]
        cloudiness = store_weather_data["cloudiness"]
        timezone = store_weather_data["timezone"]
        sunrise_time = datetime.datetime.utcfromtimestamp(
            store_weather_data["sunrise time"] +
            timezone).strftime('%d-%m-%Y %H:%M:%S')
        sunset_time = datetime.datetime.utcfromtimestamp(
            store_weather_data["sunset time"] +
            timezone).strftime('%d-%m-%Y %H:%M:%S')

        embed.add_field(
            name="Current Temperature: ",
            value=f"{current_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Minimum Temperature: ",
            value=f"{min_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Maximum Temperature: ",
            value=f"{max_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Atmospheric Pressure: ",
            value=f"{current_pressure} hPa",
            inline=False)
        embed.add_field(
            name="Humidity: ", value=f"{current_humidity}%", inline=False)
        embed.add_field(
            name="Weather Description: ",
            value=f"{weather_description}",
            inline=False)
        embed.add_field(
            name="Cloudiness: ", value=f"{cloudiness}%", inline=False)
        embed.add_field(
            name="Wind Speed: ", value=f"{wind_speed} m/sec", inline=False)
        embed.add_field(
            name="Sunrise Time: ", value=f"{sunrise_time}", inline=False)
        embed.add_field(
            name="Sunrise Time: ", value=f"{sunset_time}", inline=False)
        embed.set_thumbnail(url="https://apps-static.athom.com/nu.baretta.openweathermap/0.0.18/assets/images/large.png")
        await ctx.send(embed=embed)

    else:
        await ctx.send("City Not Found")


@bot.command(name='weather_zip', pass_context=True)
async def send_weather(ctx, *, zip_code):
    # Enter zip code in the format = {zip code},{country code}
    store_weather_data = await produce_weather_data(zip_code=zip_code)
    embed = discord.Embed(
        title=f"Weather Data for {zip_code}", color=discord.Color.blurple())
    if len(store_weather_data) != 0:
        current_temp = round(
            (store_weather_data["current_temperature"] - 273.15), 4)
        min_temp = round((store_weather_data["minimum Temperature"] - 273.15),
                         4)
        max_temp = round((store_weather_data["maximum Temperature"] - 273.15),
                         4)
        current_pressure = store_weather_data["current_pressure"]
        current_humidity = store_weather_data["current_humidity"]
        weather_description = store_weather_data["weather_description"]
        wind_speed = store_weather_data["wind speed"]
        cloudiness = store_weather_data["cloudiness"]
        timezone = store_weather_data["timezone"]
        sunrise_time = datetime.datetime.utcfromtimestamp(
            store_weather_data["sunrise time"] +
            timezone).strftime('%d-%m-%Y %H:%M:%S')
        sunset_time = datetime.datetime.utcfromtimestamp(
            store_weather_data["sunset time"] +
            timezone).strftime('%d-%m-%Y %H:%M:%S')

        embed.add_field(
            name="Current Temperature: ",
            value=f"{current_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Minimum Temperature: ",
            value=f"{min_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Maximum Temperature: ",
            value=f"{max_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Atmospheric Pressure: ",
            value=f"{current_pressure} hPa",
            inline=False)
        embed.add_field(
            name="Humidity: ", value=f"{current_humidity}%", inline=False)
        embed.add_field(
            name="Weather Description: ",
            value=f"{weather_description}",
            inline=False)
        embed.add_field(
            name="Cloudiness: ", value=f"{cloudiness}%", inline=False)
        embed.add_field(
            name="Wind Speed: ", value=f"{wind_speed} m/sec", inline=False)
        embed.add_field(
            name="Sunrise Time: ", value=f"{sunrise_time}", inline=False)
        embed.add_field(
            name="Sunrise Time: ", value=f"{sunset_time}", inline=False)
        embed.set_thumbnail(url="https://apps-static.athom.com/nu.baretta.openweathermap/0.0.18/assets/images/large.png")
        await ctx.send(embed=embed)

    else:
        await ctx.send("City Not Found")


@bot.command(name='weather_geoloc', pass_context=True)
async def send_weather(ctx, lat, long):
    store_weather_data = await produce_weather_data(lat=lat, long=long)
    embed = discord.Embed(
        title=f"Weather Data for {lat},{long}", color=discord.Color.blurple())
    if len(store_weather_data) != 0:
        current_temp = round(
            (store_weather_data["current_temperature"] - 273.15), 6)
        min_temp = round((store_weather_data["minimum Temperature"] - 273.15),
                         6)
        max_temp = round((store_weather_data["maximum Temperature"] - 273.15),
                         6)
        current_pressure = store_weather_data["current_pressure"]
        current_humidity = store_weather_data["current_humidity"]
        weather_description = store_weather_data["weather_description"]
        wind_speed = store_weather_data["wind speed"]
        cloudiness = store_weather_data["cloudiness"]
        timezone = store_weather_data["timezone"]
        sunrise_time = datetime.datetime.utcfromtimestamp(
            store_weather_data["sunrise time"] +
            timezone).strftime('%d-%m-%Y %H:%M:%S')
        sunset_time = datetime.datetime.utcfromtimestamp(
            store_weather_data["sunset time"] +
            timezone).strftime('%d-%m-%Y %H:%M:%S')

        embed.add_field(
            name="Current Temperature: ",
            value=f"{current_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Minimum Temperature: ",
            value=f"{min_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Maximum Temperature: ",
            value=f"{max_temp} Celsius",
            inline=False)
        embed.add_field(
            name="Atmospheric Pressure: ",
            value=f"{current_pressure} hPa",
            inline=False)
        embed.add_field(
            name="Humidity: ", value=f"{current_humidity}%", inline=False)
        embed.add_field(
            name="Weather Description: ",
            value=f"{weather_description}",
            inline=False)
        embed.add_field(
            name="Cloudiness: ", value=f"{cloudiness}%", inline=False)
        embed.add_field(
            name="Wind Speed: ", value=f"{wind_speed} m/sec", inline=False)
        embed.add_field(
            name="Sunrise Time: ", value=f"{sunrise_time}", inline=False)
        embed.add_field(
            name="Sunrise Time: ", value=f"{sunset_time}", inline=False)
        embed.add_field(name="Timezone: ", value=f"{timezone}", inline=False)
        embed.set_thumbnail(url="https://apps-static.athom.com/nu.baretta.openweathermap/0.0.18/assets/images/large.png")
        await ctx.send(embed=embed)
        
    else:
        await ctx.send("City Not Found")


@bot.command(name='weather_nearby')
async def send_weather(ctx, lat, long, count):
    store_weather_data = await produce_weather_data(
        lat=lat, long=long, count=count)
    embed = discord.Embed(title="Weather of nearby places",
                          description='Weather data from cities laid within definite circle'
                                      ' that is specified by center point (lat, long) and expected' \
                                      ' number of cities (count) around this point.' \
                                      ' The default number of cities is 10, the maximum is 50.',
                          color=discord.Color.blurple())
    for i in store_weather_data:
        embed.add_field(
            name=f"{i['name']} | Coordinates: {i['coord']}",
            value=
            f"Current Temperature: {round((i['current_temperature'] - 273.15), 6)}\n"
            f"Min Temp: {round((i['minimum_temperature'] - 273.15), 6)} C"
            f" | Max Temp: {round((i['maximum_temperature'] - 273.15), 6)} C\n"
            f"Weather Description: {i['weather_description']} | Cloudiness: {i['cloudiness']}%\n"
            f"Current Pressure: {i['current_pressure']}hPa | Current Humidity: {i['current_humidity']}%\n"
            f"Wind Speed: {i['wind_speed']}m/sec",
            inline=False)
    embed.set_thumbnail(url="https://apps-static.athom.com/nu.baretta.openweathermap/0.0.18/assets/images/large.png")        
    await ctx.send(embed=embed)


async def produce_weather_data(name=None,
                               lat=None,
                               long=None,
                               zip_code=None,
                               count=None):
    async with aiohttp.ClientSession() as session:
        # API key here
        api_key = api_key_weathermap
        # This outer if-else is for cities laid within definite circle
        # that is specified by center point ('lat', 'lon') and expected number of cities ('cnt')
        if count is None:

            # Querying place by name
            if name is not None:
                url = "http://api.openweathermap.org/data/2.5/weather?q=" + name + "&APPID=" + api_key

            # Querying place by Latitude and Longitude
            elif lat is not None and long is not None:
                url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + long + "&APPID=" + api_key

            # Querying place by zip code
            elif zip is not None:
                url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + "&APPID=" + api_key
            async with session.get(url) as resp:
                data = await resp.json()
                weather_data = {}
                if data["cod"] != "404":
                    # accessing value of temp inside of main and storing
                    # in the dictionary weather_data
                    weather_data["current_temperature"] = data["main"]["temp"]
                    # accessing value of pressure inside of main
                    weather_data["current_pressure"] = data["main"]["pressure"]
                    # accessing value of humidity inside of main
                    weather_data["current_humidity"] = data["main"]["humidity"]
                    weather_data["minimum Temperature"] = data['main'][
                        'temp_min']
                    weather_data["maximum Temperature"] = data["main"][
                        'temp_max']
                    weather_data["wind speed"] = data["wind"]["speed"]
                    weather_data["cloudiness"] = data["clouds"]["all"]
                    weather_data["sunrise time"] = data["sys"]["sunrise"]
                    weather_data["sunset time"] = data["sys"]["sunset"]
                    weather_data["timezone"] = data["timezone"]
                    weather_data["name"] = data["name"]
                    weather_data["coord"] = data["coord"]

                    weather_data["weather_description"] = data["weather"][0][
                        "description"]
                    return weather_data
        else:
            url = "http://api.openweathermap.org/data/2.5/find?lat=" + lat +\
                  "&lon=" + long + "&cnt=" + count + "&APPID=" + api_key_weathermap
            async with session.get(url) as resp:
                data = await resp.json()
                weather_data = []
                if data["cod"] != "404":
                    for i in data["list"]:
                        name = i['name']
                        coord = i['coord']
                        current_temperature = i["main"]["temp"]

                        current_pressure = i["main"]["pressure"]

                        current_humidity = i["main"]["humidity"]

                        minimum_temperature = i['main']['temp_min']

                        maximum_temperature = i["main"]['temp_max']

                        wind_speed = i["wind"]["speed"]

                        cloudiness = i["clouds"]["all"]

                        weather_description = i["weather"][0]["description"]

                        weather_data.append({
                            "name":
                            name,
                            "coord":
                            coord,
                            "current_temperature":
                            current_temperature,
                            "current_pressure":
                            current_pressure,
                            "current_humidity":
                            current_humidity,
                            "minimum_temperature":
                            minimum_temperature,
                            "maximum_temperature":
                            maximum_temperature,
                            "wind_speed":
                            wind_speed,
                            "cloudiness":
                            cloudiness,
                            "weather_description":
                            weather_description
                        })
                return weather_data


# ======================================== SPACE and ISS =========================================================== #


@bot.command(name='people_in_space', pass_context=True)
async def get_iss_data_people(ctx):
    list_of_people, num_of_people = await set_iss_data_people()
    embed = discord.Embed(
        title=f"Number of people in the space = {num_of_people}",
        colour=discord.Color.blue())
    for person in list_of_people:
        embed.add_field(name=person, value="--------", inline=False)
    await ctx.send(embed=embed)
    # await ctx.send(ctx.message.channel, embed=embed)for writing channel name at the top at the top


@bot.command(name='iss_position', pass_context=True)
async def get_iss_data_position(ctx):
    timestamp, iss_position = await set_iss_data_position()
    localtime = datetime.datetime.fromtimestamp(timestamp).strftime(
        '%d-%m-%Y %H:%M:%S')
    utctime = datetime.datetime.utcfromtimestamp(timestamp).strftime(
        '%d-%m-%Y %H:%M:%S')
    embed = discord.Embed(
        title=f"ISS position: ", color=discord.Color.blurple())
    embed.add_field(
        name=f'At current Time: ',
        value=f'Local time: {localtime} | UTC time: {utctime}',
        inline=False)
    embed.add_field(
        name=f'Coordinates: ',
        value=
        f'Longitude: {iss_position["longitude"]} | Latitude: {iss_position["latitude"]}',
        inline=False)
    await ctx.send(embed=embed)


@bot.command(name='iss_pass_times', pass_context=True)
async def get_iss_data_pass_times(ctx, latitude, longitude, altitude):
    passes = await set_iss_data_pass_times(latitude, longitude, altitude)
    embed = discord.Embed(
        title=
        "ISS passes overhead at current location at following time and dates",
        color=discord.Color.blurple())
    for count, i in enumerate(passes, 1):
        rise_time = datetime.datetime.fromtimestamp(
            i["risetime"]).strftime('%d-%m-%Y %H:%M:%S')
        embed.add_field(
            name=f'{count}. Pass Time: {rise_time}',
            value=f'Duration: {i["duration"]} seconds',
            inline=False)
    await ctx.send(embed=embed)


async def set_iss_data_people():
    async with aiohttp.ClientSession() as session:
        url_people = "http://api.open-notify.org/astros.json"
        async with session.get(url_people) as resp:
            iss_people_data = await resp.json()
            num_of_people = iss_people_data["number"]
            people = iss_people_data["people"]
            list_of_people = []
            for person in people:
                list_of_people.append(person['name'])
            return list_of_people, num_of_people


async def set_iss_data_position():
    async with aiohttp.ClientSession() as session:
        url = "http://api.open-notify.org/iss-now.json"
        async with session.get(url) as resp:
            iss_position_data = await resp.json()
            timestamp = iss_position_data["timestamp"]
            iss_position = iss_position_data["iss_position"]
            return timestamp, iss_position


async def set_iss_data_pass_times(latitude, longitude, altitude):
    async with aiohttp.ClientSession() as session:
        url = "http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude + "&alt=" + altitude + "&n=10"
        async with session.get(url) as resp:
            iss_pass_time_data = await resp.json()
            passes = iss_pass_time_data["response"]
            return passes

@bot.command(name='spacex_launch')
async def get_launch_details(ctx, param):
    launch_data = await launch_details(param)
    if param == 'latest':
        embed = discord.Embed(title=f"Latest SpaceX Launch Details",
                              description=f"{launch_data['details']}",
                              color=discord.Color.blurple(), inline=False)
        embed.add_field(name=f"Flight Number and Mission Name",
                        value=f"{launch_data['flight_number']} | {launch_data['mission_name']}", inline=False)
        embed.add_field(name=f"Launch Date and Time",
                        value=f"{datetime.datetime.fromtimestamp(launch_data['launch_date_unix']).strftime('%d-%m-%Y %H:%M:%S')}",
                        inline=False)
        embed.add_field(name=f"Rocket Used", value=f"{launch_data['rocket']['rocket_name']}", inline=False)
        embed.add_field(name=f"Launch Site", value=f"{launch_data['launch_site']['site_name_long']}", inline=False)
        embed.add_field(name=f"Launch Success status", value=f"{launch_data['launch_success']}", inline=False)
        embed.add_field(name=f"News article", value=f"{launch_data['links']['article_link']}", inline=False)
        embed.add_field(name="Video Link", value=f"{launch_data['links']['video_link']}", inline=False)
        embed.set_thumbnail(url='https://www.pngix.com/pngfile/middle/154-1548854_the-spacex-private-launch-site-is-a-space.png')
    elif param == 'next':
        embed = discord.Embed(title=f"Upcoming SpaceX Launch Details",
                              description=f"{launch_data['details']}",
                              color=discord.Color.blurple(), inline=False)
        embed.add_field(name=f"Flight Number and Mission Name",
                        value=f"{launch_data['flight_number']} | {launch_data['mission_name']}", inline=False)
        embed.add_field(name=f"Launch Date and Time",
                        value=f"{datetime.datetime.fromtimestamp(launch_data['launch_date_unix']).strftime('%d-%m-%Y %H:%M:%S')}", inline=False)
        embed.add_field(name=f"Rocket Used", value=f"{launch_data['rocket']['rocket_name']}", inline=False)
        embed.add_field(name=f"Launch Site", value=f"{launch_data['launch_site']['site_name_long']}", inline=False)
        embed.set_thumbnail(
            url='https://www.pngix.com/pngfile/middle/154-1548854_the-spacex-private-launch-site-is-a-space.png')
    await ctx.send(embed=embed)


async def launch_details(launch_type):
    async with aiohttp.ClientSession() as session:
        if launch_type == 'latest':
            url = "https://api.spacexdata.com/v3/launches/latest"
        elif launch_type == 'next':
            url = "https://api.spacexdata.com/v3/launches/next"
        async with session.get(url) as resp:
            data = await resp.json()
            return data


@bot.command(name='apod')
async def get_apod_data(ctx, param=None):
    apod_data = await apod(param)
    embed = discord.Embed(title=f"Astronomy Picture Of the Day (APOD) by NASA",
                          description=f"{apod_data['explanation']}",
                          color=discord.Color.blurple(), inline=False)
    embed.add_field(name="Picture Title", value=f"{apod_data['title']}", inline=False)
    embed.add_field(name="HD Image url", value=f"{apod_data['hdurl']}", inline=False)
    embed.add_field(name="Dated:", value=f"{apod_data['date']}", inline=False)
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1074223648/nasalogo_twitter_400x400.jpg")
    embed.set_image(url=f"{apod_data['url']}")
    await ctx.send(embed=embed)


async def apod(date=None):
    async with aiohttp.ClientSession() as session:
        if date is None:
            url = "https://api.nasa.gov/planetary/apod?api_key=" + nasa_api_key
        elif date is not None:
            url = "https://api.nasa.gov/planetary/apod?api_key=" + nasa_api_key + "&date=" + date
        async with session.get(url) as resp:
            data = await resp.json()
            return data

# ============================================ FOREX and CURRENCY CONVERTER ========================================== #


@bot.command(name='forex', pass_context=True)
async def get_exchange_data(ctx, base=None, *args):
    if base:
        rates = await set_exchange_data(base, *args)
        if not args:
            embed = discord.Embed(
                title=f'Latest Foreign Exchange Rates for {base}',
                color=discord.Color.blurple())
            for k, v in rates.items():
                embed.add_field(name=f'{k}', value=f"{v}", inline=False)
        else:
            embed = discord.Embed(
                title=
                f'Latest Foreign Exchange Rates for {base} to {list(args)}',
                color=discord.Color.blurple())
            for k, v in rates.items():
                embed.add_field(name=f'{k}', value=f'{v}', inline=False)
        await ctx.send(embed=embed)
    else:
        embed_global.set_field_at(
            index=0, name="Enter the required params", value="-------")
        await ctx.send(embed=embed_global)


@bot.command(name='convert', pass_context=True)
async def currency_converter(ctx, amount=None, base=None, *args):
    if base and amount:
        # args are the target currencies for conversion
        # amount is the amount to be converted
        if not args:
            embed_global.set_field_at(
                index=0, name="Enter the required params", value="-------")
        else:
            rates = await set_exchange_data(base, *args)
            embed = discord.Embed(
                title=f'Currency Conversion from {base} to {list(args)}',
                description=f"{amount} {base} equals to: ",
                color=discord.Color.blurple())
            for k, v in rates.items():
                amt = float(v)
                embed.add_field(
                    name=f'{k}', value=f'{amt * float(amount)}', inline=False)
            await ctx.send(embed=embed)
    else:
        embed_global.set_field_at(
            index=0, name="Enter the required params", value="-------")
        await ctx.send(embed=embed_global)


async def set_exchange_data(base, *args):
    async with aiohttp.ClientSession() as session:
        if not args:
            url = 'https://api.ratesapi.io/api/latest?base=' + base
            async with session.get(url) as resp:
                data = await resp.json()
                rates = data["rates"]
                return rates
        else:
            symbols = list(args)
            symbols_joined = ",".join(symbols)
            url = "https://api.ratesapi.io/api/latest?base=" + base + "&symbols=" + symbols_joined
            async with session.get(url) as resp:
                data = await resp.json()
                rates = data["rates"]
                return rates


# =============================================== CRYPTO CURRENCY =================================================== #


@bot.command(name='coin_info', pass_context=True)
async def get_coin_info(ctx, coin=None, target_currency=None):
    if coin and target_currency:
        data = await set_coin_info(coin, target_currency)
        embed = discord.Embed(
            title=f'**Coin Info for {data["symbol"]}**',
            description=
            '*[Click here](https://coinlib.io/coins)* for more info on all major cryptocurrencies',
            inline=False,
            color=discord.Colour.dark_blue())
        embed.add_field(
            name=f'{data["name"]} ({data["show_symbol"]})',
            value=f'{data["show_symbol"]}',
            inline=False)
        embed.add_field(
            name=f'Price: ',
            value=f'{round(float(data["price"]), 4)} {target_currency}',
            inline=False)
        embed.add_field(
            name=f'Market Cap: ',
            value=f'{round(float(data["market_cap"]), 4)} {target_currency}',
            inline=False)
        embed.add_field(
            name=f'Total Trade Volume over 24h in {target_currency}: ',
            value=
            f'{round(float(data["total_volume_24h"]), 4)} {target_currency}',
            inline=False)
        embed.add_field(
            name=f'Lowest Price in last 24h: ',
            value=f'{round(float(data["low_24h"]), 4)} {target_currency}',
            inline=False)
        embed.add_field(
            name=f'Highest Price in last 24h: ',
            value=f'{round(float(data["high_24h"]), 4)} {target_currency}',
            inline=False)
        embed.add_field(
            name=f'Price change in last 1h: ',
            value=f'{data["delta_1h"]}%',
            inline=False)
        embed.add_field(
            name=f'Price change in last 24h: ',
            value=f'{data["delta_24h"]}%',
            inline=False)
        embed.add_field(
            name=f'Price change in last 7d: ',
            value=f'{data["delta_7d"]}%',
            inline=False)
        embed.add_field(
            name=f'Price change in last 30d: ',
            value=f'{data["delta_30d"]}%',
            inline=False)
        embed.set_thumbnail(
            url='http://images.newindianexpress.com/uploads/user/imagel'
            'ibrary/2018/6/29/w600X300/cryptocurrency_001.jpg')
        await ctx.send(embed=embed)
    else:
        embed_global.set_field_at(
            index=0, name="Enter the required params", value="-------")
        await ctx.send(embed=embed_global)


@bot.command(name='coin_exchanges')
async def get_coin_exchange(ctx, coin, target_currency):
    data = await set_coin_info(coin, target_currency)
    embed = discord.Embed(
        title=f"**Top 3 markets and their exchanges for {coin}**",
        description=
        f"*[Click here](https://coinlib.io/exchanges)* for more info on all exchanges",
        color=discord.Color.dark_blue())
    for i in data["markets"]:
        value = ""
        for j in i["exchanges"]:
            value += f"Exchange Name: {j['name']} \nTotal Trade Volume over 24h in {i['symbol']}: {j['volume_24h']} \n" \
                f"Price: {j['price']} {i['symbol']} \n\n"
        embed.add_field(
            name=f'Price of {coin} in {i["symbol"]}: {i["price"]} \n'
            f'Top {len(i["exchanges"])} exchanges for trading the coin in {i["symbol"]}: ',
            value=value,
            inline=False)
    await ctx.send(embed=embed)


@bot.command(name='coin_list')
async def get_coin_list(ctx, target_currency, order):
    # order is the order of sorting(by rank_desc or volume_desc)
    if order.lower() == "rank":
        coin_list = await set_coin_list(target_currency, order="")
        embed = discord.Embed(
            title="Top 20 Cryptocurrencies by rank",
            color=discord.Color.dark_blue())
        for count, i in enumerate(coin_list[:20], 1):
            embed.add_field(
                name=
                f"{count}. {i['name']} ({i['symbol']}) - Rank: {i['rank']} - Price: {round(float(i['price']), 8)} {target_currency}\n",
                value=
                f"Trade Volume over 24h: {round(float(i['volume_24h']), 4)} {target_currency}\n",
                inline=False)
            # f"Market Cap: {round(float(i['market_cap']), 4)} {target_currency}\n", inline=False)
        await ctx.send(embed=embed)
    elif order.lower() == "volume":
        coin_list = await set_coin_list(target_currency, order="volume_desc")
        embed = discord.Embed(
            title="Top 20 Cryptocurrencies by volume",
            color=discord.Color.dark_blue(),
            inline=False)
        for count, i in enumerate(coin_list[:20], 1):
            embed.add_field(
                name=
                f"{count}. {i['name']} ({i['symbol']}) - Rank: {i['rank']} - Price: {round(float(i['price']), 4)} {target_currency}\n",
                value=
                f"Trade Volume over 24h: {round(float(i['volume_24h']), 4)} {target_currency}\n",
                inline=False)
            # f"Market Cap: {round(float(i['market_cap']), 4)} {target_currency}", inline=False)
        await ctx.send(embed=embed)


async def set_coin_info(coin, target_currency):
    async with aiohttp.ClientSession() as session:
        api_key = api_key_coinlib
        url = "https://coinlib.io/api/v1/coin?key=" + api_key + "&pref=" + target_currency + "&symbol=" + coin
        async with session.get(url) as resp:
            data = await resp.json()
            return data


async def set_coin_list(target_currency, order):
    async with aiohttp.ClientSession() as session:
        api_key = api_key_coinlib
        url = "https://coinlib.io/api/v1/coinlist?key=" + api_key + "&pref=" + target_currency + "&page=1&order=" + order
        async with session.get(url) as resp:
            data = await resp.json()
            return data["coins"]


# ============================= AIR QUALITY INDEX =========================================================== #


@bot.command(name="aqi")
async def get_aqi(ctx, lat=None, lon=None):
    data_aqi = await set_aqi(lat=lat, lon=lon)
    embed = discord.Embed(
        title="AQI data", color=discord.Color.dark_blue(), inline=False)
    aqi_ = data_aqi["data"]["aqi"]
    place = data_aqi["data"]["city"]["name"]
    place_url = data_aqi["data"]["city"]["url"]
    dominant_pollutant = data_aqi["data"]["dominentpol"]
    timestamp = data_aqi["data"]["time"]["s"]
    data_pollutants = data_aqi["data"]["iaqi"]

    # co_ = data_aqi["data"]["iaqi"]["co"]["v"]
    # no2_ = data_aqi["data"]["iaqi"]["no2"]["v"]
    # o3_ = data_aqi["data"]["iaqi"]["o3"]["v"]
    # so2_ = data_aqi["data"]["iaqi"]["so2"]["v"]
    # pm_10 = data_aqi["data"]["iaqi"]["pm10"]["v"]
    # pm_25 = data_aqi["data"]["iaqi"]["pm25"]["v"]
    pollutants = ''
    for k, v in data_pollutants.items():
        pollutants += f"{k} {v} \n"
    embed.add_field(
        name=f"Place: {place} | AQI: {aqi_}",
        value=f"{place_url}",
        inline=False)
    embed.add_field(
        name=f"Dominant Pollutant: ",
        value=f"{dominant_pollutant}",
        inline=False)
    embed.add_field(name=f"Pollutants: ", value=pollutants, inline=False)
    embed.add_field(
        name=f"Data Generated At: ", value=f"{timestamp}", inline=False)
    embed.set_image(url='https://airmega.com/wp-content/uploads/2016/01/1.png')
    embed.set_thumbnail(url='https://aqicn.org/air/experiments/images/aqi.png')
    await ctx.send(embed=embed)


@bot.command(name="aqi_stations")
async def get_aqi_stations(ctx, *, name):
    nearby_list = await set_aqi(name=name)
    if nearby_list:
        embed = discord.Embed(
            title="Pollution Detection Stations in the city",
            inline=False,
            color=discord.Color.blurple())
        for i in nearby_list:
            embed.add_field(
                name=f"Place: {i['name']} | AQI: {i['AQI']} ",
                value=f"Coordinates: {i['geo_loc']}",
                inline=False)
        embed.set_image(
            url=
            'https://a.scpr.org/i/e88dad6837bf40214eb2234b461cfd10/136217-full.jpg'
        )
        embed.set_thumbnail(
            url='https://aqicn.org/air/experiments/images/aqi.png')
    else:
        embed = discord.Embed(
            title="Pollution Detection Stations in the city",
            description='Regret - No stations found in the place or near it!',
            color=discord.Color.blurple(),
            inline=False)
        embed.set_thumbnail(
            url='https://aqicn.org/air/experiments/images/aqi.png')
    await ctx.send(embed=embed)


async def set_aqi(lat=None, lon=None, name=None):
    async with aiohttp.ClientSession() as session:
        if lat is None and lon is None and name is None:
            api_key = api_key_aqi
            url = "https://api.waqi.info/feed/here/?token=" + api_key
            async with session.get(url) as resp:
                aqi_data = await resp.json()
                return aqi_data
        elif name is not None and lat is None and lon is None:
            api_key = api_key_aqi
            url = "https://api.waqi.info/search/?token=" + api_key + "&keyword=" + name
            async with session.get(url) as resp:
                aqi_data = await resp.json()
                nearby_list = []
                for i in aqi_data["data"]:
                    aqi = i["aqi"]
                    name = i["station"]["name"]
                    geo_loc = i["station"]["geo"]
                    nearby_list.append({
                        "name": name,
                        "geo_loc": geo_loc,
                        "AQI": aqi
                    })
                return nearby_list
        else:
            api_key = api_key_aqi
            url = "https://api.waqi.info/feed/geo:" + lat + ";" + lon + "/?token=" + api_key
            async with session.get(url) as resp:
                aqi_data = await resp.json()
                return aqi_data


# ============================= HAVE I BEEN PAWNED =========================================================== #


@bot.command(name="have_i_been_pawned")
async def pawned(ctx, account):
    breach_list = await haveibeenpawned(account)
    if breach_list:
        embed = discord.Embed(
            title="Have I been Pawned",
            description=
            'This command checks whether your account has been compromised in any data breach.'
            ' Unfortunately, your account has been breached in the past',
            color=discord.Color.blurple(),
            inline=False)
        for i in breach_list:
            embed.add_field(
                name=f"The account on the website which suffered Data breach",
                value=f"{i['Domain']}",
                inline=False)
            embed.add_field(
                name=f"Date of data breach of the account ",
                value=f"{i['BreachDate']}",
                inline=False)
            embed.add_field(
                name=f"Compromised Data",
                value=f"{i['DataClasses']}",
                inline=False)
            embed.add_field(
                name=f"----------", value=f"-----------", inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(name="Status of your account", description="_Checking for a data breach_")
        embed.add_field(name=f"Your account {account} has not been breached",
                        value="It is safe for now", inline=False)
        embed.set_thumbnail(url="https://haveibeenpwned.com/Content/Images/SocialLogo.png")
        await ctx.send(embed=embed)



async def haveibeenpawned(account):
    async with aiohttp.ClientSession() as session:
        url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + account
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                return None


# ============================= SHORTEN URL =============================================================== #


@bot.command(name='s_url')
async def get_shorten(ctx, url):
    response = await shorten(url)
    if 'result_url' in response:
        embed = discord.Embed(
            title='Shorten URL',
            description=
            "Enter a URL and the command will return a shortened URL",
            color=discord.Color.blurple(),
            inline=False)
        embed.add_field(
            name='Shortened URL:', value=f"{response['result_url']}")
        await ctx.send(embed=embed)
    else:
        embed_global.set_field_at(
            index=0, name=f"Error in the function call", value="---")
        await ctx.send(embed=embed_global)


async def shorten(long_url):
    async with aiohttp.ClientSession() as session:
        api_url = "https://hideuri.com/api/v1/shorten"
        data_dict = {'url': long_url}
        async with session.post(api_url, data=data_dict) as resp:
            data = await resp.json()
            return data



# A dictionary for keeping record of each user's newsletter sources
bot.sources = {}


@bot.command(name="news_sources")
async def news_sources(ctx, sources):
    user_id = ctx.author.id
    user_dict = {str(user_id): str(sources)}
    bot.sources.update(user_dict)
    await ctx.send("You have successfully saved sources for your newsletter")


@bot.command(name="newsletter")
async def get_newsletter_data_(ctx):
    user_id = ctx.author.id
    data = await newsletter_data_(bot.sources[str(user_id)])
    embed = discord.Embed(title="Newsletter",
                          description="You can find the list of sources to select from, at this URL: https://newsapi.org/sources",
                          inline=False)
    embed.add_field(name="A sharable link of the newsletter will be shortly delivered to your Inbox",
                    value="This link will contain top stories along with their urls from the sources you selected",
                    inline=False)
    embed.set_thumbnail(url="http://d6vsczyu1rky0.cloudfront.net/31605_b/wp-content/uploads/2016/07/Newsletter-logo.jpg")
    
    paste_text = ""
    paste_text_sl = ""
    for count, i in enumerate(data[:10], 1):
        embed.add_field(name=f"#{count} | URL: {i['url']}", value=f"{i['title']} | {i['description']}", inline=False)
    for count, i in enumerate(data, 1):
        paste_text = paste_text + f"#{count}. URL: {i['url']} | {i['title']} | {i['description']}\n\n"
        paste_text_sl = paste_text_sl + f"#{count}. URL: [{i['url']}]({i['url']}) | {i['title']} | {i['description']}\n\n"
    await ctx.send(embed=embed)
    paste_link_sl = await create_paste_short_lived(paste_text_sl)
    paste_link = await create_paste(paste_text)
    await ctx.author.send(f"Sharable Newsletter Links:\n"
                          f"Short Lived Link for Newsletter: {paste_link_sl}"
                          f"Never Expiring Link for Newsletter: {paste_link}")


async def newsletter_data_(sources):
    async with aiohttp.ClientSession() as session:
        url = "https://newsapi.org/v2/top-headlines?sources=" + sources + "&pageSize=20&apiKey=" + news_api_key
        async with session.get(url=url) as resp:
            data = await resp.json()
            return data['articles']


async def create_paste(paste_text):
    async with aiohttp.ClientSession() as session:
        params = {"api_dev_key": pastebin_api_key, "api_option": "paste",
                  "api_paste_code": paste_text}
        api_url = "https://pastebin.com/api/api_post.php"
        async with session.post(url=api_url, data=params) as resp:
            data = await resp.text()
            return data


async def create_paste_short_lived(paste_text):
    async with aiohttp.ClientSession() as session:
        params = {"format": "url", "content": paste_text, "lexer": "_markdown",
                  "expires": "604800", "filename": "newsletter"}
        api_url = "https://dpaste.de/api/"
        async with session.post(url=api_url, data=params) as resp:
            data = await resp.text()
            return data

pastebin_api_key = os.getenv("pastebin_api_key_secret")
news_api_key = os.getenv("news_api_key_secret")
nasa_api_key = os.getenv("nasa_api_key_secret")
api_key_aqi = os.getenv("api_key_aqi_secret")
client_ID = os.getenv("client_ID_secret")
api_key_coinlib = os.getenv("api_key_coinlib_sec")
api_key_weathermap = os.getenv("api_key_weathermap_sec")
token = os.getenv("token_sec")

keep_alive()
bot.run(token)
