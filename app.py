
from flask import Flask, request, render_template

app = Flask(__name__)

# 建立題庫
zh_ko_dict = {
    "你好": "안녕하세요",
    "안녕하세요" : "你好",
    "謝謝": "감사합니다",
    "對不起": "죄송합니다",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "老師": "선생님",
    "學生": "학생",
    "朋友": "친구",
    "Pikmin": "皮克敏",
    "家人": "가족",
    "愛": "사랑"
}

    
# homepage process
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        # 2. 讀取學生的問題
        question = request.form.get('question', '').strip()
        # 3. 查詢題庫的對應答案
        answer = zh_ko_dict.get(question, "抱歉，我目前沒有這個詞的韓文對應。")
        # 4. 回傳答案給學生
        return render_template('ask.html', question=question, answer=answer)
    # GET 時給空白欄位
    return render_template('ask.html', question="", answer="")

@app.route('/stock', methods=['GET', 'POST'])
def stock():
   import requests
   @app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        stock_no = request.form.get('question', '').strip()

        url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"

        try:
            res = requests.get(url)
            data = res.json()

            if data["stat"] == "OK" and data["data"]:
                last_day = data["data"][-1]
                date = last_day[0]
                close_price = last_day[6]

                answer = f"日期：{date}，收盤價：{close_price}"
            else:
                answer = "查無資料，請確認股票代號"

        except Exception as e:
            answer = f"發生錯誤：{e}"

        return render_template('stock.html', question=stock_no, answer=answer)

    return render_template('stock.html', question="", answer="")


if __name__ == '__main__':
    # 開發用；部署用 gunicorn（見下方）
    app.run(host='0.0.0.0', debug=False)

