
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




# 使用者輸入
stock_no = input("請輸入股票代號（例如 2330）：")

 

# API URL
url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"

 

# 發送請求
res = requests.get(url) #原始
data = res.json() #解析後的資料

 

# 判斷是否成功
if data["stat"] == "OK":

 

    print("前一天收盤價：",data["data"][-1][6]) #return render_template('stock.html', question=question, answer=answer)
else:
    print("查無資料，請確認股票代號或日期") #return render_template('stock.html', question=question, answer=answer)
