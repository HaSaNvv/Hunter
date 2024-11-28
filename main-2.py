import os
import wonderwords
from wonderwords import RandomWord
filename = 'sessions.txt'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write('')
    print(f"{filename} has been created.")
else:
    print(f"{filename} already exists.")
import random
import asyncio
from os import system, name, path
from time import sleep
from random import choice
from base64 import b64decode
from kvsqlite.sync import Client

import os

try:
    import aiohttp
except:
    system('pip install aiohttp')
    import aiohttp
try:
    from telebot import TeleBot
    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
except:
    system('pip install telebot')
    from telebot import TeleBot
    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
try:
    from telethon import TelegramClient, errors, functions
    from telethon.tl.functions.account import CheckUsernameRequest
    from telethon.sessions import StringSession
except:
    system('pip install telethon')
    from telethon import TelegramClient, errors, functions
    from telethon.tl.functions.account import CheckUsernameRequest
    from telethon.sessions import StringSession
try:
    from bs4 import BeautifulSoup as S
except:
    system('pip install beautifulsoup')
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    system('pip install fake_useragent')
    from fake_useragent import UserAgent
try:
    from datetime import datetime
except:
    system('pip install datetime')
    from datetime import datetime

from telebot import types

ses = None
token = "8072115236:AAHlxPzeTQPf8bT9qienetTJHY0z-tTSsto"
chat_id = "7896895861" 
clicks = 1
bot = TeleBot(token=token)
db = Client(f"users2.bot")
filename = "sessions.txt"

async def fragment(username):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://fragment.com/username/{username}', headers={'Cookie': 'stel_ssid=105b9e3f8fc71d3078_18338999148668777485;','Pragma': 'no-cache','Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"','Sec-Ch-Ua-Mobile': '?1','Sec-Ch-Ua-Platform': '"Android"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': str(UserAgent())}) as response:
                text = await response.text()
                soup = S(text, 'html.parser')
                ok = soup.find("meta", property="og:description").get("content")
                if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
                elif "is taken" in ok:return "is taken"
                else:return False
        except:return 

async def channels2(client, username):
    di = await client.get_dialogs()
    for chat in di:
        if chat.name == f'[ {username} ]' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            print('- Flood : '+username+' .')
            return False
    return True

async def checks(username, client):
    return await client(CheckUsernameRequest(username))

async def claimer(client,username):
    global clicks
    result = await client(functions.channels.CreateChannelRequest(title=f'[ {username} ]',about=f'Source - @Dython \nOwner - @ssuxs',megagroup=False))
    try:
        await client(functions.channels.UpdateUsernameRequest(channel=result.chats[0],username=username))
        await client.send_message(username,f'⌯ Done New Hunt .\n⌯ UserName : @{username} .\n⌯ Date : {datetime.now().strftime("%H:%M:%S")} .\n⌯ Source : @dython .\n⌯ Owner : @ssuxs .')
        me = await client.get_me()
        bot.send_message(chat_id,f'⌯ Done New Hunt .\n⌯ UserName : @{username} .\n⌯ Date : {datetime.now().strftime("%H:%M:%S")}\n⌯ Clicks : {clicks} .\n⌯ Source : @dython .\n⌯ Number : {me.phone}\n⌯ ID : {me.id}\n⌯ Name : {me.first_name}{me.last_name}')
        return True
    except Exception as e: bot.send_message(chat_id,f'⌯ Error Message .\nMessage : {e} .\nUserName : @'+str(username));return False

async def checker(username, client,type):
    global clicks
    try:
        clicks += 1
        check = await checks(username, client)
        if check:
            print('\033[92m' + '- Available : ' + username + ' .' + '\033[0m')
            claim = await claimer(client,username)
            if claim and await fragment(username) == "is taken":claim = True
            else:claim = False
            flood = await channels2(client,username)
            if not flood:
            	with open('flood.txt', 'a') as floodX:
            	   floodX.write(username + "\n")
            	if claim:
            		if type == "c" or type == "fl":
            			return
            	if "flood" in type:
            		bot.send_message(chat_id=chat_id, text="Hi New Flood Username\n" + str(username))
        else:
            clicks += 1
            print('\033[91m' + '- Taken : ' + username + ' .' + '\033[0m')
    except errors.rpcbaseerrors.BadRequestError:
        print('\033[91m' + '- Banned : ' + username + ' .' + '\033[0m')
        with open("banned4.txt", "a") as banned:
            banned.write(username + '\n')
    except errors.FloodWaitError as timer:
        print('- Flood Account [ ' + str(timer.seconds) + ' Seconds ] .')
    except errors.UsernameInvalidError:
        print('- Error : ' + username + ' .')

def usernameG():
    k = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    n = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    c = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    z = ''.join(choice('1234567890') for i in range(1))
    g = ''.join(choice('1234567890') for i in range(1))
    v = ''.join(choice('_') for i in range(1)) 
    try:type = db.get("type")
    except: return False
    if type == "se7":
        u1 = k + n + z + z + z + z
        u2 = k + g + z + z + z + z 
        s = u1, u2
        return choice(s)
    elif type == "th3":
        u1 = k + v + n + n + n
        u2 = k + n + v + n + n
        u3 = k + n + n + v + n
        u4 = k + k + v + k + n
        u5 = k + v + k + k + n
        u5 = k + k + k + v + n
        u6 = k + n + v + k + k
        u7 = k + n + k + v + k
        u8 = k + k + n + v + k
        u9 = k + v + n + k + k
        u10 = k + k + v + n + k
        u11 = k + v + k + n + k
        s = u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11
        return choice(s)
    elif type == "chi": 
        u1 = 'zh_cn' + ''.join(choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(2))
        u2 = 'z_hcn' + ''.join(choice('1234567890qwertyuio') for i in range(1))
        u3 = 'zhc_n' + ''.join(choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        u4 = 'zh_cn' + ''.join(choice('1234567890') for i in range(3))
        return u4
    elif type == "f5":
        u1 = k + k + v + n + n
        u2 = k + v + k + n + n
        u3 = k + n + v + k + n
        u4 = k + n + v + n + k
        u5 = k + k + n + v + n
        u6 = k + n + k + v + n
        u7 = k + v + k + n + n
        u8 = k + v + n + n + k
        s = u1, u2, u3, u4, u5, u6, u7, u8
        return choice(s)
    elif type == "f5i":
    	u1 = k + c + n + n + n
    	u2 = k + z + z + z + k
    	u3 = k + k + k + n + c
    	u4 = k + z + z + z + g
    	u5 = k+ n+ n + n+ c
    	s = u1,u2,u3,u4,u5
    	return choice(s)
    elif type == "fi5":
        u1 = k + n + k + k + "bot"
        u2 = k + n + n + n + "bot" 
        u3 = k + k + k + n + "bot" 
        u4 = k + k + n + k + "bot" 
        u5 = k + n + k + n + "bot" 
        u6 = k + k + n + n + "bot" 
        u7 = k + n + n + k + "bot" 
        u8 = k + n + c + "bot" 
        s = u1, u2, u3, u4, u5, u6, u7, u8
        return choice(s)
    elif type == "auto":
        r = RandomWord()
        try:
            s = r.word(word_min_length=5, word_max_length=12)
            return s
        except Exception as e:
            print(f"Error generating word: {e}")



async def start(client, username,type):
    global clicks
    try:
        ok = await fragment(username)
    except:
        return
    try:
        if not ok:
            if type == "f": type = "flood"
            elif type == "c": type = "claim"
            elif type == "fl": type = "floods"
            await checker(username, client,type)
        elif ok == "is taken":
            print('\033[91m' + '- Taken : ' + username + ' .' + '\033[0m')
            clicks += 1
        else:
            print('\033[91m' + '- Fragment.com : ' + username + ' .' + '\033[0m')
            clicks +=1
            open("fragment.txt", "a").write(username + '\n')
    except Exception as e:
        print(f'an error: {e}')

async def clientX():
    try:
        with open("sessions.txt", "r") as file:
            sessions = file.readlines()
        sessions = [session.strip() for session in sessions if session.strip()]
        if not sessions:
            await bot.send_message(chat_id=chat_id, text="لايوجد حسابات بالبوت , تم ايقاف الصيد")
            return None
    except FileNotFoundError:
        await bot.send_message(chat_id=chat_id, text="ملف الجلسات غير موجود.")
        return None
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=f"حدث خطأ أثناء قراءة ملف الجلسات: {e}")
        return None

    random_session = random.choice(sessions)

    try:
        client = TelegramClient(StringSession(random_session), 
                                b64decode("MjUzMjQ1ODE=").decode(), 
                                b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
        await client.start()
        print(f"تم الاتصال باستخدام الجلسة : {random_session}")
        return client
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=f"فشل الاتصال باستخدام الجلسة المختارة. الخطأ: {e}")
        return None

flag = False
async def work(message):
    global flag, clicks
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    if not path.exists('sessions.txt'):
        ses = False
        bot.send_message(chat_id=chat_id, text="لايوجد حسابات بالبوت , تم ايقاف الصيد")
        return False

    de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        username = usernameG()
        if not username:
    	    de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="الرجاء اختر نوع من الاشكال لكي افحص",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="اختيار", callback_data="type")]]))
    	    return 
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('\033[91m' + '- Banned : ' + username + ' .' + '\033[0m')
            continue
        try:
            with open('fragment.txt', 'r') as file:
                fragment = file.read()
        except Exception as e:
            print(f'an error :{e}')

        if username in fragment:
            print('\033[91m' + '- Fragment.com : ' + username + ' .' + '\033[0m')
            continue
        type = "f"
        await start(session, username,type)

async def us5(message,username):
    global flag, clicks
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزر و صيدة\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('\033[91m' + '- Banned : ' + username + ' .' + '\033[0m')
            clicks += 1
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('\033[91m' + '- Fragment.com : ' + username + ' .' + '\033[0m')
            clicks +=1
            continue
        type = "c"
        await start(session, username,type)


async def us3(message,username):
    global flag, clicks
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزر لجلب اذا كان خاصية\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('\033[91m' + '- Banned : ' + username + ' .' + '\033[0m')
            clicks += 1
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('\033[91m' + '- Fragment.com : ' + username + ' .' + '\033[0m')
            clicks += 1
            continue
        type = "fl"
        await start(session, username,type)

async def checkCombo(message):
    global flag, clicks
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    try:de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    except:de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    with open(message.document.file_name, 'r') as file:
        usernames = file.readlines()
    for username in usernames:
        if '@' in username:
            username = username.split('@')[1]
        if flag:
            break
        username = username.strip()
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('\033[91m' + '- Banned : ' + username + ' .' + '\033[0m')
            clicks += 1
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('\033[91m' + '- Fragment.com : ' + username + ' .' + '\033[0m')
            clicks += 1
            continue
        type = "f"
        await start(session, username,type)
    bot.delete_message(chat_id=chat_id, message_id=de.message_id)
    bot.send_message(chat_id=chat_id,text="@",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))

async def add_acc(message, call):
    chat_id = call.message.chat.id
    try:
        session = message.text
        filename = 'sessions.txt'
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('')
        else:

            with open(filename, "r") as f:
                if session in f.read():
                    bot.send_message(chat_id=chat_id, text="This session already exists.", reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="Back", callback_data="stopp")]]))
                    return

            client = await TelegramClient(StringSession(session), b64decode("MjUzMjQ1ODE=").decode(), b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode()).start()

            with open(filename, "a") as f:
                f.write(session + "\n")

            bot.send_message(chat_id=chat_id, text="Session added successfully.", reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="Back", callback_data="stopp")]]))
    except Exception as e:
        bot.send_message(chat_id=chat_id, text=f'An error occurred: {e}')

async def get_accs(message, call):
    chat_id = call.message.chat.id
    filename = "sessions.txt"
    
    try:
        with open(filename, "r") as f:
            sessions = f.readlines()
            if sessions:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="ارسال السيشنات في رسالة", callback_data="send_sessions_message"))
                markup.add(types.InlineKeyboardButton(text="ارسال السيشنات في ملف", callback_data="send_sessions_file"))

                bot.send_message(chat_id=chat_id, text="اختار كيف بدك تحصل السيشنات :", reply_markup=markup)
            else:
                bot.send_message(chat_id=chat_id, text="مافي خريات")
    except Exception as e:
        if 'No such file or directory' in (str(e)):
            bot.send_message(chat_id=chat_id, text='لايوجد حسابات بالبوت')
        else:
            bot.send_message(chat_id=chat_id, text=f'An error occurred: {e}')


@bot.callback_query_handler(func=lambda call: call.data == "send_sessions_message")
def send_sessions_message(call):
    with open("sessions.txt", "r") as f:
        sessions = f.readlines()
        bot.send_message(chat_id=call.message.chat.id, text=f"السيشنات المخزنة:\n{chr(10).join(sessions).strip()}")

@bot.callback_query_handler(func=lambda call: call.data == "send_sessions_file")
def send_sessions_file(call):
    filename = 'sessions.txt'
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('')
            bot.send_document(chat_id=call.message.chat.id, document=f, caption="هذه السيشنات الخاصة بك")
    else:
        with open("sessions.txt", "rb") as f:
            bot.send_document(chat_id=call.message.chat.id, document=f, caption="هذه السيشنات الخاصة بك")


def gg(message, call):
	asyncio.run(add_acc(message=message, call=call))

def cc(message, call):
	asyncio.run(get_accs(message=message, call=call))

@bot.callback_query_handler(func=lambda call: True)
def callB(call):
    global flag
    if call.data == "type":
        bot.edit_message_text(
    chat_id=chat_id,
    message_id=call.message.message_id,
    text="اختر النوع من احدى الازرار",
    reply_markup=InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="رباعي", callback_data="th3"),
            InlineKeyboardButton(text="صيني", callback_data="chi"),
            InlineKeyboardButton(text="بوتات", callback_data="fi5"),
        ],
        [
            InlineKeyboardButton(text="رباعي حرفين", callback_data="f5"),
            InlineKeyboardButton(text="سداسي صيني", callback_data="se7"),
        ],
        [
            InlineKeyboardButton(text="خماسي حرفين عشوائي", callback_data="f5i"),
            InlineKeyboardButton(text="صيد تلقائي", callback_data="auto"),
        ],
    ])
)

    elif call.data in ["th3", "fi5", "f5", "se7","f5i", "chi", "auto"]:
        db.set("type", call.data)
        m = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"- تم اختيار النوع الذي اخترته .")
        sleep(2)
        bot.delete_message(chat_id=chat_id, message_id=m.message_id)
        reset(msg=call.message)
    elif call.data == "start":
        flag = False
        asyncio.run(work(message=call.message))
    elif call.data == "stop":
        flag = True
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        reset(msg=call.message)
    elif call.data == "add":
    	de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان سيشن telethon لأضافتة في البوت",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    	bot.register_next_step_handler(call.message,gg)
    elif call.data == "stopp":
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        reset(msg=call.message)
    elif call.data == "us1":
    	flag = False
    	bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="اختر من احدى الازرار ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="تثبيت لجلب خاصية", callback_data="po"),InlineKeyboardButton(text="تثبيت خاصية", callback_data="pi")]]))
    elif call.data == "pi":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان اليوزر للتثبيت عليه و صيدة\nارسل بهذا الشكل :\n.تثبيت xxMxx",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "po":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان اليوزر للتثبيت عليه حتى يصبح خاصية\nارسل بهذا الشكل : \n.جلب xxMxx",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "combo":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان الملف المراد فحصه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "add_account":
        de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل السيشن الذي تود اضافته بالبوت\n (اذا اكثر من سيشن خليهم سطر بسطر )", reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
        bot.register_next_step_handler(call.message, lambda message: gg(message, call))
    elif call.data == "get_accounts":
        de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="جاري جلب السيشنات\nقم بارسال YES للتاكيد",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
        bot.register_next_step_handler(call.message, lambda message: cc(message, call))
    elif call.data == "accs":
        de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="جاري جلب عدد الحسابات",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "rst":
        de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="جاري حذف التخزين ...",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
        try:
            os.remove('sessions.txt')
            sleep(2)
            de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="تم حذف التخزين ✅",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
        except Exception as x:
            if 'cannot find the file' in (str(x)):
                sleep(2)
                de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="التخزين محذوف بالفعل✅",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
            else:
                print('⌯ POWRED BY DYTHON SOURCE ⌯')

        
@bot.message_handler(content_types=["document"])
def fromCombo(message):
    file = bot.download_file(bot.get_file(message.document.file_id).file_path)
    open(file=message.document.file_name, mode="wb").write(file)
    asyncio.run(checkCombo(message=message))

def reset(msg): 
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    if last_name is None:
        last_name = ''
    profile = f'{first_name}{last_name}'
    bot.send_message(
    chat_id, 
    text=f"- Hello sir {profile} .\n- Welcome to the best hunt tool .\n- Powred by : @ssuxs .\n- Source : @dython .", 
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="⌯ إضافة حساب ⌯", callback_data="add_account"), InlineKeyboardButton(text="⌯ جلب الحسابات ⌯", callback_data="get_accounts")],
        [InlineKeyboardButton(text="⌯ عدد الحسابات ⌯", callback_data="accs")],
        [InlineKeyboardButton(text="⌯ فحص عشوائي ⌯", callback_data="start")],
        [InlineKeyboardButton(text="⌯ من ملف ⌯", callback_data="combo"), InlineKeyboardButton(text="⌯ تثبيت ⌯", callback_data="us1")],
        [InlineKeyboardButton(text="⌯ اختيار نوع ⌯", callback_data="type")],
        [InlineKeyboardButton(text="⌯ حذف التخزين ( خطر⛔ ) ⌯", callback_data="rst")]
    ])
)

@bot.message_handler(func=lambda msg: True)
def startB(msg):
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    if last_name is None:
        last_name = ''
    profile = f'{first_name}{last_name}'
    if msg.chat.id != int(chat_id): return
    elif msg.text == "/start":

        bot.send_message(
    chat_id, 
    text=f"- Hello sir {profile} .\n- Welcome to the best hunt tool .\n- Powred by : @ssuxs .\n- Source : @dython .", 
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="⌯ إضافة حساب ⌯", callback_data="add_account"), InlineKeyboardButton(text="⌯ جلب الحسابات ⌯", callback_data="get_accounts")],
        [InlineKeyboardButton(text="⌯ فحص عشوائي ⌯", callback_data="start")],
        [InlineKeyboardButton(text="⌯ من ملف ⌯", callback_data="combo"), InlineKeyboardButton(text="⌯ تثبيت ⌯", callback_data="us1")],
        [InlineKeyboardButton(text="⌯ اختيار نوع ⌯", callback_data="type")],
        [InlineKeyboardButton(text="⌯ حذف التخزين ( خطر⛔ ) ⌯", callback_data="rst")]
    ])
)
    elif ".فحص" in msg.text:
    	bot.send_message(chat_id=chat_id,text="الفحص شغال طاب يومك")
    elif '.تثبيت ' in msg.text:
    	username = msg.text.split('.تثبيت ')[1]
    	if '@' in username:username = username.split('@')[1]
    	asyncio.run(us5(message=msg,username=username))
    elif ".جلب " in msg.text:
        username = msg.text.split('.جلب ')[1]
        if '@' in username:username = username.split('@')[1]
        asyncio.run(us3(message=msg,username=username))

def polling(bot, interval=5):
    import time ; from requests import exceptions
    while True:
        try:
            bot.polling()
            print('- New Session Bot .')
        except exceptions.ConnectionError:
            print('- New Session Bot .')
            time.sleep(interval)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)
polling(bot=bot)
