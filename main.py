from flask import Flask, render_template, jsonify
from localstorage_flask import LocalStorageFlask

app = Flask(__name__)
# Khởi tạo thư viện LocalStorageFlask
localstorage = LocalStorageFlask(app)

@app.route("/")
def index():
    # Lưu thông tin vào localStorage
    localstorage.setItem("username", "currentUser")
    localstorage.setItem("theme", "dark")
    username = localstorage.getItem("username", "username")  # Lấy dữ liệu username
    theme = localstorage.getItem("theme", "theme")

    # Trả về trang HTML với mã JavaScript cần thiết
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
