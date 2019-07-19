import discord

myID = '518690278002130945'

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		
	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))
		if(myID in message.content):
			await message.channel.send('Hi, @' + message.author.mention + '!')

if __name__ == "__main__":		
	client = MyClient()
	client.run('NTE4NjkwMjc4MDAyMTMwOTQ1.XTEAcQ.L6AIHAzuFXUtImRuAYYuYG-u4Bk')
