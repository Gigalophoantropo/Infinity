from manim import *



class MyScene(Scene):
    def construct(self):
        Morange = ImageMobject("Morange.png").scale(1/2)
        GoofyAhhPeopleYaEnElHotel = ["GoofyAhhPeopleYaEnElHotel\\Skeleton.gif", 
                                   "GoofyAhhPeopleYaEnElHotel\\EDP.png", 
                                   "GoofyAhhPeopleYaEnElHotel\\HankSussyBaka.png",
                                   "GoofyAhhPeopleYaEnElHotel\\DiscordMod.png",
                                   "GoofyAhhPeopleYaEnElHotel\\Noorman.png",
                                   "GoofyAhhPeopleYaEnElHotel\\OldLadyScreaming.png",
                                   "GoofyAhhPeopleYaEnElHotel\\Pablo.png",
                                   "GoofyAhhPeopleYaEnElHotel\\Ralph.png",
                                   "GoofyAhhPeopleYaEnElHotel\\MegamindNo.png"]

        GAPIH = Group(*[
                     ImageMobject(GoofyAhhPeopleYaEnElHotel[x]).scale(1/2)
                     for x in range(9)
                  ]).arrange_in_grid(rows=3, cols=3 )
        #These are the Goofy Ahh People, They are in the Hotel for a infinty period of time 💀

        #Para encajar a los Discord Mods tuve que poner su escala en '1/g_64' 🗿

        GAPIH.insert(0, Morange)
        GAPIH.remove(GAPIH[-1])
        GAPIH.arrange_in_grid(rows=3, cols=3)


        self.add(GAPIH)

class fontspec(Scene):
    def construct(self):
        myTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
        )
        myTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Poppins}")
        
        text = Tex(
            r'''This text is in Google Poppins, 
            while the math $f(x) = x^2$ is still in regular \LaTeX.''',
            tex_template=myTexTemplate,
            tex_environment="{minipage}{5cm}"
        ).to_edge(UL)
        self.play(Write(text))

        self.wait() 