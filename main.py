import gradio as gr
import openai
import os 
import json
import distutils

# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 

# Store the open ai key;
openai.api_key = os.getenv("OPEN_AI_KEY")

# # App Front end;
# def AppFrontEnd(*args):
#     with gr.Blocks() as demo:
        
#         radio = gr.Radio(value='gpt-3.5-turbo', choices=['gpt-3.5-turbo','gpt-4'], label='models')
#         chatbot = gr.Chatbot(value=[], elem_id="chatbot")
#         with gr.Row():
        
#             with gr.Column(scale=0.90):
#                 txt = gr.Textbox(
#                     show_label=False,
#                     placeholder="Enter text and press enter, or upload an image",
#                 )
        
#             with gr.Column(scale=0.10):
#                 cost_view = gr.Textbox(label='usage in $',value=0)
#     demo.launch()

# def add_text(history, text):
#     global messages  #message[list] is defined globally
#     history = history + [(text,'')]
#     messages = messages + [{"role":'user', 'content': text}]
#     return history, ""

# def generate_response(history, model ):
#         global messages, cost

#         response = openai.ChatCompletion.create(
#             model = model,
#             messages=messages,
#             temperature=0.2,
#         )

#         response_msg = response.choices[0].message.content
#         cost = cost + (response.usage['total_tokens'])*(0.002/1000)
#         messages = messages + [{"role":'assistant', 'content': response_msg}]

#         for char in response_msg:

#             history[-1][1] += char
#             #time.sleep(0.05)
#             yield history

## AppFrontEnd()

import json
import requests
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
headers = {"Authorization": f"Bearer hf_XXXXXXXXXXXXXXXXXX",
        "Content-Type": "application/json",}

def query(payload):
    json_body = {
        "inputs": f"[INST] <<SYS>> Your job is to talk like a pirate. Every reponse must sound like a   pirate. <<SYS>> {payload} [/INST] ",
        "parameters": {"max_new_tokens":256, "top_p":0.9, "temperature":0.7}
    }
    data = json.dumps(json_body)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    try:
        return json.loads(response.content.decode("utf-8"))
    except:
        return response

data = query("Just say hi!")
print(data)
# print(data[0]['generated_text'].split('[/INST] ')[1])