from manim import *
import random as rd
import numpy as np
from Functions import summation
from manim_revealjs import PresentationScene, COMPLETE_LOOP

config.video_dir="./videos"


class Intro(PresentationScene):
    def construct(self):
        title=Title("Infinity").set_color(TEAL_D).shift(0.5*DOWN)
        BySomeOne=Text("By Gigalophoantropo", color="#333", fill_opacity=0, font_size=12).shift(3*DOWN)
        self.add(BySomeOne)
        self.play(Write(title), run_time=2)
        self.end_fragment()
        self.play(BySomeOne.animate.set_opacity(1), run_time=1.5)
        self.end_fragment()



class InfinityLengthTime(PresentationScene):
    def construct(self):
        tracker = ValueTracker(0)

        Nl = NumberLine(x_range = [0, 1000000, 100000], length = 10).set_opacity(0)

        LengthText = MathTex(r"Longitud = ").shift(Nl.get_center() + UP)

        Longitud = Integer(0).next_to(LengthText)
        def LongitudUpdater(mobj):
            mobj.set_value(tracker.get_value())
        Longitud.add_updater(LongitudUpdater, call_updater=True)

        lengthlong = VGroup(LengthText,Longitud)

        Dot1 = always_redraw(lambda: Dot(Nl.get_left()))
        Dot2 = always_redraw(
            lambda: Dot(Nl.n2p(tracker.get_value()))
        )

        line = always_redraw(
            lambda: Line(Dot1.get_center(), Dot2.get_center())
        )
        LigmaBalls = VGroup(lengthlong, Nl)

        self.add(LengthText, Longitud, Dot1, Dot2, line)
        self.wait()
        self.end_fragment()

        self.play(tracker.animate.set_value(rd.randint(0, 2500))),
        self.wait(0.5)
        self.play(tracker.animate.set_value(rd.randint(0, 2000)))
        self.wait()
        self.play(tracker.animate.increment_value(-int(tracker.get_value()/2)))
        self.wait(0.5)
        self.end_fragment()

        self.play(tracker.animate.set_value(1000000), run_time = 9)
        self.wait()
        self.end_fragment()

        self.play(LigmaBalls.animate.shift(LEFT))
        self.end_fragment()



class PotActInfinity(PresentationScene):
    def construct(self):
        tracker = ValueTracker(251120)
        PotentialText = Text("Infinito Potencial").to_edge(UL)
        ActualText = Text("Infinito Actual").to_edge(UR)

        Nl = NumberLine(x_range = [0, 1000000, 100000], length = 5).set_opacity(0).shift([-3.5, 0, 0] + DOWN)

        iq = MathTex(r"= ").shift(Nl.get_center() + UP)
        LengthText = MathTex(r"Longitud ").next_to(mobject_or_point = iq, direction = LEFT)

        Longitud = Integer(0).next_to(iq)
        def LongitudUpdater(mobj):
            mobj.set_value(tracker.get_value())
        Longitud.add_updater(LongitudUpdater, call_updater=True)

        lengthlong = VGroup(LengthText, iq, Longitud)

        Dot1 = always_redraw(lambda: Dot(Nl.get_left()).set_color(YELLOW))
        Dot2 = always_redraw(
            lambda: Dot(Nl.n2p(tracker.get_value())).set_color(YELLOW)
        )

        line = always_redraw(
            lambda: Line(Dot1.get_center(), Dot2.get_center()).set_color(YELLOW)
        )
        LigmaBalls = VGroup(lengthlong, Nl, Dot1, Dot2, line)

        Elnúmeromasgrande = MathTex(r"n \rightarrow n + 1").shift(Nl.get_top() + 2*UP)

        Actual = Line([1, -5, 0], [8, 3, 0]).set_color(PURE_RED)

        N = MathTex(r"\mathbb N").shift([4, 1, 0]).scale(2)
        Z = MathTex(r"\mathbb Z").shift(N.get_corner(DL) + DL).scale(2)
        R = MathTex(r"\mathbb R").shift([6, -2, 0]).scale(2)

        NZR = VGroup(N, Z, R)

        Air_Istotle = ImageMobject("Imágenes\\Air-Istotle.png")

        self.play(FadeIn(Air_Istotle), run_time = 3)
        self.end_fragment()

        self.play(Air_Istotle.animate.shift(4*RIGHT))
        self.end_fragment()

        Air_IstotleSays = Line(Air_Istotle.get_center() + DOWN/2, Air_Istotle.get_left() + LEFT + UP/2).set_color(YELLOW)
        WhatAir_IstotleSays = MathTex(r"\stackrel{\textstyle\text{Voy a dividir al infinito}}{\text{en dos nociones}}")
        WhatAir_IstotleSays.next_to(Air_IstotleSays, LEFT).shift(UP).set_color(YELLOW)
        self.play(Write(Air_IstotleSays), Create(WhatAir_IstotleSays), run_time = 3)
        self.end_fragment()

        self.play(FadeOut(Air_Istotle, Air_IstotleSays, WhatAir_IstotleSays))

        self.play(Write(PotentialText), run_time=2)
        self.end_fragment()

        self.play(DrawBorderThenFill(LigmaBalls),run_time = 3)
        self.end_fragment()

        self.play(Write(Elnúmeromasgrande), tracker.animate.set_value(1000000),run_time = 3, rate_func = rate_functions.ease_in_sine)
        self.end_fragment()

        self.play(Write(ActualText))
        self.end_fragment()

        self.play(DrawBorderThenFill(Actual))
        self.end_fragment()

        for conjunto in NZR:
            self.play(Write(conjunto))
        self.wait()
        self.end_fragment()



class PotentialInfinity(PresentationScene):
    def construct(self):
        titulo = Title("Infinito Potencial").set_color(YELLOW)

        Limit = MathTex(r"\lim_{x \to +\infty} \frac{1}{x} ")
        Iq = MathTex(r"= 0").next_to(Limit).set_opacity(0)
        LimitIq = VGroup(Limit, Iq)
        PotentialLimit = MathTex(
            r"\frac{1}{\stackrel{\textstyle\text{un número tan grande}}{\text{como quieras}}}}"
        ).shift(3.5*RIGHT + UP)

        n = []
        for z in range(3):
            n.append(rd.randint(1, 100))
        n.sort()
        ExamplesOneoverHUGE = VGroup(*[
            MathTex(fr"\frac{{1}}{{{x}}} \approx {round(1/x, 3)}")
            for x in n
        ]).arrange_in_grid(rows=2, cols=2, buff = 0.5).move_to(PotentialLimit.get_bottom()+2*DOWN)

        line = Line([0, -5, 0], titulo.get_bottom()).set_color(YELLOW)

        self.play(DrawBorderThenFill(titulo), run_time=2)
        self.end_fragment()

        self.play(DrawBorderThenFill(Limit), run_time=2)
        self.end_fragment()

        self.play(LimitIq.animate.move_to(3.5*LEFT))
        self.play(Create(line))
        self.end_fragment()

        self.play(Write(PotentialLimit), run_time=2)
        for x in range(3):
            self.play(Write(ExamplesOneoverHUGE[x]))
            self.end_fragment()

        self.play(Iq.animate.set_opacity(1))

        self.wait()
        self.end_fragment()



class HdH(PresentationScene):
   def construct(self):

      #Las S's son las habitaciones
      S = VGroup(*[
         Square(side_length = 1.5, stroke_color = BLUE)
         for GoofyAhhUncleProductions in range(9)
      ]).arrange_in_grid(rows = 3, cols = 3, buff = 0.25).shift(3*RIGHT)

      NerdFace1 = ImageMobject("Imágenes\\NerdFace.png")
      NerdFace2 = ImageMobject("Imágenes\\NerdFace2.png")
      NerdFace = Group(NerdFace1, NerdFace2).shift(2*LEFT + DOWN).scale(1/3)
      Morange = ImageMobject("Imágenes\\Morange.png").shift(5*LEFT + DOWN).scale(1/4) #From goofyahhuncleproductions 💀

      GoofyAhhPeopleYaEnElHotel = ["Imágenes\\GoofyAhhPeopleYaEnElHotel\\Skeleton.gif", 
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\EDP.png", 
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\HankSussyBaka.png",
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\DiscordMod.png",
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\Noorman.png",
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\OldLadyScreaming.png",
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\Pablo.png",
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\Ralph.png",
                                   "Imágenes\\GoofyAhhPeopleYaEnElHotel\\MegamindNo.png"]

      GAPIH = Group(*[
                     ImageMobject(GoofyAhhPeopleYaEnElHotel[x]).shift(S[x].get_center()).scale(1/3)
                     for x in range(9)
                  ])#These are the Goofy Ahh People, They are in the Hotel for a infinty period of time 💀

      #Para encajar a los Discord Mods tuve que poner su escala en '1/g_64' 🗿

      Puntos = MathTex(r"\cdots").shift(S[8].get_right() + RIGHT)
      SS = VGroup(*[
         Square(side_length = 0.3, stroke_color = BLUE).shift(S[g].get_corner(UR) + 0.15*LEFT + 0.15*DOWN)
         for g in range(9)
      ])
      #Será un buen sitio para enumerar las habitaciones 🐒
      Numbers = VGroup(*[
         MathTex(f"{a + 1}").shift(SS[a].get_center()).scale(1/2)
         for a in range(9)
      ])
      

      RightArrow = MathTex(r"\rightarrow ").shift(
         Morange.get_center() + ((NerdFace1.get_center()[0] - Morange.get_center()[0])/2)*RIGHT + 3*UP
      ) #🗿

      n = MathTex(r"n ").next_to(RightArrow, direction = LEFT)


      Habitación = MathTex(r"n+1").next_to(RightArrow)

      nRightArrowHabitación = VGroup(RightArrow, n, Habitación)


      NewGoofyAhhPeople = [
         "Imágenes\\GoofyAhhUncleNoBG.png",
         "Imágenes\\GoofyAhhApple.png",
         "Imágenes\\JohnPork.png",
         "Imágenes\\QuandaleDingle.png",
         "Imágenes\\GoofyAhhBird.png",
         "Imágenes\\moai.png",
      ]

      NewSussyPeople = Group(*[
         ImageMobject(NewGoofyAhhPeople[f])
         for f in range(len(NewGoofyAhhPeople))
      ]).arrange_in_grid(rows = 3, cols = 3, buff = 0.25).shift(5*LEFT + DOWN).scale(1/3)
      NewSussyPeople[0].scale(2)
      NewSussyPeople[1].scale(2)
      NewSussyPeople[4].scale(0.75)

   
      self.play(Create(S), Write(Puntos), run_time = 3)
      self.end_fragment()

      self.play(FadeIn(NerdFace1))
      self.end_fragment()

      self.play(FadeIn(Morange))
      self.end_fragment()

      self.play(FadeIn(GAPIH), Create(SS), Write(Numbers), run_time = 9)
      self.end_fragment()

      '''ChangeSkin(NerdFace1, NerdFace2, [2, 5])
      self.wait(0.4)
      SpeakButWhitMove(Morange, [2, 9])'''

      self.play(Write(nRightArrowHabitación))
      self.end_fragment()

      #Here the clients move to room number + 1 room

      for go in range(len(GAPIH) -1):
         self.play(GAPIH[go].animate.move_to(S[go + 1].get_center()))

      self.add_sound("GoofyAhhSounds/WooSE.mp3", time_offset=1)  
      self.add_sound("GoofyAhhSounds/PoopSE.mp3", time_offset=2)
      self.play(GAPIH[8].animate.move_to(Puntos.get_center()))
      self.play(FadeOut(GAPIH[8]))
      self.end_fragment()

      self.play(Morange.animate.move_to(S[0].get_center())) #Finally Morange is in The Goofy Ahh Hotel 💀
      self.end_fragment()

      Infty = MathTex(r"\infty = \infty + 1").shift(RightArrow.get_center() + DOWN)

      self.play(FadeIn(Infty))

      GAPIH.insert(0, Morange)
      GAPIH.remove(GAPIH[-1])
      for h in range(len(GAPIH)):
         GAPIH[h].move_to(S[h].get_center())

      NuevaHabitacion = MathTex(r"2n").next_to(RightArrow)
      self.end_fragment()

      self.play(FadeIn(NewSussyPeople), Infty.animate.set_opacity(0), run_time = 2)
      self.end_fragment()

      self.play(ReplacementTransform(Habitación, NuevaHabitacion), run_time = 2)
      self.end_fragment()

      for i in range(4):
         self.play(GAPIH[i].animate.move_to(S[2*i + 1].get_center()))
      for j in range(5):
         self.play(GAPIH[j+4].animate.move_to(Puntos.get_center()))
         self.play(FadeOut(GAPIH[j+4]))
      self.end_fragment()

      for k in range(5):
         self.play(NewSussyPeople[k].animate.move_to(S[2*k].get_center()))
      for l in range(len(NewGoofyAhhPeople) - 5):
         self.play(NewSussyPeople[l+5].animate.move_to(Puntos.get_center()))
         self.play(FadeOut(NewSussyPeople[l+5]))
      self.end_fragment()

      Infty = MathTex(r"\infty = 2\infty").shift(RightArrow.get_center() + DOWN)
      self.play(Infty.animate.set_opacity(1), run_time = 2)

      self.end_fragment()



class Dichotomy(PresentationScene):
    def construct(self):
        d = 64
        b = ValueTracker(0)

        sum = lambda n=None: summation(lambda x: (1/2)**x, 1, n)

        scale = lambda a: 1/(a+1)

        InvisibleLine = NumberLine(x_range = [0, d, 2], length = 10).set_opacity(0)

        tracker = ValueTracker(0)
        
        Dline = Line(
            InvisibleLine.get_left(), InvisibleLine.get_right()
        ).set_color(YELLOW) #It is the yellow line
        DlineParts = always_redraw(
            lambda: Line(
            Dline.get_left(), InvisibleLine.n2p(tracker.get_value())
        ).set_color(PURE_RED) #This the red line
        )
        Divide = Line(
            DOWN, 
            UP
        ).move_to(Dline.get_left()).set_color(PURE_BLUE).set_stroke(width = InvisibleLine.get_stroke_width()) #Ant this the divisor

        SystemDichoGroup = VGroup(InvisibleLine, Dline, Divide).move_to(DOWN)


        self.play(Create(Dline), FadeIn(DlineParts), run_time = 2)
        self.play(Write(Divide))
        self.play(Divide.copy().animate.move_to(Dline.get_right()), run_time = 2) #Another divisor
        Divide2 = always_redraw(lambda:
            Divide.copy().scale(scale(b.get_value())).move_to(
                InvisibleLine.n2p(tracker.get_value())
            )
        )

        def formulaWithResults(n: int=1):
            left_part = rf"\sum_{{i=1}}^{{{n}}} \left(\frac{{1}}{{2}}\right)^i = "
            result = rf"{{{sum(n)}}}"
            eq = left_part + result
            mobj = MathTex(eq)
            mobj[0][6].set_color(PURE_GREEN)
            return mobj
        

        eq1 = formulaWithResults().move_to(UP)

        Veces = 9 #Cuantas veces se repita la suma

        self.add(Divide2)
        for Idk in range(Veces):
            eq1_new = formulaWithResults(Idk+1).move_to(UP)
            self.wait(4/1.5**Idk)
            if Idk == 0:
                self.play(Write(eq1))
                br = Brace(Dline).shift(DOWN)
                Length = MathTex(f"{{1}}").shift(br.get_bottom() + DOWN/2).set_color(PURE_GREEN)
                self.play(FadeIn(br, Length))
                self.play(Write(Title("Dichotomy").set_color(TEAL)), run_time=1.5)
                self.end_fragment()
            self.play(
                ReplacementTransform(eq1, eq1_new),
                FadeIn(
                    Divide.copy().scale(scale(b.get_value())).move_to(
                        InvisibleLine.n2p(
                            tracker.get_value()
                        )
                    ) #The copies of the blue line 🐒
                ),
                tracker.animate.set_value(sum(Idk+1)*d),
                b.animate.set_value(Idk+1)
            )
            eq1 = eq1_new
        

        final_txt1 =  r"\lim_{n \to \infty}\sum_{i=1}^{n}\left(\frac{1}{2}\right)^i = 1"
        final_eq1 = MathTex(final_txt1).move_to(UP)
        final_eq1[0][12].set_color(PURE_GREEN)
        final_eq1[0][-1].set_color(PURE_GREEN)
        self.play(
            ReplacementTransform(eq1, final_eq1),
            tracker.animate.set_value(sum()*d),
            run_time=3)
        self.end_fragment()

        #Aquí se eliminan los objetos que estorban

        MobjectsToNotRemove = [Dline, DlineParts, Divide, Divide2]

        LengthD = MathTex(f"{{d}}").shift(br.get_bottom() + DOWN/2).set_color(PURE_GREEN)

        self.play(
            *[FadeOut(obj) 
                for obj in self.mobjects + self.foreground_mobjects
                    if obj not in MobjectsToNotRemove],
            tracker.animate.set_value(0),
            b.animate.set_value(0),
            run_time = 4
        )

        #Aquí empieza la generalización
        self.play(Divide.copy().animate.move_to(Dline.get_right()), run_time = 2)

        def formula(n=1):
            left_part = rf"\sum_{{i=1}}^{{{n}}} \left(\frac{{d}}{{2}}\right)^i ="
            terms = [rf"\frac{{d}}{{{2**i}}}" for i in range(1, n+1)]
            eq = left_part + " + ".join(terms)
            mobj = MathTex(eq)
            mobj[0][6].set_color(PURE_GREEN)
            index = 12
            for i in range(1, n+1):
                mobj[0][index].set_color(PURE_GREEN)
                index += 4 + int(np.log10(2**i))
            return mobj
        
        
        eq = formula().move_to(UP)

        Veces = 6

        for Goofy in range(Veces):
            eq_new = formula(Goofy+1).move_to(UP)
            self.wait(4/1.5**Goofy)
            if Goofy == 0:
                self.play(Write(eq))
                self.play(FadeIn(br, LengthD))
                self.play(Write(Title("Dichotomy").set_color(TEAL_D)), run_time=1.5)
                self.end_fragment()
            self.play(
                ReplacementTransform(eq, eq_new),
                FadeIn(
                    Divide.copy().scale(scale(b.get_value())).move_to(
                        InvisibleLine.n2p(
                            tracker.get_value()
                        )
                    ) #The copies of the blue line 🐒
                ),
                tracker.animate.set_value(sum(Goofy+1)*d),
                b.animate.set_value(Goofy+1)
            )
            eq = eq_new
        final_txt =  r"\lim_{n \to \infty}\sum_{i=1}^{n}\left(\frac{d}{2}\right)^i = d"
        final_eq = MathTex(final_txt).move_to(UP)
        final_eq[0][12].set_color(PURE_GREEN)
        final_eq[0][-1].set_color(PURE_GREEN)
        self.play(
            ReplacementTransform(eq, final_eq),
            tracker.animate.set_value(sum()*d),
            run_time=3)
        self.end_fragment()



class Derivative(PresentationScene):
    def construct(self):
        axis = Axes(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            x_length=14,
            y_length=8,
            axis_config={
                "include_ticks": False
            }
        )

        func1 = lambda x: (x**5)/3 - 8*(x**3)/3 + 4*x

        tracker = ValueTracker(.69)

        plotfunc1 = axis.plot(func1, x_range=[-7, 7], color = TEAL_D)
        func1_prime=lambda x: (5*x**4)/3 - 8*x**2 + 4
        ascline1 = axis.plot(func1, x_range=[-7, -(2*((6+21**(1/2))/5))**(1/2)], color=PURE_GREEN).set_z_index(1)
        ascline2 = axis.plot(func1, x_range=[-(2*((6+21**(1/2))/5))**(1/2), -(2*((6-21**(1/2))/5))**(1/2)], color=PURE_RED).set_z_index(1)
        ascline3 = axis.plot(func1, x_range=[-(2*((6-21**(1/2))/5))**(1/2), (2*((6-21**(1/2))/5))**(1/2)], color=PURE_GREEN).set_z_index(1)
        ascline4 = axis.plot(func1, x_range=[(2*((6-21**(1/2))/5))**(1/2), (2*((6+21**(1/2))/5))**(1/2)], color=PURE_RED).set_z_index(1)
        ascline5 = axis.plot(func1, x_range=[(2*((6+21**(1/2))/5))**(1/2), 7], color=PURE_GREEN).set_z_index(1)

        ASCLine=VGroup(ascline1, ascline2, ascline3, ascline4, ascline5)

        func1_prime_roots_tick = VGroup(
            *[Line(.2*DOWN, .2*UP, stroke_width=2).move_to(axis.c2p(ASCLine[x].t_max, 0)) for x in range(4)]
        )
        func1_prime_roots_dot = VGroup(
            *[Dot(axis.c2p(ASCLine[x].t_max, func1(ASCLine[x].t_max)), color=LIGHT_BROWN, radius=0.04) for x in range(4)]
        ).set_z_index(2)

        plotfunc1_labels=axis.get_axis_labels("x", "f(x)")


        self.play(Create(axis), Write(plotfunc1_labels), run_time=3)
        self.play(Create(plotfunc1), run_time=3)
        self.end_fragment()

        for i in range(4):
            self.play(Create(ASCLine[i]), run_time=3)
            self.play(Create(func1_prime_roots_tick[i]), Create(func1_prime_roots_dot[i]), run_time=3)
        self.play(Create(ASCLine[4]), run_time=3)
        self.end_fragment()

        self.play(*[FadeOut(e) for e in self.mobjects], run_time=4)
        self.play(Create(axis), run_time=2)
        m1=axis.plot(lambda x: 2*x, x_range=[-7, 7], color="#FF00FF")
        m2=axis.plot(lambda x: x/3, x_range=[-7, 7], color="#FFFF00")
        m3=axis.plot(lambda x: -3*x, x_range=[-7, 7], color="#00FFFF")
        m1_label=MathTex(r"2", color=m1.get_color()).move_to(3*UR)
        m2_label=MathTex(r"\frac{1}{3}", color=m2.get_color()).move_to(m2.get_right()+UL)
        m3_label=MathTex(r"-3", color=m3.get_color()).move_to(3*DR)
        ms=VGroup(m1, m2, m3)

        m_updater = always_redraw(
            lambda: axis.plot(lambda x: tracker.get_value()*x, x_range=[-7, 7], color=ORANGE)
        )

        m_updater_label_name = MathTex(r"m=").set_color(ORANGE).to_corner(UR).shift(LEFT).set_z_index(1)

        m_updater_label_value = always_redraw(
            lambda: DecimalNumber().set_value(tracker.get_value()).next_to(m_updater_label_name).set_color(ORANGE).set_z_index(1)
        )

        m_updater_label = VGroup(m_updater_label_name, m_updater_label_value)

        m_def_x_0=1.5
        m_def_x_1=3
        m_def_x=[m_def_x_0, m_def_x_1]

        
        self.play(Create(m1), run_time=1.5)
        self.play(Create(m2), run_time=1.5)
        self.play(Create(m3), run_time=1.5)
        self.end_fragment()

        self.play(Write(m1_label), Write(m2_label), Write(m3_label), run_time=3)
        self.end_fragment()

        self.play(FadeOut(m1_label, m2_label, m3_label), ReplacementTransform(ms, m_updater), run_time=3)
        self.play(Write(m_updater_label), run_time=2)
        self.end_fragment()

        self.play(tracker.animate.set_value(4.5), run_time=3)
        self.end_fragment()
        self.play(tracker.animate.set_value(-6.8), run_time=3)
        self.end_fragment()

        for w in [-40, 2.55, .53, .92, -.4, 69, -168.3, .01]:
            self.play(tracker.animate.set_value(w), run_time=3)
            self.wait()
        self.end_fragment()

        self.play(Unwrite(m_updater_label), run_time=1.5)
        self.play(tracker.animate.set_value(.69), run_time=3)
        mdef_ticks=VGroup(
            *[Line(.2*DOWN, .2*UP, stroke_width=2).move_to(axis.c2p(x, 0)) for x in m_def_x],
            *[Line(.2*LEFT, .2*RIGHT, stroke_width=2).move_to(axis.c2p(0, m_updater.get_point_from_function(x)[1])) for x in m_def_x],
        )
        mdef_ticks_labels=VGroup(
            *[MathTex(r"x_{}".format(x)).move_to(mdef_ticks[x].get_bottom()+DOWN/2) for x in [0, 1]],
            *[MathTex(r"f(x_{})".format(x)).move_to(mdef_ticks[x+2].get_left()+LEFT) for x in [0, 1]],
        )
        mdef_ticks_lines=VGroup(
            *[Line(axis.c2p(m_def_x[x], 0), axis.c2p(m_def_x[x], m_updater.get_point_from_function(m_def_x[x])[1]), stroke_width=2) for x in range(2)],
            *[Line(axis.c2p(m_def_x[x], m_updater.get_point_from_function(m_def_x[x])[1]), axis.c2p(0, m_updater.get_point_from_function(m_def_x[x])[1]), stroke_width=2) for x in range(2)],
        )

        m_def = MathTex(r"m=\frac{f(x_1)-f(x_0)}{x_1-x_0}=\frac{\Delta f(x)}{\Delta x}").move_to(3.5*RIGHT + 2.5*DOWN)

        self.play(Create(mdef_ticks[:2]), run_time=1.5)
        self.play(Write(mdef_ticks_labels[:2]), run_time=3)
        self.play(Create(mdef_ticks_lines[:2]), run_time=3)
        self.play(Create(mdef_ticks[2:]), run_time=1.5)
        self.play(Create(mdef_ticks_lines[2:]), run_time=3)
        self.play(Write(mdef_ticks_labels[2:]), run_time=3)
        self.play(Write(m_def), run_time=5)
        self.end_fragment()

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
        self.play(Create(axis), Write(plotfunc1_labels), run_time=3)
        self.play(Create(plotfunc1), run_time=3)
        self.end_fragment()

        func1_tans_eg = VGroup(
            *[Line(stroke_width=2, stroke_color=YELLOW).move_to(axis.c2p(x, func1(x))).rotate(np.arctan(func1_prime(x))) for x in [-2.5, -1.5, .69, 1.2, 2.3, -(2*((6-21**(1/2))/5))**(1/2)]]
        ).set_z_index(2)

        func1_dots_eg = VGroup(
            *[Dot(axis.c2p(x, func1(x)), color=LIGHT_BROWN, radius=.04) for x in [-2.5, -1.5, .69, 1.2, 2.3, -(2*((6-21**(1/2))/5))**(1/2)]]
        ).set_z_index(3)
        
        self.play(FadeIn(ASCLine, func1_prime_roots_tick, func1_prime_roots_dot), FadeOut(plotfunc1), run_time=6)
        self.end_fragment()
        
        for l in range(5):
            self.play(Create(func1_tans_eg[l]), Create(func1_dots_eg[l]), run_time=3)
            self.wait()

        self.play(Create(func1_tans_eg[-1]), Create(func1_dots_eg[-1]), run_time=3)
        self.end_fragment()

        self.play(*[FadeOut(mobj) for mobj in self.mobjects], run_time=4)

        axis2 = Axes(
            x_range=[-2.5, 11.5, 1],
            y_range=[-2, 6, 1],
            x_length=14,
            y_length=8,
            axis_config={
                "include_ticks": False
            }
        )

        axis2_labels=axis2.get_axis_labels(r"x", r"f(x)")

        func2 = lambda x: (3/2)*np.log(x+1)

        plotfunc2 = axis2.plot(func2, x_range=[-.999, 12], color="#00ff6c")

        prime_def_x = ValueTracker(1.5)
        prime_def_dx = ValueTracker(1.5)

        prime_def_ticks=always_redraw(
            lambda: VGroup(
                *[Line(.2*DOWN, .2*UP, stroke_width=2).move_to(axis2.c2p(prime_def_x.get_value()+x*prime_def_dx.get_value(), 0)) for x in range(2)],
                *[Line(.2*LEFT, .2*RIGHT, stroke_width=2).move_to(axis2.c2p(0, func2(prime_def_x.get_value() + x*prime_def_dx.get_value()))) for x in range(2)],
            )
        )
        prime_def_ticks_labels=always_redraw(
            lambda: VGroup(
                *[MathTex(r"x_0 {}".format([r"", r"+ dx"][x])).move_to(prime_def_ticks[x].get_bottom()+DOWN/4) for x in [0, 1]],
                *[MathTex(r"f(x_0 {})".format([r"", r"+ dx"][x])).move_to(prime_def_ticks[x+2].get_left()+LEFT/4, aligned_edge=RIGHT) for x in [0, 1]],
            )
        )

        prime_def_dx_label_value=always_redraw(
            lambda: DecimalNumber().set_value(prime_def_dx.get_value()).to_corner(UR).set_color(ORANGE)
        )
        prime_def_dx_label_name=MathTex(r"dx=").set_color(ORANGE).next_to(prime_def_dx_label_value, LEFT)
        prime_def_dx_label=VGroup(prime_def_dx_label_name, prime_def_dx_label_value)

        prime_def_m_label = MathTex(r"m=\frac{f(x_0+dx)-f(x_0)}{dx}=\frac{df(x)}{dx}").move_to(prime_def_dx_label.get_right()+DOWN, RIGHT).set_color("#56ccf2")

        prime_def_m = always_redraw(
            lambda: axis2.get_secant_slope_group(
                prime_def_x.get_value(),
                plotfunc2,
                prime_def_dx.get_value(),
                ORANGE,
                YELLOW,
                "dx",
                "df(x)",
                secant_line_color="#56ccf2",
                secant_line_length=8
            )
        )

        prime_def_m_dot1 = always_redraw(
            lambda: Dot().scale(.7).move_to(axis2.c2p(prime_def_x.get_value(), func2(prime_def_x.get_value()))).set_z_index(1)
        )

        prime_def_m_dot2 = always_redraw(
            lambda: Dot().scale(.7).move_to(axis2.c2p(prime_def_x.get_value()+prime_def_dx.get_value(), func2(prime_def_x.get_value()+prime_def_dx.get_value()))).set_z_index(1)
        )

        self.play(Create(VGroup(axis2, axis2_labels)), run_time=3)
        self.play(Create(plotfunc2), run_time=3)
        self.end_fragment()

        self.play(Create(VGroup(prime_def_m_dot1, prime_def_m_dot2, prime_def_m)), run_time=2)
        self.play(FadeIn(prime_def_ticks, prime_def_ticks_labels), run_time=3)
        self.play(Write(prime_def_dx_label), Write(prime_def_m_label), run_time=3)
        self.end_fragment()

        self.play(prime_def_dx.animate.set_value(3), run_time=3)
        self.end_fragment()

        self.play(
            FadeOut(prime_def_ticks_labels),
            ReplacementTransform(prime_def_dx_label_name, MathTex(r"dx\to").set_color(ORANGE).next_to(prime_def_dx_label_value, LEFT)),
            prime_def_dx.animate.set_value(.001),
            run_time=7,
        )
        self.end_fragment()

        self.play(prime_def_x.animate.set_value(.69), run_time=4)
        self.end_fragment()
        self.play(prime_def_x.animate.set_value(10), run_time=5)
        self.play(prime_def_x.animate.set_value(4), run_time=4)
        self.end_fragment()

        self.play(ReplacementTransform(prime_def_m_label, MathTex(r"f'(x_0)=\frac{df(x)}{dx}=\frac{f(x_0+dx)-f(x_0)}{dx}").move_to(prime_def_dx_label.get_right()+DOWN, RIGHT).set_color("#56ccf2")), run_time=2)
        self.end_fragment()
        
        prime_def_m_label_value=always_redraw(
            lambda: DecimalNumber().set_value(func2(prime_def_x.get_value())).to_corner(UR).set_color("#56ccf2")
        )
        self.play(
            ReplacementTransform(
                prime_def_dx_label,
                VGroup(MathTex(r"f'(x_0)=").set_color("#56ccf2").next_to(prime_def_m_label_value, LEFT), prime_def_m_label_value)
            ),
            run_time=3
        )
        self.end_fragment()

        self.play(prime_def_x.animate.set_value(-.3), run_time=4)
        self.end_fragment()

        self.play(prime_def_x.animate.set_value(1.5+1.5/2), run_time=4)
        self.end_fragment()
        self.play(prime_def_x.animate.set_value(5), run_time=4)
        self.play(prime_def_x.animate.set_value(1.5), run_time=4)
        self.end_fragment()