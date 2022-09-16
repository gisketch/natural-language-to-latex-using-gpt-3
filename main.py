import gpt
import requests
import os

class Zelda:
    def __init__(self):
        self.gpt = gpt.GPT()

    def write_text(self, data: str, path: str):
        with open(path, 'w') as file:
            file.write(data)

    def tex_to_png(self, str): #function that saves txt to tex to png
        url = "https://math.vercel.app/?from=" + str.replace(" ", "%20").replace("+", "%2B")
        svg = requests.get(url).text
        self.write_text(svg, "./temp/latex.svg")

    def latex(self, input):
        tex = self.gpt.latex(input)
        self.tex_to_png(tex)

zelda = Zelda()
zelda.latex(input("Command: "))
