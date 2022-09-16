import gpt
import requests
import pyvips

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
        self.svg_to_png("./temp/latex.svg")

    def svg_to_png(self, svg):
        image = pyvips.Image.new_from_file(svg, dpi=300)
        image.write_to_file("./temp/latex.png")


    def latex(self, input):
        tex = self.gpt.latex(input)
        self.tex_to_png(tex)

zelda = Zelda()
zelda.latex(input("Command: "))
