# Plant Disease Detection Using AI

## Overview

Plant Disease Detection is an Artificial Intelligence and Computer Vision project designed to identify diseases in plant leaves using image analysis. The system helps farmers and agricultural experts detect diseases at an early stage, reducing crop loss and improving productivity.

## Objectives

* Detect plant diseases automatically from leaf images.
* Provide fast and accurate disease diagnosis.
* Assist farmers in taking timely preventive measures.
* Improve agricultural productivity through AI-driven solutions.

## Features

* Image-based disease detection.
* Deep Learning-powered classification.
* Support for multiple plant species.
* Real-time disease prediction.
* User-friendly interface for image upload.
* High accuracy and quick results.

## System Workflow

1. User uploads an image of a plant leaf.
2. The image is preprocessed and resized.
3. The trained AI model analyzes the image.
4. Disease classification is performed.
5. The detected disease and confidence score are displayed.
6. Recommendations for disease management can be provided.

## Technologies Used

* Python
* TensorFlow / Keras
* Convolutional Neural Networks (CNN)
* OpenCV
* NumPy
* Pandas
* Matplotlib
* Flask / Streamlit

## Dataset

The model is trained on plant leaf image datasets containing healthy and diseased plant samples.

### Example Disease Classes

* Healthy Leaf
* Tomato Early Blight
* Tomato Late Blight
* Potato Early Blight
* Potato Late Blight
* Corn Rust
* Apple Scab
* Grape Black Rot

## Model Architecture

* Input Layer
* Convolutional Layers
* Pooling Layers
* Fully Connected Layers
* Softmax Output Layer

## Installation

```bash
git clone <repository-url>
cd plant-disease-detection
pip install -r requirements.txt
```

## Running the Project

```bash
python app.py
```

or

```bash
streamlit run app.py
```

## Example

### Input

Plant leaf image uploaded by user.

### Output

```text
Disease: Tomato Late Blight
Confidence Score: 96.8%
Status: Diseased
```

## Applications

* Smart Farming
* Precision Agriculture
* Crop Health Monitoring
* Agricultural Research
* Disease Surveillance Systems

## Advantages

* Early disease detection.
* Reduces crop losses.
* Saves time and manual effort.
* Supports farmers in decision-making.
* Cost-effective monitoring solution.

## Future Enhancements

* Mobile application integration.
* Real-time camera-based detection.
* Disease treatment recommendations.
* Multilingual support.
* Cloud-based deployment.
* Integration with IoT sensors and smart farming systems.

## Project Structure

```text
plant-disease-detection/
│
├── dataset/
├── models/
├── static/
├── templates/
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

## Conclusion

The Plant Disease Detection AI Model leverages Artificial Intelligence and Deep Learning techniques to identify plant diseases accurately from leaf images. This solution helps farmers and agricultural professionals detect problems early, improve crop health, and increase overall agricultural productivity.
