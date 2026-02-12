import plotly.graph_objects as go
import numpy as np

class LessonManager:
    def get_lessons(self):
        return {
            "Calculus": ["Derivatives Intuition", "Integrals Intuition"],
            "Linear Algebra": ["Vector Operations", "Dot Product Intuition"]
        }

    def get_lesson_content(self, subject, topic):
        if subject == "Calculus" and topic == "Derivatives Intuition":
            return self._calculus_derivative_lesson()
        elif subject == "Linear Algebra" and topic == "Vector Operations":
            return self._linalg_vector_lesson()
        else:
            return {
                "title": "Coming Soon",
                "markdown": "This lesson is under construction.",
                "figure": None
            }

    def _calculus_derivative_lesson(self):
        # Data for x^2
        x = np.linspace(-5, 5, 100)
        y = x**2
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = x^2'))
        
        # Initial tangent at x=1
        x0 = 1
        y0 = x0**2
        slope = 2*x0
        # Tangent line: y - y0 = m(x - x0) => y = m(x - x0) + y0
        y_tangent = slope * (x - x0) + y0
        
        fig.add_trace(go.Scatter(x=x, y=y_tangent, mode='lines', name='Tangent Line', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=[x0], y=[y0], mode='markers', name='Point (x, f(x))', marker=dict(size=10, color='red')))
        
        fig.update_layout(title="Visualizing the Derivative (Slope)", xaxis_title="x", yaxis_title="f(x)")
        
        return {
            "title": "Calculus: The Derivative is a Slope",
            "markdown": r"""
            ### What is a Derivative?
            
            The derivative of a function $f(x)$ at a point $x$ is simply the **slope** of the tangent line to the curve at that point.
            
            In this example, we have the function:
            $$ f(x) = x^2 $$
            
            The derivative is:
            $$ f'(x) = 2x $$
            
            At $x=1$, the slope is $2(1) = 2$.
            At $x=2$, the slope is $2(2) = 4$ (steeper!).
            At $x=0$, the slope is $0$ (flat).
            
            **Try it:** Use the slider below to move the point and watch the green tangent line change its slope!
            """,
            "figure": fig
        }

    def _linalg_vector_lesson(self):
        fig = go.Figure()
        
        # Vector v
        fig.add_trace(go.Scatter(x=[0, 3], y=[0, 2], mode='lines+markers+text', name='Vector v', text=['', 'v'], textposition='top right', line=dict(color='blue', width=3)))
        # Vector w
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 4], mode='lines+markers+text', name='Vector w', text=['', 'w'], textposition='top right', line=dict(color='red', width=3)))
        # Vector v+w
        fig.add_trace(go.Scatter(x=[0, 3+1], y=[0, 2+4], mode='lines+markers+text', name='v + w', text=['', 'v+w'], textposition='top right', line=dict(color='purple', width=3, dash='dot')))

        fig.update_layout(title="Vector Addition", xaxis_title="x", yaxis_title="y", xaxis_range=[-1, 5], yaxis_range=[-1, 7])
        
        return {
            "title": "Linear Algebra: Vector Addition",
            "markdown": r"""
            ### Adding Vectors
            
            Geometrically, adding two vectors $\vec{v}$ and $\vec{w}$ corresponds to placing the tail of $\vec{w}$ at the head of $\vec{v}$.
            
            The resulting vector $\vec{v} + \vec{w}$ connects the start of $\vec{v}$ to the end of $\vec{w}$.
            
            $$ \vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}, \quad \vec{w} = \begin{bmatrix} 1 \\ 4 \end{bmatrix} $$
            
            $$ \vec{v} + \vec{w} = \begin{bmatrix} 3+1 \\ 2+4 \end{bmatrix} = \begin{bmatrix} 4 \\ 6 \end{bmatrix} $$
            """,
            "figure": fig
        }
