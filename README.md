# Calcular-Material-para-Aplanado-

Este proyecto permite calcular de manera automática la cantidad de materiales necesarios para realizar un aplanado o rebocado de muro, siguiendo los parámetros establecidos por la Norma Mexicana de Construcción (NMX-C-486-ONNCCE-2014), que recomienda una proporción 1:4 (cemento:arena) para morteros de recubrimiento.

El programa solicita al usuario los datos básicos del muro:

Largo (m) → la medida horizontal del muro a aplanar.
Altura (m) → la medida vertical del muro.
Grosor del aplanado (cm) → el espesor de la capa de mortero que se aplicará.

Con base en estos datos, el programa realiza los siguientes cálculos:

Área del muro (m²) multiplicando el largo por la altura.
Volumen del aplanado (m³) al considerar el grosor indicado, convirtiendo automáticamente los centímetros a metros.

Cálculo de materiales necesarios por metro cúbico de mortero, aplicando la proporción establecida:

Cemento (kg) → con base en la densidad y la proporción 1:4.
Arena (kg y latas) → el peso total se convierte también en equivalentes de latas para una interpretación práctica en obra.
Agua (litros y cubetadas) → considerando una cubeta de 19 litros, el resultado se expresa en número de cubetadas o fracciones (por ejemplo, “1 cubetada y media”).
