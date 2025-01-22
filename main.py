import streamlit as st
from rembg import remove
from PIL import Image
import io

# App Title
st.title("Sprite Editor Web App")

# Upload Image
uploaded_file = st.file_uploader("Upload a Sprite Image", type=["png", "jpg", "jpeg"])

# Sidebar for Options
st.sidebar.header("Editing Options")
resize_width = st.sidebar.slider("Resize Width", 10, 500, 100)
remove_background = st.sidebar.checkbox("Remove Background")

# Process Image
if uploaded_file:
    # Display Uploaded Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Sprite", use_column_width=True)

    # Remove Background
    if remove_background:
        st.write("Removing background...")
        bg_removed_image = remove(image.tobytes())
        image = Image.open(io.BytesIO(bg_removed_image))
        st.image(image, caption="Background Removed Sprite", use_column_width=True)

    # Resize Image
    if resize_width:
        aspect_ratio = image.height / image.width
        new_height = int(resize_width * aspect_ratio)
        resized_image = image.resize((resize_width, new_height))
        st.image(resized_image, caption=f"Resized Sprite ({resize_width} px)", use_column_width=True)

        # Option to Download Resized Image
        buf = io.BytesIO()
        resized_image.save(buf, format="PNG")
        st.download_button(
            label="Download Edited Sprite",
            data=buf.getvalue(),
            file_name="edited_sprite.png",
            mime="image/png",
        )
