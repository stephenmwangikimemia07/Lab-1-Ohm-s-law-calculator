


if resistance != 0:
        current = voltage / resistance
        power = current * voltage  # Calculate power
        print("Current (A):", current)
       while True:
    try:
        voltage = float(input("Enter the voltage (V): "))
        resistance = float(input("Enter the resistance (Ohms): "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for voltage and resistance.")
        continue
 print("Power (W):", power)  # Display power
    else:
        print("Error: Resistance cannot be zero.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break

"""LAB 1 Ohm's law calculator"""

