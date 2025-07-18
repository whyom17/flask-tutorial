from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        user=request.form.get("user")
        passw=request.form.get("pass")
        
        users={
            'vyom':'1243',
            'abhi':'6479',
            'harry':'pass123'
        }
        
        if user in users and passw == users[user]:
            return render_template('home.html',user=user , isTrue= True)
        else:
            return 'Invalid Creds'
    else:    
        return render_template('home.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')
           
@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')
           
if __name__ == "__main__":
    app.run(debug=True)