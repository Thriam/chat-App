from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__, template_folder='templates')

# Initialize a secure password
secure_password = 'your_secure_password'
@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form['sender']
    message = request.form['message']
    with open('chat.txt', 'a') as chat_file:
        chat_file.write(f'{sender}: {message}\n')
    return 'Message sent'

@app.route('/get_messages')
def get_messages():
    with open('chat.txt', 'r') as chat_file:
        chat = chat_file.read()
    return chat

@app.route('/delete_chat', methods=['POST'])
def delete_chat():
    password = request.form['password']
    
    if password == secure_password:
        # Delete the chat messages by overwriting the file
        with open('chat.txt', 'w') as chat_file:
            chat_file.write('')
        return 'Chat deleted'
    else:
        return 'Access denied', 403

@app.route('/qazwsxedc1234', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        # Update the password from the new password provided
        with open('password.txt', 'w') as password_file:
            password_file.write(new_password)
        return 'Password changed successfully'
    else:
        return render_template('qazwsxedc1234.html')

if __name__ == '__main__':
    # Load the initial password from the password file
    try:
        with open('password.txt', 'r') as password_file:
            secure_password = password_file.read().strip()
    except FileNotFoundError:
        pass  # Handle the case when the password file doesn't exist

    app.run(debug=True,host='0.0.0.0', port=8088)

