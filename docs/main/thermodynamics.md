# 热力学

重点关注 **恒容（等容）和恒压（等压）** 这两种最常见的实验条件！

焓变的大小不仅取决于反应本身，还取决于所处的环境条件。

## 5.1 温变

$$
dH = C_p dT
$$

$$
\Delta H = \int_{T_1}^{T_2} C_p dT
$$

$C_p$ 是等压热容。如果温度区间不大， $C_p$ 可视为常数，则 $\Delta H = C_p \Delta T$ 。

## 5.2 相变

在恒压下发生相变时，温度不变，但需要吸收或释放热量：

$$
\Delta_{相}H = Q_p
$$

相变焓（如摩尔熔化焓 $\Delta_{fus}H_m$ ）通常是查表得到的已知常数。

## 5.3 基尔霍夫定律

如果已知 298K 下的反应焓 $\Delta_r H_m^\ominus(298K)$ ，想要求另一个温度 $T$ 下的焓变

$$
\left( \frac{\partial \Delta_r H_m^\ominus}{\partial T} \right)_p = \Delta_r C_{p,m}^\ominus
$$

$$
\Delta_r H_m^\ominus(T_2) = \Delta_r H_m^\ominus(T_1) + \int_{T_1}^{T_2} \Delta_r C_{p,m}^\ominus(T) \, dT
$$

$$
\Delta_r H_m^\ominus(T_2) = \Delta_r H_m^\ominus(T_1) + \Delta_r C_{p,m}^\ominus(T_2 - T_1)
$$

## 5.4 吉布斯自由能

$$
G = H - TS
$$

## 5.5 范特霍夫方程

$$
\frac{d \ln K^\ominus}{dT} = \frac{\Delta_r H_m^\ominus}{RT^2}
$$
