import os
import openai
import panel as pn
from dotenv import load_dotenv

pn.extension()
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.AsyncOpenAI(api_key=openai_api_key)


def app_layout():
    model_selector = pn.widgets.Select(name='Select Model', options=[
        'gpt-3.5-turbo', 'gpt-4'], value='gpt-4')
    temperature_slider = pn.widgets.FloatSlider(name='Temperature', start=0.0, end=1.0, step=0.01, value=0.7)
    top_p_slider = pn.widgets.FloatSlider(name='top_p', start=0.0, end=1.0, step=0.1, value=1.0)

    chat_history = []

    async def handle_user_message(contents: str, user: str, chat_instance: pn.chat.ChatInterface):
        nonlocal chat_history
        chat_history.append({"role": "user", "content": contents})

        model_name = model_selector.value
        temperature = temperature_slider.value
        top_p = top_p_slider.value

        chat_interface.callback_user = model_name

        try:
            # print("Calling OpenAI with model: " + model_name + " temperature: " + str(temperature) + " top_p: " + str(top_p))
            response = await client.chat.completions.create(
                model=model_name,
                messages=chat_history,
                temperature=temperature,
                top_p=top_p,
                stream=True,
            )
        except Exception as e:
            print(f"Error in generating response: {e}")
            return

        accumulated_response = ""
        async for chunk in response:
            part = chunk.choices[0].delta.content
            if part is not None:
                accumulated_response += part
                yield accumulated_response

        chat_history.append({"role": "assistant", "content": accumulated_response})

    print("creating chat interface")
    chat_interface = pn.chat.ChatInterface(callback=handle_user_message, callback_user="OpenAI", show_undo=False, show_clear=False)
    chat_interface.send("Send a message to get a reply from ChatGPT!", user="System", respond=False)

    # Configuration column on the right
    config_column = pn.Column(model_selector, temperature_slider, top_p_slider)

    # Vertical line
    vertical_separator = pn.Spacer(width=3, sizing_mode='stretch_height', styles={'background': 'black'})

    # app layout
    app_header = pn.pane.Markdown("# OpenAI Simple Client - (Github)[https://github.com/rogerkibbe/openai-simple-client]", align="center")
    return pn.Column(
        app_header,
        pn.Row(
            chat_interface,
            vertical_separator,
            config_column
        )
    )


# Serve the app layout
app_layout().servable()