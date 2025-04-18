from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AUTH_CHANNELS, ADMIN
from pyrogram.errors import RPCError


async def get_fsub(client, message):
    rahul = await client.get_me()
    bot = client
    user_id = message.from_user.id
    not_joined = []

    for channel_id in AUTH_CHANNELS:
        try:
            member = await bot.get_chat_member(channel_id, user_id)
            if member.status == "kicked":
                await message.reply("**🚫 You are banned from using this bot**",
                                    reply_markup=InlineKeyboardMarkup(
                                        [[InlineKeyboardButton("Support", user_id=int(ADMIN))]]
                                    ))
                return False
            if member.status in ["left", "restricted"]:
                not_joined.append(channel_id)
        except RPCError:
            not_joined.append(channel_id)

    if not not_joined:
        return True

    buttons = []
    for index, channel_id in enumerate(not_joined, 1):
        try:
            chat = await bot.get_chat(channel_id)
            channel_link = chat.invite_link
            if not channel_link:
                raise ValueError("No invite link available")
            buttons.append(InlineKeyboardButton(f"🔰 Channel {index} 🔰", url=channel_link))
        except Exception as e:
            print(f"Error fetching channel data: {e}")
    tybutton = InlineKeyboardButton("🔄 Try Again", url=f"https://telegram.me/{rahul.username}?start=start")
    buttons.append(tybutton)
    formatted_buttons = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]

    await message.reply(
        f"{message.from_user.mention}, To use the bot, you must join our channel first."
        "The bot will not process any requests without joining.\n\n"
        "போட்டைப் பயன்படுத்த முதலில் எங்கள் சேனலில் சேர வேண்டும்."
        "பங்கேற்பு இல்லாமல் எந்த Request பாட் Process.",
        reply_markup=InlineKeyboardMarkup(formatted_buttons))
    return False
            
