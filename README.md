# 🎯 MissionVision AI

### AI-Based Defence Object Recognition System

MissionVision AI is an AI-powered computer vision application designed to identify and classify selected defence-related objects from images.

The system allows a user to upload an image, processes it using a pre-trained CLIP vision-language model, and predicts the most likely supported object category along with a model score.

---

## 🎯 Objective

The objective of MissionVision AI is to demonstrate how computer vision and AI can be used to transform visual defence-related data into fast, structured, and understandable classification results.

The system focuses on a limited set of defence-related categories rather than attempting to identify every possible object.

---

## ✨ Features

- 📤 Image upload through a Streamlit interface
- 🖼️ Image preprocessing using PIL
- 🤖 Pre-trained CLIP AI model
- 🔍 Defence-object classification
- 📊 Confidence/model score display
- 🥇 Top-3 predictions
- ⚠️ Low-confidence warning
- ❌ Invalid/non-defence image handling
- 🛡️ Error handling for unsupported or invalid images
- ⚡ Model caching for faster repeated predictions

---

## 🧠 Supported Categories

MissionVision AI currently supports:

1. Fighter Aircraft
2. Helicopter
3. Tank
4. Military Vehicle
5. Naval Ship
6. Drone

---

## 🏗️ System Architecture

The application follows this workflow:

**Image Input → Preprocessing → AI/CV Model → Object Classification → Confidence Analysis → Result & Explanation**

The user uploads an image through the Streamlit interface. The image is opened and converted to RGB format using PIL. It is then passed to the pre-trained CLIP model through the Hugging Face Transformers pipeline.

CLIP compares the image with the predefined defence-related candidate categories and produces scores. The results are ranked and displayed to the user.

The application also performs an initial validity check to identify images that do not appear to contain supported defence-related objects.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| Hugging Face Transformers | AI model pipeline |
| CLIP | Zero-shot image classification |
| PyTorch | Deep learning framework |
| Torchvision | Computer vision support |
| Pillow (PIL) | Image processing |

---

## 🤖 AI Model

MissionVision AI uses the pre-trained:

**OpenAI CLIP — `openai/clip-vit-base-patch32`**

CLIP is a vision-language model that learns relationships between images and text.

In this project, it is used for zero-shot image classification. Instead of training a new classifier from scratch, the uploaded image is compared with predefined text categories.

### Why a pre-trained model?

Training a computer-vision model from scratch would require a suitable labelled dataset, significant computational resources, and additional training time.

A pre-trained model allows the project to demonstrate the required computer-vision workflow within the available development time.

---

## 🔄 How the System Works

### Step 1 — Image Upload

The user uploads a JPG, JPEG, or PNG image.

### Step 2 — Image Preprocessing

PIL opens the image and converts it into RGB format.

### Step 3 — Validity Check

The system first checks whether the image appears to contain a supported defence-related object.

If the image appears unrelated, the system displays an invalid-image message instead of continuing with object classification.

### Step 4 — AI Classification

The image is passed to the CLIP model together with the supported candidate categories.

### Step 5 — Ranking

The model produces scores for the candidate categories and ranks them.

### Step 6 — Result

The application displays:

- Predicted object
- Model score
- Top-3 predictions
- Confidence warning when appropriate
- Short explanation

---

## 🧪 Testing

The system was tested using representative images from the supported categories, including:

- Fighter aircraft
- Helicopter
- Tank
- Drone
- Naval ship
- Military vehicle

The system was also tested using unrelated/non-defence images to verify invalid-image handling.

### Observed Limitation

During testing, a tank image was classified as:

**Military Vehicle — 95.63%**

while:

**Tank — 2.28%**

This demonstrates a limitation of the current zero-shot approach. A tank is also a military vehicle, and the general-purpose CLIP model may prefer the broader category.

The result shows why the displayed score should not be interpreted as guaranteed real-world accuracy.

---

## ⚠️ Limitations

- The current model is a general-purpose zero-shot CLIP model rather than a defence-specific fine-tuned classifier.
- Similar or overlapping categories may sometimes be confused.
- Image quality and image composition can affect predictions.
- The model score should not be interpreted as guaranteed real-world accuracy.
- The system is limited to the predefined categories.
- The current system is intended as an AI-assisted classification demonstration and not as an authoritative identification system.

---

## 🚀 Future Improvements

Possible future enhancements include:

- Fine-tuning a vision model using a curated defence-object dataset
- Multi-object detection
- Bounding-box visualization
- Model comparison
- Systematic performance metrics
- Batch image processing
- Image history
- Explainable AI techniques
- Improved handling of unknown objects

---

## 📂 Project Structure

```text
MissionVision-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
└── assets/
    └── architecture.png