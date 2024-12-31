from manim import *
import numpy as np


class Question_Two(Scene): 
    def construct(self):
        intro = Tex(r"""
                    \raggedright
                    \textbf{Question 2} \\[10pt]
                    Find the eigenvalues of the resulting system in terms \\  
                    of the parameters $R$, $C$, and $L$. \\[5pt]
                    What are the possible phase planes for your system \\
                    given that $R$, $C$, and $L$ are always nonnegative? \\[5pt]
                    Sketch the phase plane and the $v_C(t)$- and $i(t)$-graphs for \\
                    each case.
        """).to_edge(UL, buff=0.5)

            
        self.play(Write(intro))
        self.wait(5)

        self.clear()

        p_1 = Tex(r"""
                    \raggedright
                    From our system: 
                    \(\left\{
                    \begin{aligned}
                        \frac{dv_c}{dt} &= \frac{i}{C} \\
                        \frac{di}{dt} &= \frac{-Ri - v_C}{L}
                    \end{aligned}
                    \right.\) we are able to get \\[5pt]
                    the matrix \(A = \begin{pmatrix}
                                0 & \frac{1}{C} \\
                                \frac{-1}{L} & \frac{-R}{L}
                            \end{pmatrix}\).
                """).to_edge(UL, buff=0.5)
        
        self.play(Write(p_1))
        self.wait(2)

        self.clear()

        t_1 = Tex(r"""
            \(\text{det}(A -\lambda I) = 0\)
        """)

        t_2 = Tex(r"""
            \(\text{det}\left( \begin{pmatrix}
            0 & \frac{1}{C} \\
            \frac{-1}{L} & \frac{-R}{L}
            \end{pmatrix} - \lambda I \right) = 0\)
        """)

        t_3 = Tex(r"""
            \(\text{det}\left( \begin{pmatrix}
            -\lambda & \frac{1}{C} \\
            \frac{1}{L} & -\lambda - \frac{R}{L}
            \end{pmatrix} \right) = 0\)
                """)

        t_4 = Tex(r"""
                \(CL\lambda^2 + RC\lambda + 1 = 0\), \text{(characteristic polynomial)}
                """)
            
        t_5 = Tex(r"""
                \(\lambda = \frac{-R \pm \sqrt{R^2 - \frac{4L}{C}}}{2L}\)
                """)

        p_2 = Tex(r"""
                    \raggedright
                    \(A = \begin{pmatrix}
                                0 & \frac{1}{C} \\
                                \frac{-1}{L} & \frac{-R}{L}
                            \end{pmatrix}\).
                    Now we can find our eigenvalues
                  
                """).to_edge(UL, buff=0.5)
        
        rect = Rectangle(height=3, color=GREEN)
        
        

        self.play(Create(p_2))

        self.play(Write(t_1))  # Write the first equation
        self.wait(2)
        self.play(Transform(t_1, t_2))  # t_1 transforms into t_2
        self.wait(2)
        self.play(Transform(t_1, t_3))  # t_1 transforms into t_3
        self.wait(2)
        self.play(Transform(t_1, t_4))  # t_1 transforms into t_4
        self.wait(2)
        self.play(Transform(t_1, t_5))
        self.play(Create(rect))
        self.wait(2)

        self.clear()

        text = Tex(
                     r"""
                    \[\text{Notice that there are 3 possible systems, all depending on } 
                    R^2 - \frac{4L}{C}, \text{ denoted as } \Delta.\]
                    \begin{itemize}
                        \item $\Delta < 0$: Underdamped System, complex eigenvalues, phase portrait: Spiral Sink
                        \item $\Delta > 0$: Overdamped System, negative eigenvalues, phase portrait: Spiral Sink
                        \item $\Delta = 0$: Critically Damped System, repeated real eigenvalues, phase portrait: Center
                    \end{itemize}
                    """,
                    font_size=34
                    ).to_edge(UL, buff=0.5)
        
        self.play(Write(text))

