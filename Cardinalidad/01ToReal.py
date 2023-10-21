from manim import *
import random as rd


class RealBijection(Scene):
    def construct(self):
        Real01str = MathTex(r"|(0, 1)| = |\mathbb R|")

        #First Part

        FuncToFind = MathTex(r"\phi: (0, 1) \rightarrow \left(-\frac{\pi}{2}, \frac{\pi}{2} \right)").move_to(2*UP)
        FuncFound = MathTex(r"\phi(x) = \pi x -\frac{\pi}{2}").move_to(FuncToFind.get_bottom() + DOWN)

        FuncG = VGroup(FuncToFind, SurroundingRectangle(FuncToFind, buff = MED_LARGE_BUFF, corner_radius = 0.2))
        FuncG2 = VGroup(FuncFound, SurroundingRectangle(FuncFound, buff = MED_LARGE_BUFF, corner_radius = 0.2))

        tracker_x = ValueTracker(0.01)

        Segm = NumberLine(
            x_range = [0, 1, 1],
            length = 1,
            include_ticks = False,
            color = PURE_BLUE
        ).move_to(3*UP/2)
        ZeroOne = MathTex(r"(0, 1)").move_to(Segm.get_top() + UP/2)

        Circ = Circle(radius = 1).set_color(GRAY)

        dot1 = Dot().add_updater(
            lambda n: n.move_to(
                Segm.n2p(tracker_x.get_value())
            )
        ).set_color(GREEN_B)

        dot2 = Dot().add_updater(
            lambda m: m.move_to(
                Circ.point_at_angle((np.pi*tracker_x.get_value() -np.pi/2) - np.pi/2)
            )
        ).set_color(YELLOW_E)

        BijecLine = always_redraw(
            lambda: DashedLine(
                Segm.n2p(tracker_x.get_value()),
                Circ.point_at_angle((np.pi*tracker_x.get_value() -np.pi/2) - np.pi/2)
            ).set_color(WHITE)
        )

        Xstr = MathTex(r"x = ")

        XValue = always_redraw(
            lambda: DecimalNumber(num_decimal_places = 3)
                .set_value(tracker_x.get_value())
                .next_to(Xstr)
        )

        PhiXstr = MathTex(r"\phi\left(x\right) \approx ")
        PhiXValue = always_redraw(
            lambda: DecimalNumber(num_decimal_places = 3)
                .set_value(np.pi*tracker_x.get_value() -np.pi/2)
                .next_to(PhiXstr)
        )
        XGroup = VGroup(Xstr, XValue)
        PhiXGroup = VGroup(PhiXstr, PhiXValue)

        XPhiXGroup = VGroup(XGroup, PhiXGroup).arrange_in_grid(rows = 2, cols = 1).move_to(Circ.get_bottom() + DOWN)

        Angles = r"\frac{\pi}{2}"

        AngleT1 = MathTex(Angles)
        AngleT2 = MathTex(r"-", Angles)

        AnglesG = VGroup(AngleT1, AngleT2).set_color(PURE_GREEN).scale(1/2)
        AnglesG[0].next_to(Circ)
        AnglesG[1].next_to(Circ, LEFT)

        dotangle = Dot(Circ.get_right())
        dotangle2 = Dot(Circ.get_left())


        self.play(Write(Real01str), Real01str.animate.scale(2), run_time = 2)
        self.wait()
        self.play(Unwrite(Real01str))
        self.play(Write(FuncToFind), FuncToFind.animate.scale(1.5), run_time = 2)
        self.wait()
        self.play(Write(FuncFound))
        self.wait()
        self.play(FuncToFind.animate.scale(2/3))
        self.play(
            Create(FuncG[1]), 
            Create(FuncG2[1]), 
            FuncG.animate.to_corner(UL).scale(1/2), 
            FuncG2.animate.to_corner(UR).scale(1/2),
            run_time = 4
        )

        self.play(Write(Segm), Create(ZeroOne), run_time = 2)
        self.play(Create(Circ))
        self.play(FadeIn(AnglesG, dotangle, dotangle2), run_time = 2)

        self.play(FadeIn(dot1, dot2, BijecLine))
        self.play(Write(XPhiXGroup), run_time = 4)

        Times = 9

        for Skull in range(Times):
            x = "%.3f" % rd.random()
            if x == 0:
                Times =+1
            else:
                self.play(tracker_x.animate.set_value(x))
                self.wait()

        self.play(
            *[FadeOut(obj) for obj in self.mobjects + self.foreground_mobjects],
            run_time = 3
        )

        self.play(FadeIn(MathTex(r"|(0, 1)| = |(-\frac{\pi}{2}, \frac{\pi}{2})|"), scale = 2), run_time = 2)

        self.play(
            *[FadeOut(obj) for obj in self.mobjects + self.foreground_mobjects]
        )

        #Second Part

        Func2ToFind = MathTex(
            r"\psi: \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \rightarrow \mathbb R"
        ).move_to(2*UP)
        Func2Found = MathTex(r"\psi(x) = \tan(x)").move_to(Func2ToFind.get_bottom() + DOWN)

        box3 = SurroundingRectangle(Func2ToFind, buff = MED_LARGE_BUFF, corner_radius = 0.2)
        box4 = SurroundingRectangle(Func2Found, buff = MED_LARGE_BUFF, corner_radius = 0.2)

        Func2G = VGroup(Func2ToFind, box3)
        Func2G2 = VGroup(Func2Found, box4)

        RealLine = NumberLine(
            [-28, 28, 7], 
            length = 56,
            include_ticks = False,
            color = PINK
        ).move_to(Circ.get_bottom())

        dot3 = Dot().add_updater(
            lambda m: m.move_to(
                RealLine.n2p(np.tan(np.pi*tracker_x.get_value() -np.pi/2))
            )
        ).set_color(MAROON_B)

        BijecLine2 = always_redraw(
            lambda: DashedLine(
                Circ.point_at_angle((np.pi*tracker_x.get_value() -np.pi/2) - np.pi/2),
                RealLine.n2p(np.tan(np.pi*tracker_x.get_value() -np.pi/2)),
            ).set_color(PURE_GREEN)
        )

        PsiXstr = MathTex(r"\psi\left(x\right) \approx")
        PsiXValue = always_redraw(
            lambda: DecimalNumber(num_decimal_places = 3)
                .set_value(np.tan(np.pi*tracker_x.get_value() -np.pi/2))
                .next_to(PsiXstr)
        )
        PsiXGroup = VGroup(PsiXstr, PsiXValue)

        TanLine = always_redraw(
            lambda: DashedLine(
                Circ.point_at_angle(((np.pi*tracker_x.get_value() -np.pi/2) - np.pi/2) + np.pi), 
                Circ.point_at_angle((np.pi*tracker_x.get_value() -np.pi/2) - np.pi/2)
            ).set_color(ORANGE)
        )

        Xstr2 = MathTex(r"x = ")

        XValue2 = always_redraw(
            lambda: DecimalNumber(num_decimal_places = 3)
                .set_value(np.pi*tracker_x.get_value() -np.pi/2)
                .next_to(Xstr2)
        )

        XGroup2 = VGroup(Xstr2, XValue2)


        self.play(Write(Func2ToFind), Func2ToFind.animate.scale(1.5), run_time = 2)
        self.wait()
        self.play(Write(Func2Found))
        self.wait()
        self.play(Func2ToFind.animate.scale(2/3))
        self.play(
            Create(box3), 
            Create(box4), 
            Func2G.animate.to_corner(UL).scale(1/2), 
            Func2G2.animate.to_corner(UR).scale(1/2),
            run_time = 4
        )
        XTanXGroup = VGroup(XGroup2, PsiXGroup).arrange_in_grid(rows = 2, cols = 1).move_to(Func2G.get_bottom() + DOWN)
        self.play(Create(Circ), DrawBorderThenFill(RealLine))
        self.play(FadeIn(dot2, dot3, BijecLine2), run_time = 2)
        self.play(Write(XTanXGroup), run_time = 4)
        self.play(Create(TanLine))
        self.play(FadeIn(AnglesG, dotangle, dotangle2))

        for Sus in range(Times):
            A = "%.3f" % rd.random()
            if A == 0:
                Times =+1
            else:
                self.play(tracker_x.animate.set_value(A))
                self.wait()

        self.play(
            *[FadeOut(obj) for obj in self.mobjects + self.foreground_mobjects],
            run_time = 6
        )

        self.play(FadeIn(MathTex(r"\left|\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\right| = |\mathbb R|"), scale = 2), run_time = 2)

        self.play(
            *[FadeOut(obj) for obj in self.mobjects + self.foreground_mobjects]
        )

        #Third Part

        Func1 = VGroup(FuncToFind, FuncFound).arrange_in_grid(rows=2)
        Func1Box = VGroup(Func1, SurroundingRectangle(Func1, buff = MED_LARGE_BUFF))

        Func2 = VGroup(Func2ToFind, Func2Found).arrange_in_grid(rows=2)
        Func2Box = VGroup(Func2, SurroundingRectangle(Func2, buff = MED_LARGE_BUFF))

        FuncCompToFind = MathTex(r"\psi \circ \phi: (0, 1) \rightarrow \mathbb R")
        FuncCompFound = MathTex(r"(\psi \circ \phi)(x) = \psi(\phi(x)) = \tan(\pi x -\frac{\pi}{2})")

        FuncComp = VGroup(FuncCompToFind, FuncCompFound).arrange_in_grid(rows=2).move_to(3*UP).scale(3/4)

        Dots = VGroup(dot1, dot2, dot3)
        BijectLines = VGroup(BijecLine.update(), BijecLine2.update())

        ImpMOBJ = VGroup(ZeroOne, Segm, Circ, RealLine)

        Psi_o_PhiXstr = MathTex(r"(\psi \circ \phi)(x) = ")
        Psi_o_PhiXValue = always_redraw(
            lambda: DecimalNumber(num_decimal_places = 3)
                .set_value(np.tan(np.pi*tracker_x.get_value() -np.pi/2))
                .next_to(Psi_o_PhiXstr)
        )
        Psi_o_PhiXGroup = VGroup(Psi_o_PhiXstr, Psi_o_PhiXValue)

        XPsi_o_PhiXGroup = VGroup(XGroup, Psi_o_PhiXGroup).arrange_in_grid(rows=2).move_to(2*DOWN)

        self.play(Write(Func1Box.to_corner(UL)), Write(Func2Box.to_corner(UR)), run_time = 2)
        self.play(Write(FuncComp), run_time = 3)

        self.play(Create(ImpMOBJ), run_time = 3)
        self.wait()
        self.play(Create(Dots))
        self.wait()
        self.play(Create(BijectLines))
        self.wait()
        self.play(Create(TanLine), run_time = 2)
        self.wait()
        self.play(FadeIn(AnglesG, dotangle, dotangle2), run_time = 2)
        self.wait()
        self.play(Write(XPsi_o_PhiXGroup), run_time = 2)
        self.wait(2)

        for QuandaleDingle in range(Times):
            A = "%.3f" % rd.random()
            if A == 0:
                Times =+1
            else:
                self.play(tracker_x.animate.set_value(A))
                self.wait()

        self.play(
            *[FadeOut(obj) for obj in self.mobjects + self.foreground_mobjects],
            run_time = 3
        )

        CardinalityEqs = MathTex(
            r"|(0, 1)| = \left|\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\right|", 
            r"\newline",
            r"|(-\frac{\pi}{2}, \frac{\pi}{2})| = |\mathbb R|"
        ) 
        self.play(FadeIn(CardinalityEqs, scale = 2), run_time = 2)
        self.play(Transform(CardinalityEqs, Real01str), run_time = 2)

        self.wait(2)