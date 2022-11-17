from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Raimzhan", url="https://t.me/dubstepking")],
         [InlineKeyboardButton(
            "Alua", url="https://t.me/arxximm")]
    ])


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send YoutTube URL and download the video - easy!"
    await message.reply_text(helptxt)
