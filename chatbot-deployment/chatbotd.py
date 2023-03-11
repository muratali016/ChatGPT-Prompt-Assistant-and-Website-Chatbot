import openai
from openai import Completion




# Set up the speech recognition module

# Set up the OpenAI API client
openai.api_key = "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"

# Create a function to send a message to ChatGPT and display the response
message = ""


def send_message(message):
    # Use the OpenAI API to get a response from ChatGPT
    response = Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=1024,
        temperature=0.5,
    )
    text= response.get('choices')[0].get('text')
    return text







