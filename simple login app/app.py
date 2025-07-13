# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
# ]
# ///

from flask import Flask, request, Response, url_for, session, redirect

app= Flask(__name__)
app.secret_key = 'misogynist'  # when working with session it is NECESSARY to set a string which is to be used by Flask to sign session cookies and protect against tampering.
# basically it is used to lock the session

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username= request.form.get("username")
        password= request.form.get('password')
        
        if username == 'admin' and password == '123' :
            session['user'] = username
            return redirect(url_for('welcome'))
        
        else: 
            return Response('invalid credentials. try again !', mimetype="text/plain" )  # by default mimetype is set HTML
    
    return '''
            <h2> Login Page </h2>
            <form method= 'POST'>
            Username: <input type='text' name="username">
            <br>
            Password: <input type='text' name="password">
            <br>
            <input type='submit' value='Login'>

'''

@app.route('/Welcome')
def welcome():
    if "user" in session:
        return f'''
            <h2> Welcome, {session['user']} ! </h2>
            <a href={url_for('logout')}>Logout</a>
    
    '''
    return redirect('/')   # or redirect(url_for('login'))

@app.route('/Logout')
def logout():
    session.pop("user", None)  
    return redirect('/')   # or redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)