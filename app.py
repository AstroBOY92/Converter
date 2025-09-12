import numpy as np
import pandas as pd
import streamlit as st

# import your functions from the existing module
from temp_conv import fahrenheit_to_celsius, celsius_to_fahrenheit

st.set_page_config(page_title="Temp Converter", page_icon="🌡️", layout="centered")

st.title("🌡️ Temperature Converter")
st.caption("Fahrenheit ↔︎ Celsius, with NumPy + Pandas")

# --- Sidebar controls ---
st.sidebar.header("Conversion Settings")
direction = st.sidebar.radio(
    "Select conversion",
    ("Fahrenheit → Celsius", "Celsius → Fahrenheit"),
)

precision = st.sidebar.slider("Decimal places", 0, 6, 2)

st.sidebar.markdown("---")
st.sidebar.write("Input options:")
input_mode = st.sidebar.radio(
    "How will you provide values?",
    ("Type/Paste values", "Upload CSV file")
)

# --- Helpers ---
def parse_numbers(text: str) -> np.ndarray:
    if not text.strip():
        return np.array([], dtype=float)
    # support commas, spaces, semicolons, newlines
    parts = [p for chunk in text.replace(";", ",").replace("\n", ",").split(",")
             for p in chunk.split()]
    return np.array([float(x) for x in parts if x.strip() != ""], dtype=float)

def convert_array(arr: np.ndarray, to_celsius: bool) -> pd.DataFrame:
    if to_celsius:
        c_vals = fahrenheit_to_celsius(arr)
        df = pd.DataFrame({"Fahrenheit": arr, "Celsius": c_vals})
    else:
        f_vals = celsius_to_fahrenheit(arr)
        df = pd.DataFrame({"Celsius": arr, "Fahrenheit": f_vals})
    return df

# --- Input section ---
st.subheader("Enter temperatures")

values_array = None
uploaded_name = None

if input_mode == "Type/Paste values":
    example = "32, 100, 212" if direction.startswith("Fahrenheit") else "0 37.5 100"
    text = st.text_area(
        "Enter numbers (comma/space/newline separated):",
        value=example,
        height=120,
        help="You can separate values by commas, spaces, semicolons, or new lines."
    )
    try:
        values_array = parse_numbers(text)
    except ValueError:
        st.error("Please enter only numeric values.")
        values_array = np.array([], dtype=float)
else:
    file = st.file_uploader("Upload a CSV with one column of numbers", type=["csv"])
    if file is not None:
        try:
            df_in = pd.read_csv(file)
            # take the first numeric column
            num_cols = [c for c in df_in.columns if pd.api.types.is_numeric_dtype(df_in[c])]
            if not num_cols:
                st.error("No numeric columns found. Please upload a CSV with at least one numeric column.")
            else:
                values_array = df_in[num_cols[0]].to_numpy(dtype=float)
                uploaded_name = file.name
                st.info(f"Using numeric column: **{num_cols[0]}** from `{uploaded_name}`")
        except Exception as e:
            st.error(f"Couldn't read the CSV: {e}")

# --- Conversion & output ---
if values_array is None or values_array.size == 0:
    st.warning("Provide some values to convert.")
else:
    to_celsius = direction.startswith("Fahrenheit")
    df_out = convert_array(values_array, to_celsius)
    st.subheader("Results")
    st.dataframe(df_out.round(precision), use_container_width=True)

    # Simple summary stats
    with st.expander("Show summary statistics"):
        st.write(df_out.round(precision).describe())

    # Download buttons
    csv_bytes = df_out.round(precision).to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download CSV",
        data=csv_bytes,
        file_name="conversion_results.csv",
        mime="text/csv",
    )

    # Quick chart (just for fun)
    st.subheader("Quick visualization")
    if to_celsius:
        st.line_chart(df_out[["Fahrenheit", "Celsius"]])
    else:
        st.line_chart(df_out[["Celsius", "Fahrenheit"]])

st.markdown("---")
st.caption("Built with Streamlit, NumPy, and Pandas.")
