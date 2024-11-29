import streamlit as st
import os
import json
from organize import organize_files, load_config

# Set Streamlit page config
st.set_page_config(
    page_title="File Organizer",
    page_icon="📁",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load file type mappings
config_path = "config.json"
file_types = load_config()

# Sidebar with app info
with st.sidebar:
    st.title("📁 File Organizer")
    st.write(
        """
        Organize your files effortlessly into categorized folders. 
        - Customize file type mappings.
        - View logs of the organization process.
        """
    )
    st.write("💡 Tip: Ensure the directory path is accessible.")
    st.markdown("---")
    st.info("Developed with ❤️ using Streamlit!")

# Main app content
st.title("File Organizer")
st.markdown(
    """
    ### 🚀 Organize Files with Ease
    Enter a directory path and let this tool sort your files into subfolders based on their type.
    """
)

# Directory input
directory = st.text_input("🔍 Enter the directory path to organize:", "")

# Customize file type mappings
if st.checkbox("🔧 Customize File Type Mappings"):
    st.markdown("### ✏️ Edit File Type Mappings Below:")
    custom_mappings = st.text_area(
        "Enter mappings in JSON format:",
        value=json.dumps(file_types, indent=4),
        height=250,
    )

    if st.button("💾 Save Custom Mappings"):
        try:
            file_types = json.loads(custom_mappings)
            with open(config_path, "w") as config_file:
                json.dump(file_types, config_file, indent=4)
            st.success("File type mappings updated successfully!")
        except json.JSONDecodeError:
            st.error("Invalid JSON format. Please check and try again.")

# Organize Files Button
if st.button("🗂️ Organize Files"):
    if directory:
        with st.spinner("Organizing files..."):
            result = organize_files(directory, file_types)
        st.success(result)
    else:
        st.error("Please enter a valid directory path.")

# Display Logs
if st.checkbox("📜 Show Logs"):
    st.markdown("### 📋 Logs of File Organization:")
    if os.path.exists("logs/organization.log"):
        with open("logs/organization.log", "r") as log_file:
            logs = log_file.read()
        st.text_area("Logs", logs, height=200)
    else:
        st.warning("No logs available yet.")

# Footer
st.markdown("---")
st.markdown(
    """
    #### Made with ❤️ by [Jaiganesh](https://github.com/Jaiganesh235)
    """
)
