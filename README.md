<div align="center">

# **Shiv Expert**

> Bridging Mathematics and AI to Model the Physical World.

<a href="https://shiv2503portfolio.netlify.app/">
  <img src="./assets/temp.gif" alt="Click to View My Interactive Portfolio" />
</a>

</div>

---

## Mathematical Frontiers I've Tackled So far


### **Physics-Informed Neural Networks (PINNs)**

* **The Challenge:** How do you force a neural network to obey the laws of physics?
* **The Solution:** By minimizing a composite loss function that simultaneously enforces known data points and the residual of the governing Partial Differential Equation ($\mathcal{F}(u)$).


$$\mathcal{L}(\theta) = \underbrace{\lambda_{data} \mathcal{L}_{data}}_{\text{Data Fidelity}} + \underbrace{\lambda_{physics} \mathcal{L}_{physics}}_{\text{Physical Law Constraint}}$$


---

### **Sinusoidal Representation Networks (SIRENs)**

* **The Challenge:** How can a network represent continuous, complex signals without losing detail?
* **The Solution:** By constructing a network where each layer is a sinusoidal function, allowing it to perfectly capture the signal's derivatives and fine details.

    $$\Phi(\mathbf{x}) = (f_L \circ \dots \circ f_1)(\mathbf{x}) \quad \text{where} \quad f_i(\mathbf{x}_i) = \sin(\mathbf{W}_i \mathbf{x}_i + \mathbf{b}_i)$$
---

## 🛠️ My Toolkit

| **Languages & Libraries** | **Frameworks & Tools** | **Core Mathematical Concepts** |
| :---: | :---: | :---: |
| Python | PyTorch & JAX & Tf | Partial Differential Equations (PDEs) |
| NumPy & SciPy | Matplotlib & Seaborn | Fourier Analysis & Signal Processing |
| C++ (Basics) | Git & GitHub | Numerical Optimization Methods |
