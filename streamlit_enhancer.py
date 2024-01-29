import streamlit as st
from PIL import Image, ImageEnhance

def enhance_image(image, enhancement_factor):
    img = Image.open(image)
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(enhancement_factor)
    return enhanced_img

def main():
    st.title("Image Enhancer")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        enhancement_factor = st.slider("Select Enhancement Factor", 0.1, 2.0, 1.0, 0.1)

        if st.button("Enhance"):
            enhanced_img = enhance_image(uploaded_file, enhancement_factor)
            st.image(enhanced_img, caption="Enhanced Image", use_column_width=True)

if __name__ == "__main__":
    main()
