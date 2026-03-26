
from flask import Flask, request, render_template

app = Flask(__name__)

# 建立題庫
zh_ko_dict = {
    "你好": "안녕하세요",
    "謝謝": "감사합니다",
    "對不起": "죄송합니다",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "老師": "선생님",
    "學生": "학생",
    "朋友": "친구",
    "家人": "가족",
    "愛": "사랑"
}
zh_jp_dict = {
    "你好": "こんにちは",
    "謝謝": "ありがとうございます",
    "對不起": "すみません",
    "早安": "おはようございます",
    "晚安": "おやすみなさい",
    "老師": "先生",
    "學生": "学生",
    "朋友": "友達",
    "家人": "家族",
    "愛": "愛"
}




# homepage process
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    question = ""
    answer = ""
    selected_lang = "ko" 

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        selected_lang = request.form.get('lang', 'ko')
        
        # 修正處：確保名稱與上方定義的 zh_ko_dict / zh_jp_dict 一致
        current_dict = zh_ko_dict if selected_lang == "ko" else zh_jp_dict
        
        # 執行查詢邏輯
        answer = current_dict.get(question, "很抱歉，目前本地辭庫沒有此詞彙")

    return render_template('ask.html', question=question, answer=answer, lang=selected_lang)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

