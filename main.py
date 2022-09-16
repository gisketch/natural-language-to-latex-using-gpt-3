import gpt
import requests
import io
import matplotlib.pyplot as plt
from PIL import Image, ImageChops

class Zelda:
    def __init__(self):
        self.gpt = gpt.GPT()

    def write_text(self, data: str, path: str):
        with open(path, 'w') as file:
            file.write(data)

    def save_svg(self, str): #function that saves txt to tex to png
        url = "https://math.vercel.app/?from=" + str
        svg = requests.get(url).text
        self.write_text(svg, "./temp/latex.svg")
    
    def latex_to_img(self, tex):
        plt.rc('text', usetex=False)
        plt.axis('off')
        plt.text(0.05, 0.5, f'${tex}$', size=60)
        # plt.savefig("img.png", format='png')
        plt.show()
        plt.close()

    def latex(self, input):
        self.latex_to_img(input)

zelda = Zelda()
latexgpt = zelda.gpt.Latex_GPT(input("Command: "))
print(latexgpt.response + " " + latexgpt.latex)
zelda.latex_to_img(latexgpt.latex)
