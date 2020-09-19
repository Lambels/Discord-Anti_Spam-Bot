from discord.ext import commands
import _user_class

client = commands.Bot(command_prefix='!')


@client.event
async def on_message(message):
    if isinstance(_user_class.User.check_if_typed(message), _user_class.User):
        x = _user_class.User.check_if_typed(message)
        x.messages.append(str(message.content.lower()))
        print(x.messages)
        if len(x.messages) == 6:
            if x.check(message) == True:
                await message.channel.purge(limit=1)
                x.messages.pop(0)
            else:
                print('28')
                x.messages.pop(0)
    else:
        inst = _user_class.User(message.author)
        _user_class.User.USER_LIST.append(inst)
        inst.messages.append(str(message.content.lower()))



client.run('TOKEN')
