
import openai
from openai import Completion
import tkinter as tk

# Set up the OpenAI API client
openai.api_key = "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"

# Create the main window
root = tk.Tk()
root.title("ChatGPT App")

# Create a text entry field and a send button
entry = tk.Entry(root)


# Create a text widget to display the conversation
conversation = tk.Text(root)

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
send_button = tk.Button(root, text="Send", command=send_message)
# Pack the widgets into the window
entry.pack()
send_button.pack()
conversation.pack()

# Run the Tkinter event loop
root.mainloop()
