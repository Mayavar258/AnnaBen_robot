import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Hey {message.from_user.mention} 🥰 Welcome to {message.chat.username} Happy to have here..❣️",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Hey {message.from_user.mention}, Have a Nice Day...❣️",chat_id=chatid)
	

