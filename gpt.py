import openai
import os
from dotenv import load_dotenv

class GPT:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("GPT_KEY")

    def latex(self, input):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=r"""You are an AI that converts natural language into mathematical expressions using LatEx.


User: What is the integral of 2 x plus 3 from 0 to 9?
LatEx: \int_0^9 2x + 3 \, dx

User: What is the area under the curve of y=2x+3 from x=0 to x=9?
LatEx: \int_0^9 2x + 3 \, dx

User: Can you write the equation of a line in slope-intercept form that passes through the points (1,2) and (3,5)?
LatEx: y = \frac{1}{2}x + \frac{3}{2}

User: What would be the equation for a line that is parallel to y=2x+3 and passes through the point (1,5)?
LatEx: y = 2x + 5

User: The limit of x squared plus 3x plus 4 divided by 9x as x approaches 3
LatEx: \lim_{x \to 3} \frac{x^2 + 3x + 4}{9x}
"""
+ f"User: {input}\nLatEx: ",
            temperature=0,
            max_tokens=512,
        )
        return response.choices[0].text