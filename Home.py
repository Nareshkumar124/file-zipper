import streamlit as st

st.page_link("pages/unzip.py", label="Unzip File", icon="1️⃣")


# code 

# code to compress file
import zipfile
import os

def compress_files(files, output_zip):
    """
    Compresses files into a zip archive.
    
    Args:
    - files: List of file paths to be compressed.
    - output_zip: Path to the output zip file.
    """
    with zipfile.ZipFile(output_zip, 'w') as zip_ref:
        for file in files:
            zip_ref.write(file, os.path.basename(file))

st.title("File compresser")

from io import StringIO
import uuid

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    input=f"./input/{uuid.uuid4()}.txt"
    with open(input,'w')as f:
        f.write(stringio.read())
    
    output=f"./output/{uuid.uuid4()}.zip"
    compress_files([input],output)
    
    
    with open(output,"rb") as f:
        data=f.read()
    
    st.download_button(
    label="Download data",
    data=data,
    file_name=output,
    mime='.zip',
    )
        
        
    


    