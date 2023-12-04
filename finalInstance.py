#Import Class libraries needed
import discord
import os
import random
from ec2_metadata import ec2_metadata

#printing ec2 metadata info to ensure it is working correctly with the ec2 server
print(ec2_metadata.region)
print(ec2_metadata.instance_id)




#creation of object with two variables, one for the bot and other for the token to be passed through for security purposes
client = discord.Bot()
token = str(os.getenv('TOKEN'))


#function to show bot is functional and logged on
@client.event
async def on_ready():
    print("Logged in as bot {0.user}".format(client))


#Creation of function and local variables
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    choices = ("time","what is the downtime","downtime")

    #error checking before running conditionals
    while user_message not in choices:
        user_message = message.channel.send(f'Please ask for "downtime" or "time"' {username})

    #output,format{f} with brackets.
    print(f'Message {user_message} by {username} on {channel}')


    #client user is the bot, to ensure a return is made
    if message.author == client.user:
        return 

    #if conditional for certain channel variable
    if channel == "updates":
    if condition for the user message along with the client repsonse with else if statments
        if user_message.lower() == "downtime" or user_message.lower() == "what is the downtime":
            await message.channel.send(f'Downtime is set for 12/25! {username} Your EC2 Data: {ec2_metadata.region}') #format of string
            return
        elif user_message.lower() == "time":
            await message.channel.send(f'12am 12/25! {username}')

        #Returning instance data for the last conditional statement.
        elif user_message.lower() == "EC2 Data":
            await message.channel.send("Your instance data is" + ec2_metadata)

#Start execution by passing the token object in ec2 instance environment
client.run(token)