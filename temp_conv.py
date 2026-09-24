"""Core temperature conversion logic.

Originally written as a simple command-line script; kept dependency-free
(NumPy only) so it can be reused outside the Streamlit UI in app.py.
"""

import numpy as np
import pandas as pd


def fahrenheit_to_celsius(f_array: np.ndarray) -> np.ndarray:
    """Convert an array of Fahrenheit values to Celsius."""
    return (f_array - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(c_array: np.ndarray) -> np.ndarray:
    """Convert an array of Celsius values to Fahrenheit."""
    return (c_array * 9.0 / 5.0) + 32


def main() -> None:
    """Small CLI entry point, kept for standalone/offline use."""
    print("Temperature Conversion Program")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        values = input("Enter Fahrenheit values separated by commas: ")
        f_values = np.array([float(x.strip()) for x in values.split(",")])
        c_values = fahrenheit_to_celsius(f_values)
        df = pd.DataFrame({"Fahrenheit": f_values, "Celsius": c_values})
        print("\nConversion Results:")
        print(df)
    elif choice == "2":
        values = input("Enter Celsius values separated by commas: ")
        c_values = np.array([float(x.strip()) for x in values.split(",")])
        f_values = celsius_to_fahrenheit(c_values)
        df = pd.DataFrame({"Celsius": c_values, "Fahrenheit": f_values})
        print("\nConversion Results:")
        print(df)
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
