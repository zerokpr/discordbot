import discord
import random
import re

# トークンの入力は適当なので、各々変えた方がよい
f = open("./dicebot_token.txt", "r")
token = f.readline()
f.close()

client = discord.Client()

def isCommand(cmd):
    command_list = ["--dice", "--hello"]
    if cmd in command_list:
        return True
    else:
        return False

def dice(val):
    if not re.match("[1-9][0-9]*d[1-9][0-9]*", val):
        return -1
    d_num, d_max = map(int, val.split('d'))
    ret = 0
    for i in range(d_num):
        ret += random.randint(1, d_max)
    return ret

def errorMsg(errno):
    ret_msg = "デフォルトエラー."
    if errno == 1:
        ret_msg = "コマンドが不正です."

    return ret_msg

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    random.seed()
    print("乱数生成器初期化")
    print("------")

@client.event
async def on_message(message):
    # 無限ループ防止
    if message.author == client.user:
        return 
    
    msg = message.content.split(' ')

    errno = -1

    # コマンドであるかをチェック
    if not isCommand(msg[0]):
        return

    print(msg)

    cmd = msg[0]

    if cmd == "--dice":
        ret = -1
        if len(msg) == 2:
            ret = dice(msg[1])

        if ret < 0:
            errno = 1
        else:
            await message.channel.send(msg[1] + " >> " + str(ret))
            return
    
    elif cmd == "--hello":
        await message.channel.send("Hello, world!")
        return

    if errno >= 1: # エラー出力
        error_msg = errorMsg(errno)
        await message.channel.send(error_msg)


client.run(token)
