from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    answer = call_baidu_api(question)
    return jsonify(answer)

def call_baidu_api(question):
    url = "https://appbuilder.baidu.com/s/ewCuB"  # 确认这是正确的 API URL
    headers = {
        "Content-Type": "application/json",
        "Authorization": "bce-v3/ALTAK-oH2mqX2fCfis7BoQ54Dc3/439538993fe13b7e098f43a63e3d2f8894e2c661"
    }
    payload = {
        "app_id": "a2340a2d-1d15-4642-b5b7-c80fd3c3cc7b",
        "query": question
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # 这将抛出异常，如果请求返回了失败状态码
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


if __name__ == '__main__':
    app.run(debug=True)
