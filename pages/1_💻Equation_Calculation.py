import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Thêm biểu tượng toán học
def math_icon():
    st.markdown(
        """<style>
            .math-icon {
                display: flex;
                align-items: center;
                margin-right: 8px;
            }
            .math-icon img {
                margin-right: 8px;
                width: 24px;
                height: 24px;
            }
            .math-icon p {
                font-size: 20px;
                font-weight: bold;
                color: #0366d6;
            }
            </style>
        """
        ,
        unsafe_allow_html=True,
    )

    st.markdown(
        """<div class="math-icon">
        <img src="https://giasuviet.net.vn/app/uploads/2017/11/ph%C6%B0%C6%A1ng-ph%C3%A1p-t%E1%BB%91t-nh%E1%BA%A5t-gi%C3%BAp-b%C3%A9-h%E1%BB%8Dc-to%C3%A1n.png" alt="math-icon">
        <p>Phương Trình Bậc 2:</p>
        </div>""",
        unsafe_allow_html=True,
    )

def gptb2(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    if a == 0:
        if b == 0:
            if c == 0:
                ket_qua = 'PTB1 có vô số nghiệm'
            else:
                ket_qua = 'PTB1 vô nghiệm'
        else:
            x_nghiem = -c / b
            ket_qua = 'PTB1 có nghiệm x = %.2f' % x_nghiem
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            ket_qua = 'PTB2 vô nghiệm'
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            ket_qua = 'PTB2 có nghiệm x1 = %.2f và x2 = %.2f' % (x1, x2)

    return ket_qua, x, y

def clear_input():
    st.session_state["nhap_a"] = 0.0
    st.session_state["nhap_b"] = 0.0
    st.session_state["nhap_c"] = 0.0

# Tính năng thêm màu sắc và biểu tượng toán học
st.set_page_config(
    page_title="Giải Phương Trình Bậc 2",
    page_icon=":heavy_exclamation_mark:",
    layout="wide",
)

# Màu nền chung
st.markdown(
    """<style>
        body {
            background-color: #f8f9fa;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Tiêu đề
st.title("Giải Phương Trình Bậc 2")

math_icon()

state = st.session_state.get("state", {"tab": "giai_phuong_trinh", "a": 0.0, "b": 0.0, "c": 0.0})

tabs = ["Giải phương trình", "Vẽ đồ thị"]
selected_tab = st.selectbox(" ", tabs, key="selectbox")

if selected_tab == "Giải phương trình":
    state["tab"] = "giai_phuong_trinh"
    with st.form(key='columns_in_form', clear_on_submit=False):
        st.subheader('Nhập các hệ số')
        state["a"] = st.number_input('Nhập a', key='nhap_a')
        state["b"] = st.number_input('Nhập b', key='nhap_b')
        state["c"] = st.number_input('Nhập c', key='nhap_c')

        btn_giai = st.form_submit_button('Giải')
        btn_xoa = st.form_submit_button('Xóa', on_click=clear_input)

    if btn_giai:
        s, x, y = gptb2(state["a"], state["b"], state["c"])
        st.markdown('<h3 style="color:#0366d6; font-size:24px;">Kết quả:</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:18px; color:#0366d6;">{s}</p>', unsafe_allow_html=True)



elif selected_tab == "Vẽ đồ thị":
    state["tab"] = "do_thi"
    s, x, y = gptb2(state["a"], state["b"], state["c"])
    st.markdown('### Đồ thị phương trình bậc 2')
    fig, ax = plt.subplots()
    ax.plot(x, y, label='y = %.2fx^2 + %.2fx + %.2f' % (state["a"], state["b"], state["c"]))
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Đồ thị phương trình bậc 2')
    st.pyplot(fig)

# Lưu trạng thái
st.session_state["state"] = state
