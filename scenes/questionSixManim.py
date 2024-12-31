from manim import *
import numpy as np


class Question_Six(Scene): 
    def construct(self):
        intro = Tex(r"""
                    \raggedright
                    \textbf{Question 6}\\
                    Repeat Part 5 using a voltage source of $v_T = 10$ volts.
                    """, 
                font_size=40
                ).to_edge(UL, buff=0.5)
        
        context = Tex(r"""
                    \raggedright
                    Since $v_T = 10$, we cannot negate it. So our system is:
                """).to_edge(UL, buff=0.5)

        system = Tex(r"""
                    \[
                    \left\{
                    \begin{aligned}
                        \frac{dv_c}{dt} &= \frac{i}{C} \\
                        \frac{di}{dt} &= \frac{v_T -Ri - v_C}{L}
                    \end{aligned}
                    \right.
                    \]
                    """).shift(np.array([0, 1, 0]))
        
        text = Tex(r"""
                    and our second-order differential equation is: \\ 
                    $ LC\frac{d^2v_C}{dt} + RC\frac{dv_C}{dt} + v_C = v_T $
                     """).shift(-2, 0, 0)
        
        p_1 = Tex(r"""
                \raggedright
                Having $v_T = 10$ does not change the the eigenvalues or \\ 
                eigenvectors. We still solve for the eigenvalues and \\ 
                eigenvectors using the unforced (homogeneous) equation. \\ 
                So we still get: 
                """).to_edge(UL, buff=0.5)
        
        eigval = Tex(r"""
                    $\lambda = -666.67 \pm 1699.67i$
                """).shift(np.array([0, 1.25, 0]))
        
        eigvect = Tex(r"""
                \raggedright
                \(v = \begin{pmatrix}
                                1 \\
                                -0.00013 + 0.00034\mathrm{i}
                            \end{pmatrix}\).
                """).shift(np.array([0, 0, 0]))
        
        p_2 = Tex(r"""
                \raggedright
                However, our second-order differential equation is:
                """, 
                  ).shift(np.array([-1, -1.25, 0]))
        
        sec_ode = Tex(r"""
                  $\frac{d^2v_c}{dt^2} + \frac{R}{L} \frac{dv_c}{dt} + \frac{1}{LC}v_C = 10$
                """).shift(np.array([0, -2, 0]))
        
        p_3 = Tex(r"""
                \raggedright
                and the general solution becomes: 
                """,
                ).to_edge(UL, buff=0.5)
        
        gen_solution = Tex(r"""
                         \[
                        v_C(t) = k_1e^{-666.67t}\sin(1699.67t) + k_2e^{-666.67t}\cos(1699.67t) + 10
                        \] 
                        """, 
                        font_size=40)
        
        note = Tex(r"""
                \raggedright
                \textit{Note: } This is just the second form of the equation, \\
                but we could use the first form too.
                """, 
                font_size = 35).shift(np.array([-2, -2, 0]))
        
        rect = Rectangle(height=2, width=12, color=GREEN)

        p_solution_text = Tex(r"""
                        \raggedright
                        To get the particular solution, we can solve for \\
                        $k_1$ and $k_2$ again using the same techniques we \\
                        used for Question 5.
                        """
                        ).to_edge(UL, buff=0.5)
        
        particular_solution_before = Tex(r"""
                                        \[
                                        v_C(t) = k_1e^{-666.67t}\sin(1699.67t) + k_2e^{-666.67t}\cos(1699.67t) + 10
                                        \]
                                        """, 
                                        font_size=40
                                        )
        
        
        particular_solution_after = Tex(r"""
                        \[
                                 v_C(t) = 10
                        \]
                        """,
                        font_size=40
                        )
        
        p_solution_conc = Tex(r"""
                        \raggedright
                        This may look strange, but we have to take into account that \\ 
                        this system is nonhomogeneous. As $t \rightarrow \infty$, all \\
                        solutions converge to the equilibrium value $v_C(t) = 10$.  \\
                        Given  the initial conditions $i(0) = 0$ and $v_C(0) = 10$, \\
                        the system starts at equilibrium. Therefore, it remains \\
                        at $v_C(t) = 10$ for all $t$. 
                        """).to_edge(UL, buff=0.5)
        
        rect2 = Rectangle(color=GREEN)
                  
        
        conc = Text("Thank you for listining to my presentation!\nAre there any questions?").to_edge(UL, buff=0.5)


        

# Animate
        self.play(Write(intro))
        self.wait(3)
        self.clear()
        self.play(Write(context))
        self.play(Write(system))
        self.play(Write(text))
        self.wait(2)
        self.clear()
        self.play(Write(p_1))
        self.play(Write(eigval))
        self.play(Write(eigvect))
        self.play(Write(p_2))
        self.play(Write(sec_ode))
        self.wait()
        self.clear()
        self.play(Write(p_3))
        self.play(Write(gen_solution))
        self.play(Create(rect))
        self.play(Write(note))
        self.wait()
        self.clear()
        self.play(Write(p_solution_text))
        self.play(Write(particular_solution_before))
        self.wait()
        self.play(Transform(particular_solution_before, particular_solution_after))
        self.play(Create(rect2))
        self.wait()
        self.clear()
        self.play(Write(p_solution_conc))
        self.wait(4)
        self.clear()
        self.play(Write(conc))
        for _ in range(3):
                tex_in_1 = Tex(r""" $\frac{dv_c}{dt} = \frac{i}{C}$ \\
                            $\frac{di}{dt} = \frac{-Ri - v_C}{L}$
                       """, 
                       font_size = 35
                       ).scale(3)
                tex_out_1 = Tex(r""" $\frac{dv_c}{dt} = \frac{i}{C}$ \\
                                $\frac{di}{dt} = \frac{v_T - Ri - v_C}{L}$
                        """, 
                       font_size = 35
                       ).scale(3)
                
                tex_in_2 = Tex(r"""
                        \[\frac{d^2v_c}{dt^2} + \frac{R}{L} \frac{dv_c}{dt} + \frac{1}{LC}v_C = 0\]
                        """)
                
                tex_out_2 = Tex(r"""
                        \[\frac{d^2v_c}{dt^2} + \frac{R}{L} \frac{dv_c}{dt} + \frac{1}{LC}v_C = 10\]
                        """)
        
                self.play(FadeIn(tex_in_1, shift=DOWN, scale=0.66))
                self.play(ReplacementTransform(tex_in_1, tex_out_1))
                self.play(FadeOut(tex_out_1, shift=DOWN * 2, scale=1.5))

                self.play(FadeIn(tex_in_2, shift=DOWN, scale=0.66))
                self.play(ReplacementTransform(tex_in_2, tex_out_2))
                self.play(FadeOut(tex_out_2, shift=DOWN * 2, scale=1.5))
