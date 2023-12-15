#Import necessary libraries
import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

load_dotenv()

#printing ec2 metadata info to ensure it is working correctly with the ec2 server
print(ec2_metadata.region)
print(ec2_metadata.instance_id)




#creation of object with two variables, one for discord bot initialization and other one retrieving discord bot token from environment variables
client = discord.Client()
token = str(os.getenv('TOKEN'))


#bot login and function to show bot successful login
@client.event
async def on_ready():
    print("Logged in as bot {0.user}".format(client))


#Creation of function and local variables details of username,channel,and user_message
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    #output,format{f} with brackets logging the user's message details
    print(f'Message {user_message} by {username} on {channel}')


    #Client user is the bot, to ignore and return is made from the bot itself
    if message.author == client.user:
        return 

    #if conditional for 'updates' channel, checking conditions for specific user messages and bot responses. User query about downtime in the 'updates' channel
    if channel == "random":
    #if condition for the user message along with the client repsonse with else if statments
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'hello {username}') 
            return
        elif user_message.lower() == "update":
            await message.channel.send(f'Update in 2 hours {username}')

        elif user_message.lower() == "hello world":
            await message.channel.send(f'hello {username}')

        #User query for 'EC2 Data', responding query about EC2 instance data in the 'updates' channel. Retrieves and displays the region of the EC2 instance. Displays the public IP address of the EC2 instance. Shows the availability zone where the EC2 instance is located.
        elif user_message.lower() == "tell me about my server":
            await message.channel.send(f"""Your EC2 data:\nRegion: {ec2_metadata.region}\nIp address: {ec2_metadata.public_ipv4}\nZone: {ec2_metadata.availability_zone}\nServer instance: {ec2_metadata.instance_type}""")


        #if the user's message, when converted to lowercase, matches the word "bye". 
        elif user_message.lower() == "bye":
            await message.channel.send(f'Goodbye {username}')

#Start execution by passing the token object in ec2 instance environment
client.run(token)