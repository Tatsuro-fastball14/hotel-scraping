# ライブラリ呼び出し
from flask import Flask, render_template

# クラス呼び出し
app = Flask(__name__)

# ルーティングを定義
@app.route('/')
def hello_World():
    return 'HelloWorld！'

# サーバー起動
app.run(debug=True)


