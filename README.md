
# OpenAI Simple Client

This project is a simple web-based chat interface that allows users to interact with OpenAI's GPT-3.5 and GPT-4 models. It's built using Python and integrates the OpenAI API for generating responses.

## Features

- Model Selection: Choose between GPT-3.5-turbo and GPT-4 models.
- Customizable Interaction: Adjust the temperature and top_p values to fine-tune the responses.
- Real-time Chat Interface: Engage in a conversation with the AI model with a user-friendly chat interface.

## Installation

Before you start, make sure you have Python 3.8 or higher installed on your system.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rogerkibbe/openai-simple-client.git
   cd openai-simple-client
   ```

2. **Install Dependencies**
   - It's recommended to use a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

This python app uses [Panel](https://panel.holoviz.org/) so, run the application using:

```bash
panel serve openai_api_web.py
```

Open your web browser and navigate to the address provided in the console to interact with the chat interface.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/rogerkibbe/openai-simple-client/issues) if you want to contribute.

## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.

## Contact

Roger Kibbe - [LinkedIn](https://www.linkedin.com/in/rkibbe/)

Project Link: [https://github.com/rogerkibbe/openai-simple-client](https://github.com/rogerkibbe/openai-simple-client)

