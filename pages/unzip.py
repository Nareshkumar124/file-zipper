import streamlit as st

import zipfile
import os

st.title("UnZip File")

import io
import uuid

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Create a temporary directory to extract the ZIP contents
    temp_dir = f"./unzip/{uuid.uuid4()}"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Read the ZIP file and extract its contents
    with zipfile.ZipFile(io.BytesIO(uploaded_file.read()), 'r') as zip_ref:
        # Extract all contents to the temporary directory
        zip_ref.extractall(temp_dir)

    st.success("ZIP file extracted successfully!")

    # Display the list of extracted files
    extracted_files = os.listdir(temp_dir)
    st.write("Extracted files:")
    for file_name in extracted_files:
        st.download_button(
            label=f"Download {file_name}",
            data=open(f"{temp_dir}/{file_name}").read(),
            file_name=file_name,
            mime='.txt',
    )

    if st.button("Delete extracted files"):
        # Clean up the temporary directory
        for file_name in extracted_files:
            os.remove(os.path.join(temp_dir, file_name))
        os.rmdir(temp_dir)
        st.success("Extracted files deleted successfully!")
