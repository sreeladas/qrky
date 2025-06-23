import streamlit as st
import qrcode
from PIL import Image
import io

st.title("QR Code Generator with Logo")

logo_file = st.file_uploader("Upload Logo Image", type=["jpg", "png"])
url = st.text_input("Enter URL or text", "https://www.geeksforgeeks.org/")
col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("QR Foreground Color", "#000000")
with col2:
    bg_color = st.color_picker("QR Background Color", "#ffffff")
logo_width = st.slider("Logo Width (px)", 30, 300, 100)
qr_box_size = st.slider("QR Code Size", 5, 20, 10)
qr_border = st.slider("QR Code Border", 0, 10, 1)

if logo_file and url:
    logo = Image.open(logo_file)
    wpercent = logo_width / float(logo.size[0])
    hsize = int(float(logo.size[1]) * wpercent)
    logo = logo.resize((logo_width, hsize), Image.LANCZOS)

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=qr_box_size,
        border=qr_border
    )
    qr.add_data(url)
    qr.make()
    qr_img = qr.make_image(fill_color=fill_color, back_color=bg_color).convert("RGB")

    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos)

    st.image(qr_img, caption="Generated QR Code")

    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    st.download_button("Download QR Code", buf.getvalue(), "qr_code.png", "image/png")

