from manim import *
import numpy as np
from scipy.integrate import solve_ivp

HIGH = 10
LOW = 0.1
INITIAL_CONDITION = [3, 3]  
T_SPAN = (0, 50)  

class Overdamped(Scene): 
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
        R = 3.0133838625396234 
        C = 0.44113970455183943 
        L = 2.124987159422198

        axes = Axes(
            x_range=[-10, 10, 1], 
            y_range=[-10, 10, 1], 
            axis_config=None
        )

        point = axes.coords_to_point(np.array([INITIAL_CONDITION]))
        dot_scene = Dot(point, color=YELLOW)

        def vector_field_func(point): 
            vc, i = point[:2]
            derivatives = self.ode_system(0, [vc, i], R, C, L)
            return np.array([derivatives[0], derivatives[1], 0])
        
        vector_field = ArrowVectorField(vector_field_func, x_range=[-10, 10], y_range=[-10, 10])
        stream_lines = StreamLines(vector_field_func, x_range=[-10, 10], y_range=[-10, 10], max_anchors_per_line=20)
        stream_lines.set_color_by_gradient(BLUE, GREEN, YELLOW)

        solution = self.solve_system(R, C, L)
        t = np.linspace(T_SPAN[0], T_SPAN[1])
        vc, i = solution.sol(t)

        trajectory_points = [axes.coords_to_point(vc[k], i[k]) for k in range(len(t))]
        trajectory = VMobject()
        trajectory.set_points_smoothly(trajectory_points)
        trajectory.set_color(YELLOW)

        intro = Tex(r"""
                    \textbf{Overdamped System}
                    \begin{itemize}
                        \item $R^2 - \frac{4L}{C} > 0$ $\rightarrow$ Two distince real roots
                        \item Phase Portrait $\rightarrow$ Real Sink
                        \item No oscillation
                    \end{itemize}
                    """, 
                    font_size=38
                    ).to_edge(UL, buff=0.5)


        axes2 = Axes(
            x_range=[-1, 11, 1],
            y_range=[-2, 8, 1],
            axis_config={"include_tip": True, "numbers_to_exclude": [0], "include_numbers": True}
        )

        labels = axes2.get_axis_labels(
            Tex("t").scale(0.7), Tex(r"""$v_C(t), i(t)$""").scale(0.45)
        )

        vc_solution_points = [axes2.coords_to_point(t[k], vc[k]) for k in range(10)]
        vc_solution = VMobject()
        vc_solution.set_points_smoothly(vc_solution_points)
        vc_solution.set_color(BLUE)

        i_solution_points = [axes2.coords_to_point(t[k], i[k]) for k in range(10)]
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
        self.add(axes, dot_scene)
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

