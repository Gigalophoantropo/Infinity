from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP


class cardinalNZQ(PresentationScene):
    def construct(self):

        NZ = MathTex(r"|\mathbb N| = |\mathbb Q|")

        Qplus = MathTex(r"\mathbb Q^+ = \{q \in \mathbb Q | q>0\}")

        NQplus = MathTex(r"|\mathbb N| = |\mathbb Q^+|")


        fracs = VGroup(*[
            MathTex(f"\\frac{1}{y+1}")
            for y in range(4)
        ]).arrange(buff = 3).shift(3*UP)

        fracs2 = VGroup(*[
            MathTex(f"\\frac{2}{y+1}")
            for y in range(4)
        ]).arrange(buff = 3).shift((3/2)*UP)
        
        fracs3 = VGroup(*[
            MathTex(f"\\frac{3}{y+1}")
            for y in range(4)
        ]).arrange(buff = 3)

        fracs4 = VGroup(*[
            MathTex(f"\\frac{4}{y+1}")
            for y in range(4)
        ]).arrange(buff = 3).shift((3/2)*DOWN)

        Frac = VGroup(*[fracs, fracs2, fracs3, fracs4])
        Frac.to_corner().shift(UP)

        cdots = VGroup(*[MathTex("\cdots") for s in range(0, 4)])
        cdots.arrange_in_grid(rows = 4,buff = 1.5).shift(Frac.get_right() + 2*RIGHT)
        vdots = VGroup(*[MathTex(r"\vdots") for s in range(0, 4)])
        vdots.arrange_in_grid(rows = 1,buff = 3.25).shift(Frac.get_bottom() + DOWN)

        o = MathTex("1").shift(Frac[0][0].get_corner(UR) + (1/4)*UR)
        t = MathTex("2").shift(Frac[0][1].get_corner(UR) + (1/4)*UR)
        th = MathTex("3").shift(Frac[1][0].get_corner(UR)+ (1/4)*UR)
        f = MathTex("4").shift(Frac[2][0].get_corner(UR) + (1/4)*UR)
        fi = MathTex("5").shift(Frac[0][2].get_corner(UR) + (1/4)*UR)
        s = MathTex("6").shift(Frac[0][3].get_corner(UR)+ (1/4)*UR)
        se = MathTex("7").shift(Frac[1][2].get_corner(UR) + (1/4)*UR)
        e = MathTex("8").shift(Frac[2][1].get_corner(UR) + (1/4)*UR)
        n = MathTex("9").shift(Frac[3][0].get_corner(UR)+ (1/4)*UR)

        Arrow1 = Arrow(
            start = Frac[0][0].get_right() + (0.125)**(1/2)*RIGHT,
            end = Frac[0][1].get_left() + (0.125)**(1/2)*LEFT
        )
        Arrow2 = Arrow(
            start = Frac[0][1].get_left() + (0.125)**(1/2)*LEFT,
            end = Frac[1][0].get_right() + (0.125)**(1/2)*RIGHT
        )
        Arrow3 = Arrow(
            start = Frac[2][0].get_top() + (0.125)**(1/2)*UP,
            end = Frac[1][0].get_bottom() + (0.125)**(1/2)*DOWN
        )

        Arrow4 = Arrow(
            start = Frac[2][0].get_right() + (0.125)**(1/2)*RIGHT,
            end = Frac[1][1].get_left() + (0.125)**(1/2)*LEFT
        )

        Arrow5 = Arrow(
            start = Frac[2][0].get_right() + (0.125)**(1/2)*RIGHT,
            end = Frac[0][2].get_left() + (0.125)**(1/2)*LEFT
        )

        Arrow6 = Arrow(
            start = Frac[0][2].get_right() + (0.125)**(1/2)*RIGHT,
            end = Frac[0][3].get_left() + (0.125)**(1/2)*LEFT
        )

        Arrow7 = Arrow(
            start = Frac[0][3].get_left() + (0.125)**(1/2)*LEFT,
            end = Frac[1][2].get_right() + (0.125)**(1/2)*RIGHT
        )

        Arrow8 = Arrow(
            start = Frac[1][2].get_left() + (0.125)**(1/2)*LEFT,
            end = Frac[2][1].get_right() + (0.125)**(1/2)*RIGHT
        )

        Arrow9 = Arrow(
            start = Frac[2][1].get_left() + (0.125)**(1/2)*LEFT,
            end = Frac[3][0].get_right() + (0.125)**(1/2)*RIGHT
        )

        l = Line(
            start = Frac[1][1].get_corner(DL),
            end = Frac[1][1].get_corner(UR)
        ).set_color(RED)

        A = VGroup(
            Arrow1, Arrow2, Arrow3, Arrow4, Arrow5, Arrow6, Arrow7, Arrow8, Arrow9
        )
        A.set_color(BLUE)
        B = VGroup(A, l, Frac, o, t, th, f, fi, s, se, e, n, cdots, vdots)

        func = MathTex("g(n)").shift(5*RIGHT + 2*DOWN)
        fNZ = MathTex(r"f(n) = \frac{1 + (-1)^n(2n-1)}{4}").shift(3*DOWN + LEFT)

        NZQ = MathTex(r"|\mathbb N|=|\mathbb Z|=|\mathbb Q|=\aleph_0")
        

        self.play(Write(NZ))
        self.end_fragment()

        self.play(Unwrite(NZ))
        self.play(Write(Qplus))
        self.play(Qplus.animate.scale(2))
        self.end_fragment()

        self.play(Qplus.animate.shift(2*UP))
        self.play(Write(NQplus))
        self.play(NQplus.animate.scale(2))
        self.play(NQplus.animate.shift(2*DOWN))
        self.end_fragment()

        self.play(Unwrite(Qplus), Unwrite(NQplus))
        self.end_fragment()

        Qplus = MathTex(
            r"\mathbb Q^+ = \{1, \frac{1}{2}, 2, 3, \frac{1}{3},\frac{1}{4} \cdots\} = \{g(1), g(2), g(3), g(4), g(5), g(6) \cdots\}"
        ).scale(1/2)
        Qzero = MathTex(r"\mathbb Q^0 = \{0\} = {g(0)}").scale(1/2)
        Qminus = MathTex(
            r"\mathbb Q^- = \{-1, -\frac{1}{2}, -2, -3, -\frac{1}{3}, -\frac{1}{4} \cdots\} = \{g(-1), g(-2), g(-3), g(-4), g(-5), g(-6) \cdots\}"
        ).scale(1/2)

        Q = VGroup(Qplus, Qzero, Qminus)

        self.play(Create(fracs))
        self.wait()
        self.play(Create(fracs2))
        self.wait()
        self.play(Create(fracs3))
        self.wait()
        self.play(Create(fracs4))
        self.wait()
        self.play(Create(cdots))
        self.play(Create(vdots))
        self.end_fragment()

        self.play(Write(o))
        self.end_fragment()

        self.play(Write(t), Create(Arrow1))
        self.end_fragment()

        self.play(Write(th), Create(Arrow2))
        self.end_fragment()

        self.play(Write(f), Create(Arrow3))
        self.end_fragment()

        self.play(Create(Arrow4), Create(l))
        self.end_fragment()

        self.play(
            Transform(Arrow4, Arrow5),
            Write(fi), run_time = 2
        )
        self.end_fragment()

        self.play(Write(s), Create(Arrow6))
        self.play(Write(se), Create(Arrow7))
        self.play(Write(e), Create(Arrow8))
        self.play(Write(n), Create(Arrow9))
        self.end_fragment()

        self.play(B.animate.scale(3/4).to_corner(UL))
        self.play(Write(func))
        self.end_fragment()

        Fl = always_redraw(
            lambda: CurvedArrow(
                start_point = B.get_corner(DR), end_point = func.get_corner(DL)
            )
        )

        self.play(Create(Fl))
        self.end_fragment()

        self.play(Uncreate(B), Uncreate(Fl), (Unwrite(func)))
        self.end_fragment()

        self.play(Write(Qplus))
        self.play(Qplus.animate.shift(UP))
        self.end_fragment()

        self.play(Write(Qminus))
        self.play(Qminus.animate.shift(DOWN))
        self.end_fragment()

        self.play(Write(Qzero))
        self.end_fragment()

        self.play(Q.animate.shift(2*UP))
        Fl2 = always_redraw(
            lambda: CurvedArrow(
                start_point = Q.get_corner(DR), end_point = fNZ.get_right(), angle = -PI/2
            ).set_color(PURE_BLUE)
        )
        self.play(DrawBorderThenFill(Fl2), Write(fNZ), run_time = 2)
        self.end_fragment()

        self.play(FadeOut(Fl2), Unwrite(fNZ), Uncreate(Q), run_time = 4)
        self.play(Write(NZQ), NZQ.animate.scale(3), run_time = 3)
        self.wait()


class cardinaldef(PresentationScene):
    def construct(self):

        C = MathTex(r"|A|=|B|")
        CC = Ellipse(height = 7, width = 3, color = PURE_RED).shift(3*LEFT + (1/4)*DOWN)
        CC2 = CC.copy().shift(6*RIGHT)
        cc = VGroup(CC, CC2)
        A = VGroup(*[
            Square(side_length = ((2*y)/5) +0.4, color = ORANGE, fill_opacity = 0.5, stroke_color = ORANGE)
            for y in range(3)
        ]).arrange_in_grid(rows = 3, buff = 1).shift(3*LEFT + (1/4)*DOWN)

        B = VGroup(*[
            Circle(radius = (y/5) +0.2, color = ORANGE, fill_opacity = 0.5, stroke_color = ORANGE)
            for y in range(3)
        ]).arrange_in_grid(rows = 3, buff = 1).shift(3*RIGHT + (1/4)*DOWN)

        Flnt = VGroup(*[
            Arrow(start = A[y].get_right(), end = B[y].get_left())
            for y in range(3)
        ]).set_color(PURE_BLUE)

        fAB = MathTex(r"f").set_color(YELLOW).shift(Flnt[2].get_bottom() + DOWN)

        fABFl = Arrow(start = Flnt[2].get_bottom(), end = fAB.get_top())

        TwoN = MathTex(r"|\mathbb N| = |2\mathbb N|").scale(3)
        fNTwoN = MathTex(
            r'f', r'\colon \mathbb N \rightarrow 2\mathbb N'
        ).set_color_by_tex_to_color_map({"f": ORANGE}).shift(cc.get_top()).scale(2)
        Nc = VGroup(*[
            MathTex(f"{y+1}")
            for y in range(5)
        ]).arrange_in_grid(rows = 5, buff = 0.75).shift(cc[0].get_center())
        TwoNc = VGroup(*[
            MathTex(f"{2*(y+1)}")
            for y in range(5)
        ]).arrange_in_grid(rows = 5, buff = 0.75).shift(cc[1].get_center())
        vdots = MathTex(r"\vdots").shift(Nc[4].get_bottom() + DOWN)
        Vvdots = VGroup(vdots, vdots.copy().shift(6*RIGHT))
        Flzero = VGroup(*[
            Arrow(start = Nc[y].get_right(), end = TwoNc[y].get_left())
            for y in range(5)
        ]).set_color(PURE_GREEN)
        fTwoN = MathTex(r"f(x) = 2x").set_color(YELLOW).shift(Flzero[4].get_bottom() + DOWN)
        Z = MathTex(r"|\mathbb N| = |\mathbb Z|").scale(3)
        CZ = Ellipse(height = 7, width = 3, color = BLUE)
        NN = VGroup(*[
            MathTex(f"{y+1}")
            for y in range(5)
        ]).arrange_in_grid(rows = 5, buff = 0.75).shift(3*LEFT + (1/2)*UP)
        NZ = VGroup(*[
            MathTex(f"{int((1+(-1)**(y+1)*(2*(y+1)-1))/4)}")
            for y in range(5)
        ]).arrange_in_grid(rows = 5, buff = 0.75).shift(3*RIGHT + (1/2)*UP)
        Fl = VGroup(*[
            Arrow(start = NN[y].get_right(), end = NZ[y].get_left())
            for y in range(5)
        ]).set_color(PURE_GREEN)
        fNZ = MathTex(r"f(n) = \frac{1 + (-1)^n(2n-1)}{4}").scale(1/2).shift(3*DOWN)

        self.play(DrawBorderThenFill(cc))
        self.end_fragment()

        self.play(DrawBorderThenFill(A))
        self.end_fragment()

        self.play(DrawBorderThenFill(B))
        self.end_fragment()

        self.play(DrawBorderThenFill(Flnt), run_time = 3)
        self.end_fragment()

        self.play(Write(fAB), FadeIn(fABFl), run_time = 2)
        self.end_fragment()

        self.play(FadeOut(cc), Uncreate(A), Uncreate(B), Uncreate(Flnt), Unwrite(fAB), FadeOut(fABFl), run_time = 8)
        self.play(Write(C))
        self.play(C.animate.scale(3))
        self.end_fragment()

        self.play(Unwrite(C))
        self.end_fragment()

        self.play(Write(TwoN))
        self.end_fragment()

        self.play(Unwrite(TwoN))
        self.play(FadeIn(cc), run_time = 2)
        self.play(Write(fNTwoN), run_time = 2)
        self.end_fragment()

        self.play(Write(Nc))
        self.play(Write(TwoNc))
        self.play(Write(Vvdots))
        self.end_fragment()

        self.play(DrawBorderThenFill(Flzero), run_time = 3)
        self.end_fragment()

        self.play(Write(fTwoN))
        self.end_fragment()

        self.play(FadeOut(cc), Unwrite(fNTwoN), Unwrite(Nc), Unwrite(Vvdots), Unwrite(TwoNc), Uncreate(Flzero), Unwrite(fTwoN), run_time = 10)
        self.end_fragment()

        self.play(Write(Z)) #Here start |N|=|Z|
        self.end_fragment()

        self.play(Unwrite(Z))
        self.play(Write(MathTex(r"f: \mathbb N \rightarrow \mathbb Z").scale(2).shift(3.5*UP)))
        self.play(DrawBorderThenFill(CZ.shift(3*LEFT + (1/4)*DOWN)))
        self.play(DrawBorderThenFill(CZ.copy().shift(6*RIGHT)))
        self.end_fragment()

        self.play(Create(NN), run_time = 2)
        self.end_fragment()

        self.play(Create(NZ), run_time = 2)
        self.play(Write(Vvdots))
        self.end_fragment()

        self.play(DrawBorderThenFill(Fl), run_time = 3)
        self.end_fragment()

        self.play(Write(fNZ))
        self.end_fragment()

        self.wait()