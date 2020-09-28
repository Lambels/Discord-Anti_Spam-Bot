from discord.ext import commands
import _user_class
from datetime import datetime, timedelta

client = commands.Bot(command_prefix='!')


@client.event
async def on_message(message):
    if isinstance(_user_class.User.check_if_typed(message), _user_class.User):
        x = _user_class.User.check_if_typed(message)
        x.messages.append(str(message.content.lower()))
        x.set_time(datetime.now())
        if len(x.messages) == 6:
            if x.check(message) == True:
                await message.channel.purge(limit=1)
                x.messages.pop(0)
            else:
                x.messages.pop(0)
        if len(x.time) == 2:
            if x.check_timer() == True:
                await message.channel.purge(limit=1)
                x.time.pop(0)
            else:
                x.time.pop(0)
    else:
        inst = _user_class.User(message.author)
        _user_class.User.USER_LIST.append(inst)
        inst.messages.append(str(message.content.lower()))
        inst.set_time(datetime.now())



client.run('TOKEN')
