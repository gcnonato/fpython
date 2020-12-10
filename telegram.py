# -*- coding: utf-8 -*-
from decouple import config
from telethon import TelegramClient

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = config("TELEGRAM_API_ID")
api_hash = config("TELEGRAM_API_HASH")

client = TelegramClient("session_name", api_id, api_hash)
client.start()
# print(client.get_me().stringify())

# client.send_message('username', 'Hello! Talking to you from Telethon')
# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# client.download_profile_photo('me')
# messages = client.get_messages('username')
# messages[0].download_media()


def salvar_no_arquivo_contatos_telegram():
    traco = f'{"*"*70}'

    async def main():
        cont = 0
        with open("friends_user_telegram.txt", "w", encoding="utf-8") as _f:

            async for dialog in client.iter_dialogs():
                cont += 1
                print(dialog.name, "has ID", dialog.id)
                _f.write(f"{traco}\n")
                gravar = f"{cont} {dialog.name}-{dialog.id}"
                _f.write(gravar)
                _f.write(f"\n{traco}")

    print("Fim da gravação!")
    with client:
        client.loop.run_until_complete(main())


async def main():
    # Getting information about yourself
    await client.get_me()

    # "me" is an User object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, "has ID", dialog.id)

    # You can send messages to yourself...
    await client.send_message("me", "Hello, myself!")
    # ...to some chat ID
    await client.send_message(-100123456, "Hello, group!")
    # ...to your contacts
    await client.send_message("+34600123123", "Hello, friend!")
    # ...or even to any username
    await client.send_message("TelethonChat", "Hello, Telethon!")

    # You can, of course, use markdown in your messages:
    message = await client.send_message(
        "me",
        "This message has **bold**, `code`, __italics__ and "
        "a [nice website](https://example.com)!",
        link_preview=False,
    )

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    async for message in client.iter_messages("me"):
        print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo:
            path = await message.download_media()
            print("File saved to", path)  # printed after download is done


with client:
    client.loop.run_until_complete(main())
