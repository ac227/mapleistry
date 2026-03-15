# 电化学


## 8.1 常用公式和数据

$$
\Delta G = -nFE
$$

Nernst 方程：

$$
E = E^\circ - \frac{RT}{nF} \ln Q = E^\circ - \frac{RT}{nF} \ln \frac{\prod a_\text{产物}}{\prod a_\text{反应物}}
$$

0.0591 / log

Butler-Volmer 方程：

$$
j = j_0 \left[ \exp\left( \frac{\alpha n F \eta}{RT} \right) - \exp\left( -\frac{(1-\alpha) n F \eta}{RT} \right) \right]
$$

高正过电位 Tafel 近似 阳极区：

$$
\eta = \frac{2.303 RT}{\alpha n F} \log_{10} \left( \frac{j}{j_0} \right) \qquad
$$

或简写为

$$
\quad \eta = a + b \log_{10} j
$$

25℃ 时 Tafel 斜率：

$$
b_a = \frac{0.0591}{\alpha n} \quad (\text{V/dec}) \qquad
$$

$$
b_c = \frac{0.0591}{(1-\alpha) n} \quad (\text{V/dec})
$$

法拉第定律：

$$
\quad Q_\text{理论} = n F \cdot \frac{m}{M}
$$

电流效率：

$$
\varphi = \frac{m_\text{实际}}{m_\text{理论}} = \frac{Q_\text{实际有效}}{Q_\text{总}}
$$

常见电极电势表达式（25℃）：

| 电极反应                              | Nernst 方程 (V)                                 |
|---------------------------------------|--------------------------------------------------|
| ${2H+ + 2e- ⇌ H2}$                 | $E = 0 - 0.0591\,\text{pH}$                      |
| ${O2 + 4H+ + 4e- ⇌ 2H2O}$          | $E = 1.229 - 0.0591\,\text{pH} + 0.0148 \log p_{{O2}}$ |
| ${AgCl + e- ⇌ Ag + Cl-}$           | $E = 0.222 - 0.0591 \log [{Cl-}]$             |
| ${M^{n+} + n e- ⇌ M}$              | $E = E^\circ + \frac{0.0591}{n} \log [{M^{n+}}]$ |
| 玻璃 pH 电极                          | $E = K - 0.0591\,\text{pH}$                      |

电池总电压组成：

$$
E_\text{cell} = E^\circ_\text{cell} - |\eta_a| - |\eta_c| - I R_\text{ohm} - \Delta E_\text{浓差}
$$
