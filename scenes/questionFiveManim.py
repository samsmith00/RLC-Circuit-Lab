from manim import *
import numpy as np
import sympy as smp

class Question_Five(Scene):
    def construct(self):
        intro = Tex(r"""
                    \raggedright
                    \textbf{Question 5}\\
                    The units used in applications are volts and amps for voltages \\ 
                    and currents, ohms for resistors, farads for capacitors, and henrys \\
                    for inductors. A typical, off-the-shelf circuit might have \\
                    parameter values $R = 2000$ ohms (or 2 kilo-ohms), $C = 2 * 10^{-7}$  farads \\
                     (or 0.2 microfarads), and $L = 1.5$ henrys. Assuming zero input, $v_T = 0$, \\
                    and that the initial values of the current and voltage \\
                    are $i(0) = 0$ and $v_C(0) = 10$, describe the behavior of the \\
                    current and voltage for this circuit.
                    """, 
                font_size=40
                ).to_edge(UL, buff=0.5)
        
        p_1 = Tex(r"""
                \raggedright
                We have: 
                \begin{itemize}
                  \item $R = 2000$ ohms
                  \item $C = 2 * 10^{-7}$  farads
                  \item $L = 1.5$ henrys
                  \item $v_T = 0$, (zero input)
                  \item $i(0) = 0$ and $v_C(0) = 10$, (initial conditions)
                \end{itemize}
                """, 
                 font_size=40
                ).to_edge(UL, buff=0.5)
        
        t_1 = Tex(r"""
                \raggedright
                First lets find $\Delta$ to determine what type of system we have
                """).to_edge(UL, buff=0.5)
        
        t_2 = Tex(r"""
                $R^2 - \frac{4L}{C}$ 
                """)
        t_2_1 = Tex(r"""
                $2000^2 - \frac{4(1.5)}{2 * 10^{-7}}$
                """)
        
        t_2_2 = Tex(r"""
                $2000^2 - \frac{4(1.5)}{2 * 10^{-7}}$
                """)
        t_2_3 = Tex(r"""
                $-26,000,000$
                """)
        
        p_2 = Tex(r"""
                \raggedright
                Since $\Delta$ is negative, we know the system is a spiral sink \\
                with complex eigenvalues
                """).shift(np.array([0, -1, 0]))
        
        p_3 = Tex(r"""
                \raggedright
                Now lets find the eigenvalues: 
                """).to_edge(UL, buff=0.5)
        
        e_1 = Tex(r"""
                $CL\lambda^2 + RC\lambda + 1 = 0$
                """)
        
        e_2 = Tex(r"""
                $(2*10^{-7})(1.5)\lambda^2 + (2000)(2*10^{-7})\lambda + 1 = 0$
                """)
        
        e_3 = Tex(r"""
                $\lambda = -666.67 \pm 1699.67i$ \\
                $\alpha = -666.67$ \\
                $\beta = 1699.67$ \\
                """)
        
        p_4 = Tex(r"""
                \raggedright
                Using Python's linear algebra funciton \textbf{eig}, we can calculate \\
                the systems eigenvectors
                """).to_edge(UL, buff=0.5)
        
        code_text = """
                import numpy as np
                from numpy.linalg import eig

                def calculate_eigenvalues(R, C, L): 
                    A = np.array([[0, 1/C], [-1/L, -R/L]])
                    eigenvals, eigenvects = eig(A)
                    print(f"Eigenvectors: {eigenvects}")
                    """
        code = Code(
            code=code_text,
            tab_width=3,
            language="Python",  
            font_size=20,       
            background="window" 
        )

        v_1 = Tex(r"""
                \raggedright
                which gives us \(v = \begin{pmatrix}
                                1 \\
                                -0.00013 + 0.00034\mathrm{i}
                            \end{pmatrix}\).
                """).shift(np.array([-1, -2.5, 0]))
        
        conclusion = Tex(r"""
                    \raggedright
                    Since $R > 0$, the phase portrait spirals clockwise toward the orgin. This indicates
                    that the system is underdamped and both $v_C$ (voltage) and $i$ (current) oscillate 
                    while they gradually decay, enventually approaching \\
                    $(0,0)$ in the phase portrait.Lastly, we can create our general solution \\
                    equation by plugging our values into the equation: 
                    """,
                    font_size=40
                         ).to_edge(UL, buff=0.5)

        general_solutio_start = Tex(r"""
                            $v_C(t) = e^{\alpha t} \left( \cos(\beta t) + i \sin(\beta t) \right) v_{C_0}$
                            """)

        
        general_solution_end = Tex(r"""
                                   
                                \[
                                        v_C(t) = e^{-666.67t} \left( \cos(1699.67t) + i \sin(1699.67t) \right)
                                        \begin{pmatrix} 
                                        1 \\ 
                                        -0.00013 + 0.00034i 
                                        \end{pmatrix}
                                \] 
                                """, 
                                font_size=35
                                )
        
        gen_solution_two = Tex(r"""
                                \begin{align*}
                                \text{Or: } \\ \hfill & v_C(t) = k_1e^{-666.67t}\sin(1699.67t) + k_2e^{-666.67t}\cos(1699.67t)
                                \end{align*}
                                """, 
                                font_size=35
                                ).shift(np.array([0, -2, 0]))
        

        c_1 = Tex(r"""
                \raggedright
                To get the particular solution, we can use the second form \\
                for the general solution and solve for $k_1$ and $k_2$: 
                """).to_edge(UL, buff=0.5)
        
        particular_solution_before = Tex(r"""
                                        \[
                                        v_C(t) = k_1e^{-666.67t}\sin(1699.67t) + k_2e^{-666.67t}\cos(1699.67t)
                                        \]
                                        """, 
                                        font_size=40
                                        )
        
        
        particular_solution_after = Tex(r"""
                        \[
                                 v_C(t) = 3.92e^{-666.67t}\sin(1699.67t) + 10e^{-666.67t}\cos(1699.67t)
                        \]
                        """,
                        font_size=40
                        )
        


        # Calculate Derivatives

        t, k, c = smp.symbols('t k c')

        f = k*smp.exp(-666.67*t) * smp.cos(0.00033993*t) + c*smp.exp(-666.67*t) * smp.sin(0.00033993*t)
        smp.diff(f, t)
            

        
        rect = Rectangle(height=2, width=12, color=GREEN)
        rect2 = Rectangle(height=2, width=12, color=GREEN)
        rect2.shift(np.array([0, -2, 0]))
        rect3 = Rectangle(height=2, width=12, color=GREEN)
        


        # Animate
        self.play(Write(intro))
        self.wait(7)
        self.clear()

        self.play(Write(p_1))
        self.wait(3)
        self.clear()

        self.play(Write(t_1))
        self.wait(1)
        self.play(Write(t_2))
        self.wait()
        self.play(Transform(t_2, t_2_1))
        self.wait()
        self.play(Transform(t_2, t_2_2))
        self.wait()
        self.play(Transform(t_2, t_2_3))
                  
        self.wait()
        self.play(Write(p_2))
        self.wait()
        self.clear()

        self.play(Write(p_3))
        self.play(Write(e_1))
        self.wait(1)
        self.play(Transform(e_1, e_2)) 
        self.wait(1)
        self.play(Transform(e_1, e_3))
        self.wait(1)
        self.clear()

        self.play(Write(p_4))
        self.play(Write(code))
        self.play(Write(v_1))
        self.wait()
        self.clear()

        self.play(Write(conclusion))
        self.play(Write(general_solutio_start))
        self.wait()
        self.play(Transform(general_solutio_start, general_solution_end))
        self.play(Create(rect))
        self.play(Write(gen_solution_two))
        self.play(Create(rect2))
        self.wait()
        self.clear()
        self.play(Write(c_1))
        self.play(Write(particular_solution_before))
        self.wait()
        self.play(Transform(particular_solution_before, particular_solution_after))
        self.play(Create(rect3))