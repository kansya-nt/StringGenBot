import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Anony
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ {ty} sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ...")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴋɪʀɪᴍ sɪɴɪ ᴀᴘɪ ɪᴅ ʟᴜ ᴋᴀᴋ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ʟᴜ ᴜᴅᴀʜ ʜᴀʙɪs ᴋᴀᴋ.\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ᴜʟᴀɴɢ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ɪᴅ ʏᴀɴɢ ʟᴜ ᴋɪʀɪᴍ sᴀʟᴀʜ ᴄᴏʙᴀ ᴄᴇᴋ ᴅᴜʟᴜ.\n\nʙᴀʀᴜ sᴛᴀʀᴛ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴋɪʀɪᴍ sɪɴɪ ᴀᴘɪ ʜᴀsʜ ʟᴜ ᴋᴀᴋ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ʟᴜ ᴜᴅᴀʜ ʜᴀʙɪs ᴋᴀᴋ. \n\nᴄᴏʙᴀ sᴛᴀʀᴛ ᴜʟᴀɴɢ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ʜᴀsʜ ʏᴀɴɢ ʟᴜ ᴋɪʀɪᴍ sᴀʟᴀʜ ᴄᴏʙᴀ ᴄᴇᴋ ᴅᴜʟᴜ.\n\nʙᴀʀᴜ sᴛᴀʀᴛ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀɴᴀ ɴᴏᴍᴏʀ ᴀᴋᴜɴ ɴʏᴀ ᴀɴᴊ ɴɢᴀɴᴛᴜᴋ ɴɪ ɢᴡ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ʟᴜ ᴜᴅᴀʜ ʜᴀʙɪs ᴋᴀᴋ.\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ᴜʟᴀɴɢ.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"» ɢᴀɢᴀʟ ᴍᴇɴɢɪʀɪᴍ ᴄᴏᴅᴇ ʟᴏɢɪɴ.\n\nᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀᴀɴ {f.value or f.x} ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ɪᴅ ʜᴀsʜ ʏᴀɴɢ ʟᴜ ᴋɪʀɪᴍ sᴀʟᴀʜ ᴄᴏʙᴀ ᴄᴇᴋ ᴅᴜʟᴜ.\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "» ɴᴏᴍᴏʀ ᴀᴋᴜɴ ɴʏᴀ sᴀʟᴀʜ.\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"ᴋɪʀɪᴍ sɪɴɪ ᴏᴛᴘ ɴʏᴀ ᴋᴀᴋ {phone_number}.\n\nᴄᴏɴᴛᴏʜ ᴏᴛᴩ <code>12345</code>, ʟᴜ ᴋɪʀɪᴍ ɴʏᴀ ᴘᴀᴋᴇ sᴘᴀsɪ ʏᴀ ᴍᴇᴋ <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ʟᴜ ᴜᴅᴀʜ ʜᴀʙɪs ᴋᴀᴋ.\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴏᴛᴩ ɴʏᴀ sᴀʟᴀʜ.</b>\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ..",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» ᴋᴇʟᴀᴍᴀᴀɴ ᴀɴᴊ ɴɢɪʀɪᴍ ᴏᴛᴘ ᴊᴜɢᴀ <b>ᴊᴀᴅɪ ɢᴀɢᴀʟ.</b>\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="» ᴋɪʀɪᴍ ᴘᴀssᴡᴏʀᴅ ᴠ2ʟ ɴʏᴀ ᴍᴇᴋ ᴊᴀɴ ʟᴀᴍᴀ :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "» ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ʟᴜ ᴜᴅᴀʜ ʜᴀʙɪs ᴋᴀᴋ. \n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "» ᴘᴀssᴡᴏʀᴅ ʟᴜ sᴀʟᴀʜ ɢᴏʙʟᴏᴋ, ʏᴀɴɢ ʙᴇɴᴇʀ ɴᴀᴘᴀ.\n\nᴄᴏʙᴀ sᴛᴀʀᴛ ʟᴀɢɪ.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "ɴɪʜ ᴍᴇᴋ {0} sᴛʀɪɴɢ sᴇssɪᴏɴ\n\n<code>{1}</code>\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={2}>ʙᴇꝛʟɪɴ sᴛʀɪɴɢ ɢᴇɴ</a>\n☠ <b>ɴᴏᴛᴇ :</b> ᴊᴀɴ ʟᴜ sʜᴀʀᴇ ᴋᴇ sɪᴀᴘᴀ ʏᴀ ᴀɴᴊɪɴɢ."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@Virtualmidnight"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("Berlinmidnight")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"{ty} ᴅᴀʜ ᴊᴀᴅɪ ʏᴀʜ ᴘᴜᴋɪᴍᴀᴋ.\n\nᴄᴏʙᴀ ᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ʟᴜ ʏᴀɴɢ ʙᴀɴʏᴀᴋ ʙᴏᴋᴇᴘ ɴʏᴀ.\n\nᴍɪɴɪᴍᴀʟ ʙɪʟᴀɴɢ ʜᴀᴛᴜʀ ɴᴜʜᴜɴ ʙᴀʙɪ ᴋᴇ <a href={SUPPORT_CHAT}>ʙᴇꝛʟɪɴ sᴛʀɪɴɢ</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» ᴘʀᴏsᴇs ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇɴɢᴀᴍʙɪʟᴀɴ sᴛʀɪɴɢ.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» ʙᴇʀʜᴀsɪʟ ᴍᴇʀᴇsᴛᴀʀᴛ ʙᴏᴛ.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» ᴘʀᴏsᴇs ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇɴɢᴀᴍʙɪʟᴀɴ sᴛʀɪɴɢ.", reply_markup=retry_key
        )
        return True
    else:
        return False
