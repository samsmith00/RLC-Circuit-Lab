from manim import *
import numpy as np
from scipy.integrate import solve_ivp

INITIAL_CONDITION = [3, 3]  
T_SPAN = (0, 50)  


class Underdamped(Scene):  
    def ode_system(self, t, y, R, C, L): 
        vc = y[0]  # Voltage across the capacitor
        i = y[1]   # Current through the circuit
        
        #Equation 1 
        dvc_dt = i / C 

        # Equation 2
        di_dt = -(R * i + vc) / L  
        
        return [dvc_dt, di_dt]    

    
    def solve_system(self, R, C, L):
        solution = solve_ivp(
            self.ode_system, T_SPAN, INITIAL_CONDITION, args=(R, C, L), dense_output=True
        )
        return solution

    def construct(self): 
        # Underdamped system
        R = 0.30373512110395623 
        C = 5.083823113883663 
        L = 2.2488382269215936

        axes1 = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"include_tip": False, "numbers_to_exclude": [0]},
        )

        # Create initial value point
        point = axes1.coords_to_point(INITIAL_CONDITION[0], INITIAL_CONDITION[1])
        dot_scene = Dot(point, color=YELLOW)

        label = MathTex("({:1f}, {:1f})".format(INITIAL_CONDITION[0], INITIAL_CONDITION[1])).scale(0.5).next_to(UL, point)

    
        # Define the vector field function
        def vector_field_func(point):
            vc, i = point[:2]
            derivatives = self.ode_system(0, [vc, i], R, C, L)
            return np.array([derivatives[0], derivatives[1], 0])
        
        vector_field = ArrowVectorField(vector_field_func, x_range=[-10, 10], y_range=[-10, 10])
        stream_lines = StreamLines(vector_field_func, x_range=[-10, 10], y_range=[-10, 10], max_anchors_per_line=20)
        stream_lines.set_color_by_gradient(RED, YELLOW, GREEN)

        # Solve system for phase portrait
        solution = self.solve_system(R, C, L)
        t = np.linspace(T_SPAN[0], T_SPAN[1], 1000)
        vc, i = solution.sol(t)


        # Create phase trajectory
        trajectory_points = [axes1.coords_to_point(vc[k], i[k]) for k in range(len(t))]
        trajectory = VMobject()
        trajectory.set_points_smoothly(trajectory_points)
        trajectory.set_color(YELLOW)

        intro = Tex(r"""
                    \textbf{Underdamped System}
                    \begin{itemize}
                        \item $R^2 - \frac{4L}{C} < 0$ $\rightarrow$ Solutions are complex with real part $-\frac{R}{2L}$
                        \item Phase Portrait $\rightarrow$ Spiral Sink
                        \item $v_C$ and $i$ oscillate as they approach the equilibrium point
                    \end{itemize}
                    """, 
                    font_size=38
                    ).to_edge(UL, buff=0.5)
        
        axes2 = Axes(
            x_range=[-1, 55, 5],
            y_range=[-5, 10, 1],
            axis_config={"include_tip": True, "numbers_to_exclude": [0], "include_numbers": True}
        )

        labels = axes2.get_axis_labels(
            Tex("t").scale(0.7), Tex(r"""$v_C(t), i(t)$""").scale(0.45)
        )

    

        vc_solution_points = [axes2.coords_to_point(t[k], vc[k]) for k in range(len(t))]
        vc_solution = VMobject()
        vc_solution.set_points_smoothly(vc_solution_points)
        vc_solution.set_color(BLUE)

        i_solution_points = [axes2.coords_to_point(t[k], i[k]) for k in range(len(t))]
        i_solution = VMobject()
        i_solution.set_points_smoothly(i_solution_points)
        i_solution.set_color(RED)

        vc_label = Tex(r"$v_C(t)$", color=BLUE)
        vc_label.shift(np.array([1, 3, 0]))
        i_label = Tex(r"$i(t)$", color=RED)
        i_label.shift(np.array([2.5, 3, 0]))




        # Animate
        self.play(Write(intro))
        self.wait(4)
        self.clear()
        self.add(vector_field)
        self.add(axes1, dot_scene)
        self.play(Create(vector_field))
        self.play(Create(trajectory), run_time=5)
        self.wait()
        self.play(Transform(vector_field, stream_lines))
        stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())
        self.wait()

        # Solutions Graph
        self.clear()
        self.add(axes2, labels, vc_label, i_label)
        self.play(
            Write(vc_label),
            Write(i_label)
            )
        self.play(
            Create(vc_solution),
            Create(i_solution),
            run_time=5
        )

