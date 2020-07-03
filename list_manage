import discord
import pickle
import time

print("discordのトークンを入力してください.\n")
token = str(input())

# このファイルがあるディレクトリにplaylists.pklという名前の空のファイルを作っておく.
f = open("./playlists.pkl", "r+b")


try:
    playlists = pickle.load(f)
except EOFError:
    playlists = dict()

pickle.dump(playlists, f)
f.close()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    # 再帰メッセージ呼び出し防止
    if message.author == client.user:
        return

    print(message.content)
    msg = message.content.split(' ')

    if msg[0] == "--create": # プレイリスト作成
        listname = msg[1]

        # エラー処理
        if listname in playlists:
            print("既に存在するプレイリストです.\n")
            await message.channel.send("既に存在するプレイリストです.")
            return 
        
        playlists[listname] = []

    elif msg[0] == "--add": # 曲をプレイリストに追加
        if len(msg) != 3: # 引数不適
            print("コマンドの引数が不正です.\naddコマンドは次のようにならなければなりません.\n--add playlist_name url\n")
            await message.channel.send("コマンドの引数が不正です.\naddコマンドは次のようにならなければなりません.\n--add playlist_name url")
            return
        
        listname = msg[1]
        url = msg[2]

        # エラー処理
        if not (listname in playlists): # プレイリストが存在しない場合
            print("指定されたプレイリストは存在しません.\ncreateコマンドで作成してください.\n")
            await message.channel.send("指定されたプレイリストは存在しません.\ncreateコマンドで作成してください.")
            return
        if url in playlists[listname]: # 曲が既に存在する場合
            print("このurlの曲は既にプレイリストに存在します.\n")
            await message.channel.send("このurlの曲は既にプレイリストに存在します")
            return

        playlists[listname].append(url)
    elif msg[0] == "--remove": # 曲をプレイリストから削除

        if len(msg) != 3: # 引数不適
            print("コマンドの引数が不正です.\nremoveコマンドは次のようにならなければなりません.\n--remove playlist_name url\n")
            await message.cahnnel.send("コマンドの引数が不正です.\nremoveコマンドは次のようにならなければなりません.\n--remove playlist_name url")
            return 
        
        listname = msg[1]
        url = msg[2]
        
        if not url in playlists[listname]:
            print("指定された曲はプレイリストに存在しません\n")
            await message.cahnnel.send("指定された曲はプレイリストに存在しません")
        playlists[listname].remove(url)
        
    elif msg[0] == "--remove_playlist": # プレイリストを削除
        if len(msg) != 2:
            print("コマンドの引数が不正です.\nremove_playlistコマンドは次のようにならなければなりません.\n--remove_playlist playlist_name\n")
            await message.channel.send("コマンドの引数が不正です.\nremove_playlistコマンドは次のようにならなければなりません.\n--remove_playlist playlist_name")
        listname = msg[1]
    
        if not listname in playlists:
            print("指定されたプレイリストは存在しません\n")
            await message.channel.send("指定されたプレイリストは存在しません.")        
        playlists.pop(listname)

    elif msg[0] == "--print": # プレイリストのurl一覧を出力する（Groovyに再生させる）
        if len(msg) != 2:
            print("引数の数が不正です.\nprintコマンドは次のようにならなければなりません.\n--print playlist_name\n")
            await message.channel.send("引数の数が不正です.\nprintコマンドは次のようにならなければなりません.\n--print playlist_name")
            return
        listname = msg[1]
        
        if not (listname in playlists): # プレイリストが存在しない場合
            print("指定されたプレイリストは存在しません.\ncreateコマンドで作成してください.\n")
            await message.channel.send("指定されたプレイリストは存在しません.\ncreateコマンドで作成してください.")
        for url in playlists[listname]:
            cmd = "-play " + url + "\n"
            await message.channel.send(cmd)
            time.sleep(0.5)
    with open("./playlists.pkl", "wb") as f:
        pickle.dump(playlists, f)

client.run(token)
