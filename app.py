from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.gbr1o.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
# 이거 몽고데이터베이스 본인껄로 바꿔주세요!

@app.route('/')
def home():
   return render_template('index.html')

#상우님 영균님이 한 요리 포스트 올리기 서버
@app.route('/food', methods=['POST'])
def food_post():
    name_receive = request.form['name_give']
    url_receive = request.form['url_give']
    choice_receive = request.form['choice_give']
    recipe_receive = request.form['recipe_give']

    food_list = list(db.food.find({}, {'_id': False}))
    count = len(food_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'url': url_receive,
        'choice': choice_receive,
        'recipe': recipe_receive
    }
    db.food.insert_one(doc)

    return jsonify({'result':'success', 'msg': '등록 완료!'})

@app.route("/food", methods=["GET"])
def food_get():
    food_list = list(db.food.find({}, {'_id': False}))
    return jsonify({'foods': food_list})

#댓글 올리기 서버
@app.route('/food/comment', methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    nickname_receive = request.form['nickname_give']
    num_receive = request.form['num_give']
    doc = {
        'comment': comment_receive,
        'nickname': nickname_receive,
        'num': num_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '댓글 추가 완료!'})

#내가 진행하는 댓글 GET 서버
@app.route("/food/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.comment.find({}, {'_id':False}))
    return jsonify({'comments':comment_list})

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username
#[출처] [Python Flask] # 02 파이썬 플라스크 라우팅|작성자 넬티아

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' % message_id
#[출처] [Python Flask] # 02 파이썬 플라스크 라우팅|작성자 넬티아




if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)