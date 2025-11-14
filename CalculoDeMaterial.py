import tkinter as tk
from tkinter import messagebox

# ======== Función auxiliar para convertir decimales en fracciones ========
def fraccionar(valor):
    entero = int(valor)
    decimal = valor - entero

    if decimal < 0.13:
        fraccion = ""
    elif decimal < 0.38:
        fraccion = " un cuarto"
    elif decimal < 0.63:
        fraccion = " media"
    elif decimal < 0.88:
        fraccion = " tres cuartos"
    else:
        entero += 1
        fraccion = ""

    if entero == 0 and fraccion != "":
        return f"{fraccion.strip()}"
    elif fraccion != "":
        return f"{entero} y{fraccion}"
    else:
        return f"{entero}"

# ======== Cálculo principal ========
def calcular_materiales():
    try:
        largo = float(entry_largo.get())
        alto = float(entry_alto.get())
        grosor_cm = float(entry_grosor.get())

        area = largo * alto
        grosor_m = grosor_cm / 100
        volumen = area * grosor_m

        # proporción 1:4 (cemento : arena)
        proporcion_cemento = 1
        proporcion_arena = 4
        densidad_mortero = 1750  # kg/m³
        masa_total = volumen * densidad_mortero
        partes = proporcion_cemento + proporcion_arena

        masa_cemento = masa_total * (proporcion_cemento / partes)
        masa_arena = masa_total * (proporcion_arena / partes)
        masa_agua = masa_cemento * 0.5  # relación agua/cemento 0.5

        # Conversiones
        kg_por_saco = 25
        sacos = masa_cemento / kg_por_saco

        kg_por_lata = 27  # 1 lata ≈ 27 kg de arena seca
        latas = masa_arena / kg_por_lata

        litros_por_cubeta = 19
        cubetas = masa_agua / litros_por_cubeta

        resultado = (
            f"RESULTADOS:\n"
            f"Área: {area:.2f} m²\n"
            f"Volumen: {volumen:.3f} m³\n\n"
            f" Cemento: {masa_cemento:.1f} kg → {fraccionar(sacos)} sacos de 25 kg\n"
            f" Arena: {masa_arena:.1f} kg → {fraccionar(latas)} latas\n"
            f" Agua: {masa_agua:.1f} L → {fraccionar(cubetas)} cubetadas\n"
        )

        text_resultado.config(state="normal")
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado)
        text_resultado.config(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

# ======== Interfaz gráfica ========
root = tk.Tk()
root.title("Calculadora de Materiales para Aplanado")
root.geometry("500x500")
root.resizable(False, False)

titulo = tk.Label(root, text="CÁLCULO DE MATERIALES PARA APLANADO", font=("Arial", 13, "bold"))
titulo.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

# Entradas
tk.Label(frame, text="Largo del muro (m):", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_largo = tk.Entry(frame, width=10)
entry_largo.grid(row=0, column=1)

tk.Label(frame, text="Altura del muro (m):", font=("Arial", 11)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_alto = tk.Entry(frame, width=10)
entry_alto.grid(row=1, column=1)

tk.Label(frame, text="Grosor del aplanado (cm):", font=("Arial", 11)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_grosor = tk.Entry(frame, width=10)
entry_grosor.grid(row=2, column=1)

# Botón
btn_calcular = tk.Button(root, text="Calcular Materiales", command=calcular_materiales, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
btn_calcular.pack(pady=10)

# Caja de resultados
text_resultado = tk.Text(root, height=10, width=55, wrap="word", state="disabled", font=("Arial", 10))
text_resultado.pack(pady=10)

# Pie
pie = tk.Label(root, text="Basado en proporción 1:4 (cemento:arena) según NMX-C-486-ONNCCE-2014", font=("Arial", 8), fg="gray")
pie.pack(side="bottom", pady=5)

root.mainloop()