import discord 
import os
import asyncio
import sqlite3
from pydantic import BaseModel
import datetime

# task usage: !task create a cool hat 12:00 PM

class UserTasks(BaseModel):
    name: str
    task: dict



async def create_task(message):
    if message.content.startswith("!task"):
        task = message.content.split("!task")[1]
        time = datetime.utcnow() + datetime.timedelta(minutes=5)
        usertask = UserTasks(name=str(message.author), task={"task": task, "time": time})
        await message.channel.send(f"{task.name.split('#')[0]}, I will remind you to . . . {task}")
        

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith("!task"):
            await create_task(message)
            await message.channel.send("Task noted!")

def connect_to_discord():
    client = MyClient()
    client.run(os.getenv("token"))
connect_to_task_db()
connect_to_discord()


            

