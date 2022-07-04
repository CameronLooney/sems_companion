import pandas as pd
import streamlit as st
def excel(excl_merged):
    import io
    buffer = io.BytesIO()
    writer = pd.ExcelWriter(buffer)

    excl_merged.to_excel(writer, index=False)
    worksheet = writer.sheets['Sheet1']

    # Get the dimensions of the dataframe.
    (max_row, max_col) = excl_merged.shape

    # Set the column widths, to make the dates clearer.
    worksheet.set_column(1, max_col, 20)
    writer.save()
    return buffer




# download file
def download(buffer):
    st.download_button(
        label="Download Excel worksheets",
        data=buffer,
        file_name="Merged.xlsx",
        mime="application/vnd.ms-excel"
    )