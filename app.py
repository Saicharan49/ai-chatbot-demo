!pip install openai gradio  # Install libraries

import openai
import gradio as gr

# Set your OpenAI API key (get it from: https://platform.openai.com/api-keys)
openai.api_key = "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"  # Replace with your key

def chatbot(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

# Create a web interface
gr.Interface(fn=chatbot, inputs="textbox", outputs="textbox").launch(share=True) 
