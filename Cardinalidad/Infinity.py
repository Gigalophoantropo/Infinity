from manim import *
import random as rd
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



class Derivative(Scene):
    def construct(self):
        #Functex = MathTex(r"f(x)=\frac{x^(5)}{3}-\frac{8(x^(3))}{3}+4x")

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

        plot = axis.plot(func1, x_range=[-7, 7], color = TEAL_D)
        func1_prime=lambda x: (5*x**4)/3 - 8*x**2 + 4
        ascline = axis.plot(func1, x_range=[-7, -(2*((6+21**(1/2))/5))**(1/2)], color=PURE_RED).set_z_index(1)
        """self.play(Create(axis), run_time=2)
        self.play(Create(plot), run_time=2)"""
        self.add(ascline, plot)
        #self.wait()