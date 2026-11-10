# Veronica Valenzuela 
# CIS256 Fall 2026 
# Programming Assignment 5 


from flask import Flask
from flask import request, render_template_string
from flask_bcrypt import Bcrypt
import re 

app = Flask(__name__)
bcrypt = Bcrypt(app)


# GET: display HTML registration form. 
@app.route("/register", methods=["GET"])
def register_form(): 
    
    form_html = """
    <h2>Programming Assignment 5</h2>
    
    <form method="POST" action"/register">
    
        <label for="fullname">Full Name:</label>
        <input type="text" id="fullname" name="fullname"
            name="fullname" required>
        <br><br>
        
        <label for="username">Username:</label> 
        <input type="text" id="username" name"username" 
            name="" required> 
        <br><br>
            
        <label for="password">Password:</label> 
        <input type="password" id="password" name="password" 
            name="password" minlength="8" required> 
        <br><br>
                
        <label for="confirm">Confirm Password:</label>
        <input type="password" id="confirm" 
            name="confirm" required> 
        <br><br>
        
        <input tupe="submit" value="Register">
    </form>
    """
    
    return render_template_string(form_html)

# POST: process registration form.  
@app.route("/register", methods=["POST"])
def register(): 
    
    fullname = request.form.get("fullname", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    confirm = request.form.get("confirm", "")
    
    # Validate equired fields. 
    if not fullname or not username or not password or not confirm: 
        return "ERROR: All fields required.", 400 
    
    # Valeidate username. 
    if not re.fullmatch(r"[A-Za-z0-9_]+", username): 
        return "ERROR: Use only letters numbers and underscores.", 400
    
    # Validate password length.
    if len(password) < 8: 
        return "ERROR: Password must be at least 8 characters.", 400
    
    # Validate password characters. 
    if not re.fullmatch(r"[A-Za-z-0-9]+", password): 
        return "ERROR: Only use letters or numbers.", 400
    
    # Password requirement. 
    if not re.search(r"[A-Za-z]", password) or not re.search(r"[0-9]", password): 
        return "ERROR: Password must include at least one letter and one number.", 400
    
    # Confirm passwords match. 
    if password != confirm: 
        return "ERROR: Passwords don't match.", 400
    
    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")
    
        
    return (
        f"Registration Successfull!" <br>
        f"Full Name: {fullname}" <br>
        f"Username: {username}" <br>
        f"Password: {password}" <br>
        f"Confirm Password: {confirm}"
    )


if __name__ == "__main__": 
    app.run(debug=True, port="5050")
