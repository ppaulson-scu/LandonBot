import discord
import re

# Bot's Discord ID
myID = '518690278002130945'
filename_strikes = 'strikes.txt'

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		
	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))
		if myID in message.content:
			await message.channel.send('Hi, @' + message.author.mention + '!')
		elif '!' == message.content[0]:
			if '!strikes' in message.content:
				await message.channel.send('User has ' + str(get_strikes(get_user_id(message.content))) + ' strikes.')
			elif '!strike' in message.content:
				user_id = get_user_id(message.content)
				give_strike(user_id)
				

def give_strike(user):
	strikes = open(filename_strikes, 'r+')
	line = strikes.readline()
	while line != '':
		if line[:len(user)] != user:
			line = strikes.readline()
			continue
		else:
			numstrikes = int(line[-1:])
			if(numstrikes == 2):
				punish(user)
				numstrikes = 0
				print('User reset after punishment.')
			else:
				numstrikes += 1
				print('Strike added to user.')
			return numstrikes
	
	strikes.write(user + ' 1')
	print('User added to strikes DB.')
	strikes.close()
	return 1
	
def punish(user):
	print('User punished.')

def get_user_id(message):
	res = re.search('<@(|!)[0-9]+>', message)
	res = res.group(0)
	res = re.sub('!', '', res)
	print('Found UID ' + res + 'in message.')
	return res
	
if __name__ == "__main__":		
	client = MyClient()
	client.run('NTE4NjkwMjc4MDAyMTMwOTQ1.XTEAcQ.L6AIHAzuFXUtImRuAYYuYG-u4Bk')