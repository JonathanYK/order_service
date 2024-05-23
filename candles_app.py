from app_init import create_app
# Yonatan Kalma
# https://github.com/JonathanYK

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=8765)
