from app import app
import webview

# This is to run directly through python only. Not thorugh the flask run
# To run this code you would type     python run.py
if __name__ == '__main__':
    app.run(debug=True)
    #webview.start()