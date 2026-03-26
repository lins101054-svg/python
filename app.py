
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
    answer = None  # 預設為 None，代表尚未進行查詢
    selected_lang = "ko"

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        selected_lang = request.form.get('lang', 'ko')
        
        current_dict = zh_ko_dict if selected_lang == "ko" else zh_jp_dict
        answer = current_dict.get(question, "很抱歉，目前本地辭庫沒有此詞彙")

    # 在 render 時，如果 answer 是 None，前端就不顯示結果
    return render_template('ask.html', question=question, answer=answer, lang=selected_lang)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

