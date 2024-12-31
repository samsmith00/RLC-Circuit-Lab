from manim import *
import numpy as np


class Question_Four(Scene):
    def construct(self):
        intro = Tex(r"""
                    \raggedright
                    \textbf{Question 4}\\
                    Repeat Part 1, assuming that $v_T$ is nonzero. The resulting system\\ 
                    will have $R$, $C$, $L$, and $v_T$ as parameters.   
                """, 
                font_size=40
                ).to_edge(UL, buff=0.5)

        p_1 = Tex(r"""
                \raggedright
                We have:
                \begin{itemize}
                  \item $\frac{dv_C}{dt} = \frac{i}{C}$
                  \item $\frac{di}{dt} = \frac{v_L}{L}$
                  \item $v_T - Ri = v_C + v_L $
                \end{itemize} 
                """, 
                font_size=40
                ).to_edge(UL, buff=0.5)

        p_2 = Tex(r"""
                \raggedright
                For our system, we want $\frac{dv_C}{dt} = something$ and $\frac{di}{dt} = something$ \\
                Hence we get:  
                """, 
                font_size=40
                ).to_edge()
        
        eq_one_before = Tex(r"""
                $\frac{dv_C}{dt} = something$ \\
                """, 
                font_size=45
                ).to_edge()
        
        eq_one_before.shift(np.array([5, -1, 0]))
        
        eq_two_before = Tex(r"""
                $\frac{di}{dt} = something$
                """,
                font_size=45
                ).to_edge()
        
        eq_two_before.shift(np.array([5, -2, 0]))

        eq_one_after = Tex(r"""
                $\frac{dv_C}{dt} = \frac{i}{C}$ \\
                """, 
                font_size=45
                ).to_edge()
        
        eq_one_after.shift(np.array([5, -1, 0]))

        eq_two_after = Tex(r"""
                $\frac{di}{dt} = \frac{v_T - Ri - v_C}{L}$
                """,
                font_size=45
                ).to_edge()

        eq_two_after.shift(np.array([5, -2, 0]))


        rect = Rectangle(height=2, width=6, color=GREEN)
        rect.shift(np.array([0, -1.5, 0]))


        # Animate 
        self.play(Write(intro))
        self.wait(4)
        self.clear()
        self.play(Write(p_1))
        self.play(Write(p_2))
        self.play(
            Write(eq_one_before), 
            Write(eq_two_before)
            )
        self.wait(2)
        self.play(
            Transform(eq_one_before, eq_one_after), 
            Transform(eq_two_before, eq_two_after)
            )
        self.play(Create(rect))
        self.wait()