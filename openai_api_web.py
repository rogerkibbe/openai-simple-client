import os
import openai
import panel as pn
from dotenv import load_dotenv

pn.extension()

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": contents}],
    #     stream=True,
    # )

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": contents}],
        stream=True,
    )

    message = ""
    for chunk in response:
        message += chunk["choices"][0]["delta"].get("content", "")
        yield message


chat_interface = pn.chat.ChatInterface(callback=callback, callback_user="ChatGPT")
chat_interface.send(
    "Send a message to get a reply from ChatGPT!", user="System", respond=False
)
chat_interface.servable()