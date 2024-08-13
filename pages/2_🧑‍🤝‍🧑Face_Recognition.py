import streamlit as st
import numpy as np
import cv2 as cv
import joblib

# Thêm biểu tượng và tiêu đề
st.title("Nhận dạng khuôn mặt")

if "frame_stop" not in st.session_state:
    frame_stop = cv.imread("./data/image/stop.jpg")
    st.session_state.frame_stop = frame_stop
    print("Đã load stop.jpg")


# Hàm để hiển thị video
def show_video():
    FRAME_WINDOW.image(frame, channels="BGR")


# Hàm để nhận diện khuôn mặt và vẽ kết quả
def visualize(input, faces, results, fps, thickness=4, fontScale=1.2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            coords = face[:-1].astype(np.int32)
            cv.rectangle(
                input,
                (coords[0], coords[1]),
                (coords[0] + coords[2], coords[1] + coords[3]),
                (0, 255, 0),
                thickness,
            )
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness)

            # Hiển thị kết quả nhận diện trên video
            result = results[idx] if idx < len(results) else "Unknown"
            cv.putText(
                input,
                result,
                (coords[0], coords[1] - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                fontScale,
                (255, 0, 0),
                thickness,
            )

    cv.putText(
        input,
        "FPS: {:.2f}".format(fps),
        (1, 16),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )


# Nút Start và Stop
start_stop_container = st.container()
start_stop_button = start_stop_container.button("Stop/Start")

# Biến lưu trạng thái
if "stop" not in st.session_state:
    st.session_state.stop = False

if start_stop_button:
    st.session_state.stop = not st.session_state.stop

# Icon
st.image(
    "https://img.freepik.com/premium-vector/flat-people-portraits-smiling-human-icon-human-avatar-simple-cute-characters_191504-120.jpg?w=2000",
    width=50,
)

# Hiển thị video khi chạy
FRAME_WINDOW = st.image([])

# Kiểm tra trạng thái để hiển thị video hoặc hình ảnh dừng
if st.session_state.stop == True:
    FRAME_WINDOW.image(st.session_state.frame_stop, channels="BGR")
else:
    # Mô hình và dữ liệu
    svc = joblib.load("./train/model/Facedetection/svc.pkl")
    mydict = ["DucNhan", "CongDanh", "TanPhat", "ThayDuc", "tuongvy"]

    # Tạo mô hình nhận diện khuôn mặt
    detector = cv.FaceDetectorYN.create(
        "./train/model/Facedetection/face_detection_yunet_2023mar.onnx",
        "",
        (320, 320),
        0.9,
        0.3,
        5000,
    )

    recognizer = cv.FaceRecognizerSF.create(
        "./train/model/Facedetection/face_recognition_sface_2021dec.onnx", ""
    )

    tm = cv.TickMeter()

    # Kích thước video
    frameWidth = 1280
    frameHeight = 720

    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
    detector.setInputSize([frameWidth, frameHeight])

    results_list = []  # List lưu kết quả nhận diện khuôn mặt cho mỗi frame
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print("No frames grabbed!")
            break

        tm.start()
        faces = detector.detect(frame)
        tm.stop()

        frame_results = []
        if faces[1] is not None:
            for idx, face in enumerate(faces[1]):
                face_align = recognizer.alignCrop(frame, face)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)
                result = mydict[test_predict[0]]
                frame_results.append(result)

        visualize(frame, faces, frame_results, tm.getFPS())
        show_video()
