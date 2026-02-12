import sympy as sp
import random

class MathGenerator:
    def __init__(self):
        self.x = sp.symbols('x')

    def generate_calculus_derivative(self):
        """Generates a random function and its derivative."""
        # Random coefficients and powers
        a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 5)
        n, m = random.randint(2, 5), random.randint(2, 5)
        
        # Mix of polynomials and trig
        functions = [
            a * self.x**n + b * self.x,
            a * sp.sin(b * self.x),
            a * sp.cos(b * self.x),
            a * self.x**2 + b * sp.exp(self.x),
            a * sp.log(self.x**2 + 1)
        ]
        
        func = random.choice(functions)
        derivative = sp.diff(func, self.x)
        
        return {
            "type": "derivative",
            "question": f"Find the derivative of: $f(x) = {sp.latex(func)}$",
            "answer": f"$f'(x) = {sp.latex(derivative)}$",
            "raw_answer": derivative
        }

    def generate_linear_algebra_dot(self):
        """Generates a dot product problem."""
        dim = random.randint(2, 3)
        v1 = [random.randint(-5, 5) for _ in range(dim)]
        v2 = [random.randint(-5, 5) for _ in range(dim)]
        
        dot_product = sum(i*j for i, j in zip(v1, v2))
        
        # Format vectors for LaTeX
        vec1_tex = "\\begin{bmatrix}" + "\\\\".join(map(str, v1)) + "\\end{bmatrix}"
        vec2_tex = "\\begin{bmatrix}" + "\\\\".join(map(str, v2)) + "\\end{bmatrix}"
        
        return {
            "type": "linalg_dot",
            "question": f"Calculate the dot product: ${vec1_tex} \\cdot {vec2_tex}$",
            "answer": f"${dot_product}$",
            "raw_answer": dot_product
        }

    def get_problem(self, category):
        if category == "Calculus (Derivatives)":
            return self.generate_calculus_derivative()
        elif category == "Linear Algebra (Dot Product)":
            return self.generate_linear_algebra_dot()
        else:
            return {"question": "Select a valid category.", "answer": ""}

if __name__ == "__main__":
    gen = MathGenerator()
    print("Testing Generator:")
    print(gen.get_problem("Calculus (Derivatives)"))
    print(gen.get_problem("Linear Algebra (Dot Product)"))
