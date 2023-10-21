from manim import *
from Functions import *


class cardinalNZQ(Scene):
    def construct(self):

        NZ = MathTex(r"|\mathbb N| = |\mathbb Q|")

        Qplus = MathTex(r"\mathbb Q^+ = \{q \in \mathbb Q | q>0\}")

        NQplus = MathTex(r"|\mathbb Z^+| = |\mathbb Q^+|")

        SDS1 = MathTex(r"a_0 = 0")
        SDS2 = MathTex(r"a_1 = 1")
        SDS3 = MathTex(r"a_{2n} = a_n")
        SDS4 = MathTex(r"a_{2n + 1} = a_n + a_{n + 1}")
        SDSt = Text("Stern's diatomic series", font = "Times New Roman").move_to(3*UP).scale(3/2).set_color(YELLOW)

        SDS = VGroup(SDS1, SDS2, SDS3, SDS4).arrange_in_grid(rows = 4, buff = 0.75).move_to(DOWN)

        ax = Axes(
            x_range = [0, 1024, 256],
            y_range = [0, 80, 20],
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
            Dot(ax.coords_to_point(n, SternsDiatomicSeries(n)), radius = 0.02, color = BLUE)
            for n in range(1024)
        ])

        ZplustoQplusf = MathTex(r"g(n) = \frac{a_n}{a_{n + 1}}")
        ZplustoQplus = MathTex(r"\mathbb Z^+ \rightarrow \mathbb Q^+")

        Eq = MathTex(r"[a_n, a_{n+1}] \Rightarrow \frac{a_n}{a_{n+1}}").scale(1/2).shift(DOWN)
        L = MathTex(r"L = [1, 1], [1, 2], [2, 1], [1, 3], \cdots, [a_n, a_{n + 1}], \cdots")

        def SEA(a: list):
            if a[0] > a[1]:
                return [a[0]-a[1], a[1]]
            else:
                return [a[0], a[1]-a[0]]

        SEAe = MathTex(r"[8, 3] \rightarrow [5, 3] \rightarrow [2, 3] \rightarrow [2, 1] \rightarrow [1,1]")
        SEAt = Text("SEA:").scale((3/2)).shift(3*UP).set_color(YELLOW)

        abgmcdab = MathTex(r"a<b; g = m.c.d(a, b)").shift(UP)
        gmcdaba = MathTex(r"g = m.c.d(a, b-a)")

        SEAfab = MathTex(r"[a, b] \rightarrow \cdots \rightarrow [g, g], g = m.c.d(a, b)").shift(DOWN)

        Ln = MathTex(r"L_n = [a_n, a_{n+1}]")

        box = SurroundingRectangle(Ln, corner_radius = 0.2).to_corner(UL)

        SEAln = MathTex(r"SEA: L_{2n}, L_{2n + 1} \rightarrow L_n")

        func = MathTex("g(n)").shift(5*RIGHT + 2*DOWN)
        fNZ = MathTex(r"f(n) = \frac{1 + (-1)^n(2n-1)}{4}").shift(3*DOWN + LEFT)

        NZQ = MathTex(r"|\mathbb N|=|\mathbb Z|=|\mathbb Q|=\aleph_0")
        

        self.play(Write(NZ))
        self.pause()

        self.play(Unwrite(NZ))
        self.play(Write(Qplus))
        self.play(Qplus.animate.scale(2))
        self.pause()

        self.play(Qplus.animate.shift(2*UP))
        self.play(Write(NQplus))
        self.play(NQplus.animate.scale(2))
        self.play(NQplus.animate.shift(2*DOWN))
        self.pause()

        self.play(Unwrite(Qplus), Unwrite(NQplus))
        self.pause()

        self.play(Write(SDSt))
        self.play(Write(SDS))

        self.play(Unwrite(SDSt), Unwrite(SDS))

        self.play(Create(SDSg), Write(lab), Create(ax), run_time = 32)
        self.play(FadeOut(SDSg), Unwrite(lab), Uncreate(ax), run_time = 3)
        self.play(Write(ZplustoQplusf), ZplustoQplusf.animate.scale(2), ZplustoQplusf.animate.shift(DOWN), run_time = 3)
        self.play(
            Write(ZplustoQplus), ZplustoQplus.animate.scale(3/2), ZplustoQplus.animate.shift(UP), run_time = 6
        )

        self.play(Uncreate(ZplustoQplus), Uncreate(ZplustoQplusf), run_time = 2)

        self.play(Write(L), run_time = 2)
        self.play(FadeIn(Eq))
        self.play(Uncreate(Eq), FadeOut(L))
        
        self.play(Write(SEAe), Write(SEAt), run_time = 2)
        self.play(Unwrite(SEAe), Unwrite(SEAt), run_time = 2)
        
        self.play(Write(abgmcdab), Write(gmcdaba), Write(SEAfab), run_time = 3)
        self.play(Unwrite(abgmcdab), Unwrite(gmcdaba), Unwrite(SEAfab))


        self.play(Write(Ln))
        self.play(Ln.animate.scale(1/2).shift(box.get_center()), run_time = 3)
        self.play(Create(box))
        

        """self.play(Write(Qplus))
        self.play(Qplus.animate.shift(UP))
        self.pause()

        self.play(Write(NZQ), NZQ.animate.scale(3), run_time = 3)"""

        self.wait()
