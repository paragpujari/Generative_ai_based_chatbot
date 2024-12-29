# Generative AI Based Chat Bot:
Chat Bot is a powerful-based AI tool that is used to take the input from the user, understand the input text, process it and give the response back to the user.  It can understand process and respond the text or voice in real time scenario. It provides many helpful information, automating the tasks and felicitating the communication.

## Features of Chat Bot:
1.	Chat Bot provides 24 * 7 availability ensuring that the customer gets support any time.
2.	It solves all the complex queries within a fraction of seconds thus; it saves the time and space and saves the cost for solving the problems.
3.	It solves all the complex problems within a shorter period with accurate results and thus increases its productivity.
4.	It solves n number of problems within few seconds thus makes them ideal support for scaling customer support during rapid growth.
5.	It replies to all the queries of the users by providing the responses of the request send by the user and keeps the users engaged.
6.	It can quickly analyse the data and provide the insights for the data within a short span of time and is used for fast decision-making.
7.	It collects the data and provides insights for the data.
8.	It can communicate to the users in multiple languages and thus enables the business to cater to a global audience.
9.	It consistently replies to all the queries send by the users.
10.	It makes the digital services more accessible to the users to deal with the persons with disabilities.

## Evolution of Chat Bot:

###  EARLY CHAT BOTS (1960 – 1980): Rule Based Systems
These chat bots are based on certain predefined rules.
These chat bots lack conversational ability
These chat bots lack real time understanding.
They can solve only simple queries.

### 1.	ELIZA:
a.	It was the first chat bot established in the year 1966.
b.	It was used for pattern matching
c.	It is used to mimic a psychotherapist.
d.	It cannot understand the text or solve any of the complex queries.

### 2.	PARRY:
a.	It was the second chat bot established in the year 1972.
b.	It enables the user to communicate with paranoid schizophrenia.
c.	It is much advanced than Eliza incorporating human emotion.

### EXPERT SYSTEMS (1980 – 1990): Task Oriented Chatbots
These chat bots are integrated into expert systems.
It focused on industries.
It is heavily dependent on predefined rules and decision trees.
Challenges:
It is unable to handle complex queries.
It requires constant updates into the rule base.



### The Rise of Machine Learning (2000s): Smarter Chatbots
These chat bots are integrated with machine learning to improve its functionalities.
Here NLP is also added into the chat bots to improve its performance.
It can solve complex problems.
Challenges:
It lacked deep understanding.
It requires significant data for training.

### The AI Revolution (2010s): Intelligent Virtual Assistants
These AI powered chat bots are integrated with deep learning and advance NLP.
It requires integration with cloud computing, large datasets and image processing.

It can solve complex queries.
Ex = Siri, Amazon Alexa 

Challenges:
Privacy concerns with the data usage.


### Current Era (2020s): Conversational AI and Multimodal Chatbots

Generative AI is integrated into the chat bots.
Large Language Models (LLM) is integrated into the chatbots.
It can solve complex queries and can understand the natural language based processing text.


# Objective:

The main motto of this project is to build an AI based Chat Bot that can take the input message and give the response with respect to the message given.

# Problem Statement:

Chat Bot is a powerful-based AI tool that takes the input from the user, understand the input text, process it and give the response back to the user.  So Chat bot is used to felicitate the seamless communication between the humans and digital systems. Thus, we can save the time, improve user experiences and optimize the processes.


It can be integrated into platforms like WhatsApp, Microsoft Teams etc.
It is widely used in health care, education etc.

# Algorithm:
1.	First, the generative API key is configured.
2.	Then all the models have been listed for the Generative AI.
3.	Gemini-pro model is preferred, as it is used for scaling across a wide range of tasks.
4.	A particular text is considered and content is generated from the text provided using generative ai.
   (i)	We have taken the text and applied the generative ai algorithm in it.

   (ii)	Then generate_content function is applied on the text. This function generates the answer message from the text.

   (iii)	Then text is used that extracts only text from the prompt information.

5.	Chat Bot website is created. 
   (i)	A key is set for the generative API.

  (ii)	Model named ‘gemini-pro’ is created and initialized using the library of generative Model.

  (iii)	Default Chat is made that has the initial chat id, the chat name, and the chat message.

  (iv)	‘/’ app.route function is used that is used to navigate to the main page.

  (v)	‘/get_chats’ app.route function is used to get all the chats.

  (vi)	‘/get_chat_history’ app.route function is used to get the history of all the chats.

          a.	Get the chat id
          b.	Scan through the default chat and check if the chat id is present in it
          c.	If found print the chat message with respect to the chat is found.
          d.	Print the history of all the chat messages for the entire chat id.

(vii)	‘/new_chat’ app.route function is used to create the new chats.

          a.	request the data from the server   
          b.	get the chat name
          c.	get the new chat id
          d.	create a new chat by adding chat name and chat id
          e.	append the chat to the default chat
          f.	return the chat message
          
(viii)	‘/delete_chat’ app.route function is used to create the new chats.

          a.	request the data from the server
          b.	get the data chat id
          c.	make the default chat list as global
          d.	check if the chat id obtained is not present in the default list
          e.	return the message that the chat has been deleted successfully.

(ix)	‘/generate’ app.route function is used to generate the AI based messages based on the input text provided.
          a.	request the data from the server
          b.	get the user input
          c.	 get the chat id
          d.	 Find the relevant chat and get the chat history

e.	# generate the AI response
f.	use AIResponse function to generate the AI response
g.	If there is any chat history, append it to the current prompt and  it generates the previous message of the input text
h.	def AIResponse -> Generate the AI response that contains the current response and the previous response of the input message.
i.	Return only the new AI response in text format
j.	Append user input and AI response to the chat history

# Algorithms Used:
  1.	Generative Model

# Hyper Parameters Used:
  1.	Name -> chat name
  2.	Id      ->  chat id
  3.	Messages -> chat message
