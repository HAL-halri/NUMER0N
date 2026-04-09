from flask import Flask, render_template, request, jsonify, session
import random
import time

app = Flask(__name__)
# セッションキー
app.secret_key = 'numer0n_secret_training_key'

#数字生成
def generate_secret(length):
    digits = []
    while len(digits) < length:
        random_digit = random.randint(0, 9)
        
        #難易度によって生成数を変える
        if length == 6:
            digits.append(str(random_digit))
        else:
            if str(random_digit) not in digits:
                digits.append(str(random_digit))
            
    return "".join(digits)

#Eat,Bite判定
def calculate_eat_bite(guess, secret):
    eat = 0
    bite = 0
    
    #一度判定された数字を保存
    secret_list = list(secret)
    guess_list = list(guess)
    
    #Eat判定
    for i in range(len(guess)):
        if guess_list[i] == secret_list[i]:
            eat += 1
            #判定済みの文字を置換、Biteでの誤検知防止
            secret_list[i] = 'E'
            guess_list[i] = 'G'
            
    #Bite判定
    for i in range(len(guess)):
        if guess_list[i] != 'G' and guess_list[i] in secret_list:
            bite += 1
            #Bite判定した文字を1つ置換 (2重Bite防止)
            secret_list[secret_list.index(guess_list[i])] = 'B'
            
    return {"eat": eat, "bite": bite}
    #Eatで判定されたものがBiteでも判定されるのを防ぐためにEat側で判定されたことをマークする(G)


def format_time(total_seconds):
    m = total_seconds // 60
    s = total_seconds % 60
    return f"{m:02}:{s:02}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start', methods=['POST'])
def start_game():
    data = request.json
    length = int(data.get('difficulty', 4))
    
    session['secret'] = generate_secret(length)
    session['start_time'] = time.time()
    
    return jsonify({"status": "started"})

@app.route('/api/check', methods=['POST'])
def check_guess():
    guess = request.json.get('guess', '')
    secret = session.get('secret', '')
    
    if not secret:
        return jsonify({"error": "ゲームが開始されていません"}), 400
        
    result = calculate_eat_bite(guess, secret)
    is_clear = (result['eat'] == len(secret))
    
    response_data = {
        "eat": result['eat'],
        "bite": result['bite'],
        "is_clear": is_clear
    }
    
    if is_clear:
        elapsed_time = int(time.time() - session.get('start_time', time.time()))
        response_data["clear_time"] = format_time(elapsed_time)
        response_data["secret"] = secret
        
    return jsonify(response_data)

@app.route('/api/retire', methods=['POST'])
def retire():
    secret = session.get('secret', '')
    return jsonify({"secret": secret})

if __name__ == '__main__':
    app.run(debug=True)