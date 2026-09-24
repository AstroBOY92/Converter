"""Minimal unit tests for temp_conv.py — run with: pytest test_temp_conv.py"""

import numpy as np
from temp_conv import fahrenheit_to_celsius, celsius_to_fahrenheit


def test_freezing_point():
    assert fahrenheit_to_celsius(np.array([32.0]))[0] == 0.0


def test_boiling_point():
    assert fahrenheit_to_celsius(np.array([212.0]))[0] == 100.0


def test_body_temperature_roundtrip():
    c = np.array([37.0])
    f = celsius_to_fahrenheit(c)
    back_to_c = fahrenheit_to_celsius(f)
    assert np.allclose(back_to_c, c)


def test_vectorised_input():
    f_values = np.array([32.0, 100.0, 212.0])
    c_values = fahrenheit_to_celsius(f_values)
    np.testing.assert_allclose(c_values, [0.0, 37.777778, 100.0], rtol=1e-4)
