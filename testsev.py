from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 경로에 대해 CORS 활성화

# 정적 파일을 제공하는 라우트
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

if __name__ == '__main__':
    app.run(debug=True)
