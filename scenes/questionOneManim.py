import numpy as np
from manim import *

class Question_One(Scene):
    def construct(self):
        title = Text("RLC Circuit Lab\n By: Sam Smith").to_edge(UL, buff=0.5)

        capacitor_left = Line(LEFT * 0.5, RIGHT * 0.5, color=GREEN).shift([4, -0.3, 0])
        capacitor_right = Line(LEFT * 0.5, RIGHT * 0.5, color=GREEN).shift([4, -0.9, 0])
        capacitor_lines = VGroup(capacitor_left, capacitor_right)

        def inductor_curve(t, b, r):
            return ((0.09*b*t - 0.3 * r * np.sin(b*t)), (1 - r * np.cos(b*t)), 0)  # Parametric equations

        b = 2
        r = 0.5
        inductor = ParametricFunction(lambda t: inductor_curve(t, b, r), t_range=[0, 3 * np.pi], color=YELLOW).shift(UP * 0.2)

        r_1 = np.array([-4.2, 0.72, 0])
        r_2 = np.array([-3.9, 1.3, 0])
        r_3 = np.array([-3.6, 0.3, 0])
        r_4 = np.array([-3.3, 1.3, 0])
        r_5 = np.array([-3.0, 0.3, 0])
        r_6 = np.array([-2.7, 1.3, 0])
        r_7 = np.array([-2.5, 0.72, 0])
        
        resistor_points = [r_1, r_2, r_3, r_4, r_5, r_6, r_7,]
        
        # Create a line connecting the points
        zigzag_line = VMobject(color=BLUE)
        zigzag_line.set_points_as_corners(resistor_points)

        circ = Circle(radius=0.6)
        circ.move_to(np.array([-6, -0.9, 0]))

        b_1 = np.array([-6, -0.3, 0])
        b_2 = np.array([-6, 0.723, 0])
        b_3 = np.array([-4.2, 0.723, 0])
        b_4 = np.array([-2.5, 0.723, 0])
        b_5 = np.array([0, 0.723, 0])
        b_6 = np.array([1.748, 0.723, 0])
        b_7 = np.array([4, 0.723, 0])
        b_8 = np.array([4, -0.3, 0])
        b_9 = np.array([4, -0.9, 0])
        b_10 = np.array([4, -2.3, 0])
        b_11 = np.array([-6, -2.3, 0])
        b_12 = np.array([-6, -1.5, 0])

        first_connection_points = [b_1, b_2, b_3]
        second_connection_points = [b_4, b_5]
        third_connection_points = [b_6, b_7, b_8]
        fourth_connection_points = [b_9, b_10, b_11, b_12]

        first_connection = VMobject()
        first_connection.set_points_as_corners(first_connection_points)
        
        second_connection = VMobject()
        second_connection.set_points_as_corners(second_connection_points)

        third_connection = VMobject()
        third_connection.set_points_as_corners(third_connection_points)

        fourth_connection = VMobject()
        fourth_connection.set_points_as_corners(fourth_connection_points)

        
        self.play(Write(title))
        self.play(Create(circ), run_time=0.3)
        self.play(Create(first_connection), run_time=0.3)
        self.play(Create(zigzag_line), run_time=0.3)
        self.play(Create(second_connection), run_time=0.3)
        self.play(Create(inductor), run_time=0.3)
        self.play(Create(third_connection), run_time=0.3)
        self.play(Create(capacitor_lines), run_time=0.3)
        self.play(Create(fourth_connection), run_time=0.3)
        
        self.wait(2)

        self.clear()

        # ******************** Start Question 1 ********************

        intro = Tex(r"""
                    \raggedright
                    \textbf{Question 1} \\[10pt]
                    First, set the input voltage to zero, that is, assume $v_T = 0$. \\
                    Using the three equations above, write a first-order system of \\
                    differential equations with dependent variables $i$ and $v_C$. \\[5pt]
                    \textit{Hint:} Use the first equation to eliminate $v_L$ from the \\
                    third equation. You should have $R$, $C$, and $L$ as parameters \\
                    in your system.
                    """
                ).to_edge(UL, buff=0.5)
            
        self.play(Write(intro))
        self.wait(5)

        self.clear()

        equs = Tex(r"""
                \raggedright
                We are given three equations: 
                \begin{enumerate}
                    \item[1)] $v_T - Ri = v_C + v_L$ (Kirchhoff’s voltage law)
                    \item[2)] $C\frac{dv_c}{dt} = i$
                    \item[3)] $L\frac{di}{dt} = v_L$
                \end{enumerate}
                \vspace{1em}
                   """).to_edge(UL, buff=0.5)
        text = Tex(r"""
                    and must turm them into a system of differential equations
                """)
        text.shift(np.array([0, -1, 0]))
        
        self.play(Write(equs))
        self.play(Write(text))
        self.wait(3)

        self.clear()

        
        eq_initial = MathTex(r"\frac{di}{dt} = \frac{v_L}{L}")
        eq_initial.shift(np.array([3.3, -1.2, 0]))

        # Final substituted equation
        eq_substitute = MathTex(r"\frac{di}{dt} = \frac{-Ri - v_C}{L}").to_edge(UP, buff=1)
        eq_substitute.shift(np.array([4, -3.7, 0]))

        # Part 1: Deriving \( v_L \)
        part_1 = Tex(r"""
            Since $v_T = 0$, we obtain: 
            \begin{align*}
                v_T - Ri &= v_C + v_L \\
                - Ri &= v_C + v_L \\
                v_L &= -Ri - v_C
            \end{align*}
        """).to_edge(LEFT, buff=1)

        # Part 2: Final system of equations
        part_2 = Tex(r"""
            Finally, we get the system: 
            \begin{align*}
                \frac{dv_c}{dt} &= \frac{i}{C} \\
            \end{align*}
        """).to_edge(RIGHT, buff=1)

        part_2.shift(UP * (part_1.get_height() - part_2.get_height()) / 2)

        rect = Rectangle(height=3.5, color=GREEN).shift(np.array([3.95, -1.1, 0]))



        # Animations
        self.play(Write(part_1))
        self.play(Write(part_2))
        self.play(Write(eq_initial))

        # Transition from eq_initial to eq_substitute
        self.play(Transform(eq_initial, eq_substitute))
        self.wait(1)

        self.play(Create(rect))
        self.wait(2)


