from manim import *
import numpy as np

class Question_Three(Scene): 
    def construct(self):
        intro = Tex(r"""
                    \raggedright
                    \textbf{Question 3}\\
                    Convert the first-order system of equations from Part 1 into a \\
                    second-order differential equation involving only \( v_C \) (and not \( i \)). \\
                    (This is the form of the equation that you will typically find \\
                    in electric circuit theory texts.)

                """, 
                font_size=40
                ).to_edge(UL, buff=0.5)
        
        p_1 = Tex(r"""
                    We have \(\left\{
                    \begin{aligned}
                        \frac{dv_c}{dt} &= \frac{i}{C} \\
                        \frac{di}{dt} &= \frac{-Ri - v_C}{L}
                    \end{aligned}
                    \right.\) \\ Now take the derivitive of our $v_C$ term to get: 
                """).to_edge(UL, buff=0.5)
        
        t_1 = Tex(r"""
                \[\frac{d^2v_c}{dt^2} = \frac{1}{C} * \frac{di}{dt}\]
                """)
        
        p_2 = Tex(r"""
                \raggedright
                Now plug in $\frac{di}{dt}$ into the second derivative and simplifying \\
                the expresson results in our second-order differential equation
                """).to_edge(UL, buff=0.5)

        t_2 = Tex(r"""
                \[\frac{d^2v_c}{dt^2} = \frac{1}{C} \left( \frac{-Ri}{L} - \frac{v_C}{L} \right)\]
                """)
        
        t_3 = Tex(r"""
                \[\frac{d^2v_c}{dt^2} = \frac{-R}{LC} \left(C \frac{dv_c}{dt} \right) - \frac{v_C}{LC}\]
                """)
        
        t_4 = Tex(r"""
                \[\frac{d^2v_c}{dt^2} = \frac{-R}{L} \frac{dv_c}{dt} - \frac{v_C}{LC}\]
                """)
        
        t_5 = Tex(r"""
                \[\frac{d^2v_c}{dt^2} + \frac{R}{L} \frac{dv_c}{dt} + \frac{1}{LC}v_C = 0\]
                """)
        
        
        rect = Rectangle(height=2, width=6, color=GREEN)

        # Animate
        self.play(Write(intro))
        self.wait(4)
        self.clear()

        self.play(Write(p_1))
        self.play(Write(t_1))
        self.wait()
        self.clear()

        self.play(Write(p_2))
        self.play(Write(t_2))
        self.wait()
        self.play(Transform(t_2, t_3))
        self.wait()
        self.play(Transform(t_2, t_4))
        self.wait()
        self.play(Transform(t_2, t_5))
        self.wait()
        self.play(Create(rect))
        self.wait()




