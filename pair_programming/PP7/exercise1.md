Jacobian = $\begin{bmatrix} 2x & 2y \\\ e^{(x+y)} & e^{x+y} \end{bmatrix}$

Part A: Jacobian at pt 1 = $\begin{bmatrix} 2 & 2 \\\ e & e^{2} \end{bmatrix}$

Part B i.) : Jacobian at pt 1 = $\begin{bmatrix} 2 & -4 \\\ e & e^{4} \end{bmatrix}$

Part B ii.)  Jacobian at pt 1 = $\begin{bmatrix} 2 & 2 \\\ e & e^{2} \end{bmatrix}$



| Trace | Elementary Function | Current Value | Elementary Function Derivative | $\nabla_x$ Value | $\nabla_y$ Value |
| ----- | ------------------- | ------------- | ------------------------------ | ---------------- | ---------------- |
| $x$   | $x_1$               | 2             | $\dot x_i$                     | 2                | 0                |
| $y$   | $x_2$               | 1             | $\dot x_2$                     | 0                | 2                |
| $x_3$ | $x_1^2$             | 1             | $2 x_1 \dot x_1$               | 2                | 0                |
| $x_4$ | $x_2^2$             | 1             | $2 x_2 \dot x_2$               | 0                | 2                |
| $x_5$ | $x_3 + x_4$         | 2             | $\dot x_3 + \dot x_4$          | 2                | 2                |
| $x_6$ | $x_1 + x_2$         | 2             | $\dot x_1 + \dot x_2$          | 1                | 1                |
| $x_7$ | $e^{x_6}$           | $e^2$         | $e^{x_6} \dot x_6$             | $e^2$            | $e^2$            |
|       |                     |               |                                |                  |                  |

