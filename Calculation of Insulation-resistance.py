# Calculation of Insulation-resistance.py

V = float(input("Enter the applied voltage (V): "))
I = float(input("Enter the leakage current (A): "))

R = V / I

print("Insulation Resistance =", R, "Ohms")
