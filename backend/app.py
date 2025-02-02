from flask import Flask, request, jsonify

app = Flask(__name__)
posts = []

@app.route('/post', methods=['POST'])
def add_post():
    data = request.json
    posts.append(data)
    return jsonify({"message": "Пост додано!"})

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
