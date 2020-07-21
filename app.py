from flask import Flask, render_template #플라스크 라이브러리로 서버를 띄우는 방법
from data import Articles
app = Flask(__name__) #대문자 플라스크는 클라스 객체생성
app.debug = True

@app.route('/')
def index():
    print("Success")
    #return "Test"
    return render_template('home.html', hello = "Daechan")

@app.route('/about')
def about():
    print("Success")
    #return "Test"
    return render_template('about.html', hello = "Daechan")

@app.route('/articles', methods = ['GET', 'post'])
def articles():
    print("Success")
    #return "Test"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', articles = articles)

#이미지
@app.route('/test')
def show_image():
    return render_template('image.html')

if __name__=="__main__":
    # app.run(host = '0.0.0.0', port='50')
    app.run()
