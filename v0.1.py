import openai
from openai import Completion
import tkinter as tk

# Set up the OpenAI API client
openai.api_key = "Your API key"

# Create the main window
root = tk.Tk()
root.title("ChatGPT App")
root.configure(bg='light blue')

# Create a text entry field and a send button
entry = tk.Entry(root, font=('Arial', 14), bg='white', fg='black')

# Create a text widget to display the conversation
conversation = tk.Text(root, font=('Arial', 14), bg='white', fg='black')

# Create a scrollbar for the conversation widget
scrollbar = tk.Scrollbar(root, orient='vertical', command=conversation.yview)
conversation['yscrollcommand'] = scrollbar.set

# Create a function to clear the conversation widget
def clear_conversation():
    conversation.delete('1.0', 'end')

# Create a function to send a message to ChatGPT and display the response
def send_message():
    # Get the message from the entry field
    message = entry.get()

    # Clear the entry field
    entry.delete(0, "end")

    # Use the OpenAI API to get a response from ChatGPT
    response = Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        temperature=0.5,
    )

    # Display the message and the response in the conversation widget
    conversation.insert("end", f"You: {message}\n")
    conversation.insert("end", f"Bot: {response.get('choices')[0].get('text')}\n")

# Create the send button
send_button = tk.Button(root, text="Send", font=('Arial', 14), command=send_message, bg='white', fg='black')

# Create the clear button
clear_button = tk.Button(root, text='Clear', command=clear_conversation, bg='white', fg='black')

# Pack the widgets into the window
entry.pack()
send_button.pack()
clear_button.pack()
conversation.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# Run the Tkinter event loop
root.mainloop()
