import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

# -------------- SETTINGS --------------
page_title = "Trang giới thiệu"
page_icon = ":tada"  # emoji mô tả trang web của bạn
layout = "wide"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
# st.title(page_title + " " + page_icon)
# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/css/style.css")
local_css("./pages/css/clone.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/1d55fc8a-2879-48bf-8851-f6445c66132a/6fo20JApSj.json")
img_contact_form = Image.open("./data/images/calculate.png")
img_chuso = Image.open("./data/images/chuso.png")
img_human = Image.open("./data/images/human.png")
img_object = Image.open("./data/images/object.png")
img_fruit = Image.open("./data/images/fruit.png")
img_number = Image.open("./data/images/sign.png")
img_process = Image.open("./data/images/img_process.png")
img_hand=Image.open("./data/images/okay-JPG-5442-1380073443-2910-1380077076.jpg")


st.markdown(
    f'<img src="https://fit.hcmute.edu.vn/Resources/Images/SubDomain/fit/HCMUTE-fit.png" alt="ảnh đồ án" class="custom-image-class">',
    unsafe_allow_html=True
)

# ---- HEADER SECTION ----
with st.container():
    st.markdown(
        f'<h1 style="text-align: center"> XỬ LÝ ẢNH SỐ </h1>' '</br>' ,
        unsafe_allow_html=True
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns([2,1])
    with open("./pages/html/card.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    with left_column:
        st.markdown(html_content, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding, height=367,width=200, key="coding")

st.header("My Projects")
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, width=150)
    with text_column:
        st.subheader("Module 1: GIẢI PHƯƠNG TRÌNH BẬC HAI")
        st.write(
            """
            👉 Giải phương trình bậc 2: ax2+bx+c=0 (a≠0) \n
            👉 Phương trình: Có nghiệm - Vô nghiệm - Vô số nghiệm 
            """
        )
        st.markdown('<a href="GiaiPhuongTrinhBac2" target="_self">Phương trình bậc 2🧮</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_human, width=150)
    with text_column:
        st.subheader("Module 2: NHẬN DẠNG GƯƠNG MẶT")
        st.write(
            """
            👉 NHẬN DẠNG GƯƠNG MẶT -  NHẬN DIỆN 5 Người trong 1 khuôn hình
            """
        )
        st.markdown('<a href="Face_Recognition" target="_self">Nhận diện khuôn mặt 🧑</a>', unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_object, width=150)
    with text_column:
        st.subheader("Module 3: NHẬN DẠNG ĐỐI TƯỢNG")
        st.write(
            """
            👉 Phát hiện theo từng loại đối tượng khác nhau\n
            👉 person - bicycle - car - motorbike - aeroplane - bus - train - truck - boat
            """
        )
        st.markdown('<a href="Object_detection" target="_self">Nhận diện đối tượng 👨‍👩‍👧‍👦</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_number, width=150)
    with text_column:
        st.subheader("Module 4: NHẬN DẠNG CHỮ SỐ VIẾT TAY")
        st.write(
            """
            👉 Nhận dạng chữ - số viết tay Mnist 
            """
        )
        st.markdown('<a href="Mnist_detection" target="_self">Nhận diện chữ số viết tay ✍️</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_fruit, width=150)
    with text_column:
        st.subheader("Module 5: NHẬN DIỆN TRÁI CÂY")
        st.write(
            """
            👉 Nhận diện các loại trái cây khác nhau, bao gồm 15 loại trái cây được trainning trong file onnx.
            👉 Dualeo - Tao - Kiwi - Chuoi - Cam - Dua - Dao - Chery - Le - Luu - Thom - Thom - Duahau - Dualuoi - Nho - Dau
            """
        )
        st.markdown('<a href="Fruit_detection" target="_self">Nhận diện các loại trái cây 🍉</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_process, width=150)
    with text_column:
        st.subheader("Module 6: XỬ LÝ ẢNH")
        st.write(
            """
            👉 Bao gồm 4 Chapter 3, 4, 5, 9\n
            
            """
        )
        st.markdown('<a href="Image_Processing" target="_self">Xử lý ảnh 📷</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_hand, width=150)
    with text_column:
        st.subheader("Module 7: NHẬN DIỆN KÍ HIỆU TAY")
        st.write(
            """
            👉 Chỉ nhận dạng được 3 kí hiệu\n
            
            """
        )
        st.markdown('<a href="Hand_Detection" target="_self">Xử lý ảnh 📷</a>', unsafe_allow_html=True)