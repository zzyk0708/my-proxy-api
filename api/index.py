from flask import Flask
import random
import os

app = Flask(__name__)

@app.route('/get_ip')
def get_ip():
    try:
        # Vercel 中读取上一级目录的文件
        file_path = os.path.join(os.path.dirname(__file__), '../ips.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            proxies = [line.strip() for line in f if line.strip()]

        if not proxies:
            return "Error: IP list is empty", 500

        return random.choice(proxies)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run()
