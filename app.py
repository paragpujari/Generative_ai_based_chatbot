from flask import Flask, request, render_template,jsonify
import google.generativeai as genai # type: ignore
import os

# Set the key for generative API
os.environ["GOOGLE_API_KEY"] = "AIzaSyCN2kISIHbZGcTRkN89thAf5k7J9epGRis"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# Initialize the model
model = genai.GenerativeModel("models/gemini-pro")


# create an object for Flask app
app = Flask(__name__)


# Store chats in memory in a database

# First Default Chat
chats = [{'name': 'New Chat', 'id': 1, 'messages': []}]  

def AIResponse(prompt, chat_history=None):

    # If there is any chat history, append it to the current prompt
    if chat_history:
        context = "\n".join(
            [f"User: {msg['text']}" if msg['text'].startswith('User') else f"AI: {msg['text']}" for msg in
             chat_history])
        prompt = f"{context}\nUser: {prompt}\nAI:"             # generates the previous message of the input text

    # Generate the AI response
    response = model.generate_content(prompt)                  # contains the previous and current input message and generates the response.

    # Return only the new AI response
    return response.text


# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# get all the chats
@app.route("/get_chats",methods=['GET'])
def get_chats():
    return jsonify({'chats':chats})

# get the history of all the chats
@app.route("/get_chat_history",methods=['GET'])
def get_chat_history():
    chat_id = int(request.args.get('chat_id'))                                         # get the chat_id
    chat = next((chat for chat in chats if chat['id']==chat_id),None)                  # get all the chat one by one if the chat_id we are getting is present in the default chat
    if chat:
        return jsonify({'messages': chat['messages']})                                 # if the chat id we have obtained is present in the default list, then return all the chat messages   
    return jsonify({'messages':[]})


# Updated route for generating AI responses
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()                                                         # request the data from the server
    user_input = data.get('input')                                                    # get the user input   
    chat_id    = data.get('chat_id')                                                  # get the chat id


    # Find the relevant chat and get the chat history
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)              # Find the relevant chat
    chat_history = chat['messages'] if chat else []                                   # get the chat history for the related chat

    # generate the AI response
    response = AIResponse(user_input, chat_history)

    # Append user input and AI response to the chat history
    if chat:
        chat['messages'].append({'text': f'User: {user_input}'})
        chat['messages'].append({'text': f'AI: {response}'})

    return jsonify({'response': response})


# Route to create a new chat
@app.route('/new_chat', methods=['POST'])
def new_chat():
    data = request.get_json()                                                          # request the data from the server
    chat_name = data.get('chat_name')                                                  # get the chat name
    new_chat_id = len(chats) + 1                                                       # get the new chat id
    new_chat = {'name': chat_name, 'id': new_chat_id, 'messages': []}                  # create a new chat by adding chat name and chat id
    chats.append(new_chat)                                                             # append the chat to the default chat
    return jsonify({'status': 'Chat created successfully', 'chat_id': new_chat_id})    # return the chat message

# Route to delete a chat
@app.route('/delete_chat', methods=['POST'])
def delete_chat():
    data = request.get_json()                                                         # request the data from the server
    chat_id = data.get('chat_id')                                                     # get the data chat id
    global chats                                                                      # make the default chat list as global
    chats = [chat for chat in chats if chat['id'] != chat_id]                         # check if the chat id obtained is not present in the default list
    return jsonify({'status': f'Chat {chat_id} deleted successfully'})                # return the message that the chat has been deleted successfully.

if __name__ == '__main__':
    app.run(debug=True)
