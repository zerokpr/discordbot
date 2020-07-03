# discordbot
身内のdiscordサーバーで使えるツール
現在discord.pyを用いて作っています。

・list_manage.py
「Groovyにプレイリスト機能を外付けするbot作れないかな」という友人の呟きがきっかけ。
--create listname
listnameの部分を名前に持つプレイリストを作成
--add listname url
listnameのプレイリストにurlを追加する。
--print listname
listnameに入っているurlをメッセージ欄へ"-play url"の形式で送信していく。ラグを考慮すると送信の合間に少し待機した方がよいと思いそのようにしている。
後はremoveなども備えている...が、
Groovy側がbotからのメッセージを受け付けないようにしているらしく、折角のエラー出力も無駄になってしまった。

・dice_bot.py
TRPGで使うダイス機能のみを持つbot。
メッセージで
--dice 2d20
のように送ると、ダイスの結果を出力してくれる。
TRPGをやるサーバーで「キャラクターステータスを自動管理したいねー」という話が出たので始まったが、必要な機能がかなり多くなるのでこれでとりあえずお茶を濁した。
そのうち管理システムも作ってみたい。