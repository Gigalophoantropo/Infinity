from Functions import *
from manim import*

'''N = [int(input("Type the first natural number"))]
N.append(int(input("Type the second natural number")))

#print(NtoQ(N))


#print(NtoQplus(N))

class Exp(Scene):
    def construct(self):

        ax = Axes(
            x_range = [0, 2072, 518],
            y_range = [0, 1084, 296],
            tips = False,
            axis_config = {
                "include_numbers": True,
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0
                }
            }
        )
        
        lab = ax.get_axis_labels(
            x_label = MathTex("n"),
            y_label = MathTex("a_n")
        )

        SDSg = VGroup(*[
            Dot(ax.coords_to_point(n, SternsDiatomicSeries(n)), radius = 0.005, color = BLUE)
            for n in range(1024)
        ])

        self.add(SDSg, ax, lab)


def SEA(a: list):
            if a[0] > a[1]:
                return [a[0]-a[1], a[1]]
            elif a[0] < a[1]:
                return [a[0], a[1]-a[0]]
            else:
                return a

print(SEA(N))


class SquareSeries(Scene):
    def construct(self):
        S = Square(side_length = 6)
        self.add(S)


a = ["jijijija", "jedniwnsd", "wejneo"]
a.pop(-1)
print(a)'''
"""A = [2, 4]
class Ex(Scene):
    def construct(self):
        def Speak(GoofyAhhSpeaker: ImageMobject, Text: list):
            for g in Text:
                for go in range(g):
                    self.play(GoofyAhhSpeaker.animate.shift(UP/8), run_time = 0.1), self.play(GoofyAhhSpeaker.animate.shift(DOWN/8), run_time = 0.1)
                if g != Text[-1]:
                    self.wait(0.4)

        Speak(ImageMobject("NerdFace.png"), [8, 4])"""


'''class Ex(Scene):
    def construct(self):
        def Speak2(GoofyAhhSkin1: ImageMobject, GoofyAhhSkin2: ImageMobject, Text: list):
            for g in Text:
                for go in range(g):
                    self.add(GoofyAhhSkin1, run_time = 1)
                if g != Text[-1]:
                    self.wait(0.4)'''

'''print(summation(lambda i: (1/2)**i, i=1))'''