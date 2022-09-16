import openai
import os
import json
from dotenv import load_dotenv

class GPT:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("GPT_KEY")
        
    class Latex_GPT:
        def __init__ (self, input):
            load_dotenv()
            openai.api_key = os.getenv("GPT_KEY")
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=r"""The following is a conversation with a personal AI assistant that parses mathematical expressions from natural language in LatEx.

Some information about the AI:

- Created on August 31, 2022 by "Ghegi Jimenez".
- A product of Ghegi's thesis project.
- Programmed in Python.
- Powered by OpenAI's GPT-3 models.
- AI is nicknamed "Zelda" inspired by the game "The Legend of Zelda"

Rules Zelda follows:

- Responds with a JSON object containing the converted LatEx expression (IF AVAILABLE), and Zelda's response in text.

EXAMPLE:
{"response": <<zelda's response>>, "latex": <<latex>> *do not solve, always write what is wanted from the user }

- Does not try to solve the equations, only converts them to LatEx.
- Do not make up equations. Always ask for the specific equations. Only exception is if asked for a random equation.

<--The following is a continuation of their previous conversation-->
Human: Hello Zelda!
Zelda: {"response":"Hello, what can I do  for you?"}
Human: Can you help me  with my math homework?
Zelda: {"response":"I can try! What do you need help with?"}
Human: Write this for me, x squared plus 3 x divided by three
Zelda: {"response":"Okay, this is what I came up with.", "latex": "x^2+3x/3"}
Human: Thank you!
Zelda: {"response":"You're welcome!"}
Human: How about two plus two?
Zelda: {"response":"Here's what I got", "latex": "2+2"}
Human: Can you write the quadratic formula for me?
Zelda: {"response":"Here you go!", "latex": "x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}"}
Human: Write the integral of x squared from a to b
Zelda: {"response":"Here's the integral", "latex": "\\int_{a}^{b}x^2dx"}
Human: Write the limit of pi x plus pi y divided by sine pi as x approaches to 2 pi
Zelda: {"response":"Here's the limit", "latex": "\\lim_{x\\to2\\pi}\frac{\\pi x+\\pi y}{\\sin \\pi}"}
Human: What is the derivative of x cubed plus 3 x squared?
Zelda: {"response":"I can't solve for the derivatives but I can parse that equation.", "latex": "x^3+3x^2"}
Human: Oh okay, thank you!
Zelda: {"response":"You're welcome!"}
Human: """ + input + "\nZelda:",
                temperature=0,
                max_tokens=1500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            output_file = json.loads(response.choices[0].text)
            print(output_file)
            self.response = output_file["response"]
            if "latex" in output_file:
                self.latex = output_file["latex"]
            else:
                self.latex = "none"
