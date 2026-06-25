import streamlit as st
import numpy as np
import tensorflow as tf
from disease_info import disease_info
from PIL import Image

st.set_page_config(
page_title="AI Plant Disease Detection",
page_icon="🌿",
layout="wide",
)

st.markdown("""
<style>
.main{
        background-color: #0E1117
            }
            

.title{
            text-align : center;
            color : #00FF99;
            font-size: 42px;
            font-weight: bold;
        }
.subtitle{
            text-align: center;
            color: #CCCCCC;
            font-size : 18px;
        }
.card{
            background-color: #1E1E1E;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0px 0px 10px rgba(0,255,150,0.2);
        }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('plant_disease_model.h5')

model = load_model()

with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

st.markdown("<p class='title'>🌿 AI Plant Disease Detection</p>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Upload a leaf image and get disease prediction</p>", unsafe_allow_html=True)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

    img = image.resize((224,224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    prediction_index = np.argmax(prediction)
    predicted_class = class_names[prediction_index]
    confidence = float(np.max(prediction)) * 100

    with col2:
     
        st.markdown(f"""
                    <div class="card">
                    <h3> Predicted Disease</h3>
                    <h2>{predicted_class}</h2>\
                    </div>
                    """,
                    unsafe_allow_html=True
                    )
        
        st.markdown(f"""
                    <div class="card">
                    <h3> Confidence Score</h3>
                    <h2>{confidence:.2f}%</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                    )
        
        st.progress(confidence / 100)

        if confidence > 90:
            st.success("High confidence in prediction!")
        elif confidence > 70:
            st.warning("Moderate confidence in prediction")
        else:
            st.error("Low confidence in prediction. Please check the image quality or try another image.")

        if predicted_class in disease_info:
            st.markdown("### Description")
            st.write(disease_info[predicted_class]["description"])
            st.markdown("### Treatment")
            st.write(disease_info[predicted_class]["treatment"])
            st.markdown("### Prevention tips")
            st.write(disease_info[predicted_class]["prevention"])
        else:
            st.warning("Disease information not available. ")
        
            st.divider()

            st.subheader("Top 3 Predictions")

            top3 = np.argsort(prediction[0])[-3:][::-1]

            for idx in top3:

                disease_name = class_names[idx]

                score = prediction[0][idx] * 100

                st.write(f"**{disease_name}** = {score:.2f}%")

                st.progress(score / 100)
            
