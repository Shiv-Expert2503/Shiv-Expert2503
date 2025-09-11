# generate_attractor.py
import numpy as np
from scipy.integrate import solve_ivp

# 1. Define the Aizawa Attractor's differential equations
def aizawa_attractor(t, xyz, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
    x, y, z = xyz
    dxdt = (z - b) * x - d * y
    dydt = d * x + (z - b) * y
    dzdt = c + a * z - (z**3 / 3) - (x**2 + y**2) * (1 + e * z) + f * z * x**3
    return [dxdt, dydt, dzdt]

# 2. Set initial conditions and time span
initial_state = [0.1, 0.0, 0.0]
t_span = [0, 100]
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# 3. Solve the ODE system
solution = solve_ivp(
    aizawa_attractor,
    t_span,
    initial_state,
    t_eval=t_eval,
    dense_output=True
)

# 4. Extract the 2D path (x, y coordinates) and format for SVG
points = solution.y[0:2].T  # Use x and y for a 2D projection
scaled_points = (points - np.mean(points, axis=0)) / np.std(points, axis=0) * 25 # Scale for visibility

# Create the SVG path string
path_data = f"M {scaled_points[0,0]:.2f},{scaled_points[0,1]:.2f} "
path_data += " ".join([f"L {p[0]:.2f},{p[1]:.2f}" for p in scaled_points[1:]])

# 5. Read the SVG template and inject the new path
# (Your existing SVG file, but with a placeholder for the path)
with open('assets/aizawa_template.svg', 'r') as f:
    svg_template = f.read()

final_svg = svg_template.replace('__AIZAWA_PATH_PLACEHOLDER__', path_data)

with open('assets/aizawa.svg', 'w') as f:
    f.write(final_svg)

print("✅ Successfully generated aizawa.svg in assets/ folder!")
