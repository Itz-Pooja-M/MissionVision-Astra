import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(
    page_title="MissionVision AI",
    page_icon="🎯"
)

st.title("🎯 MissionVision AI")
st.subheader("AI-Based Defence Object Recognition System")

st.write(
    "Upload an image and the AI model will identify "
    "the most likely defence-related object."
)


@st.cache_resource
def load_model():
    return pipeline(
        "zero-shot-image-classification",
        model="openai/clip-vit-base-patch32"
    )


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    try:
        # -------------------------------
        # STEP 1: Open and process image
        # -------------------------------
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.success("Image uploaded successfully!")

        # -------------------------------
        # Load AI model
        # -------------------------------
        with st.spinner("🤖 Analysing image..."):

            model = load_model()

            # -------------------------------
            # STEP 2: VALIDITY CHECK
            # -------------------------------
            validity_results = model(
                image,
                candidate_labels=[
                    "a defence-related military object",
                    "a non-defence ordinary object"
                ]
            )

            defence_score = validity_results[0]["score"]
            defence_label = validity_results[0]["label"]

            # -------------------------------
            # STEP 3: Reject invalid images
            # -------------------------------
            if (
                defence_label == "a non-defence ordinary object"
                or defence_score < 0.60
            ):

                st.divider()
                st.error("❌ Invalid Image")

                st.write(
                    "The uploaded image does not appear to contain "
                    "a supported defence-related object."
                )

                st.info(
                    "Please upload an image containing a fighter "
                    "aircraft, helicopter, tank, military vehicle, "
                    "naval ship, or drone."
                )

                st.stop()

            # -------------------------------
            # STEP 4: Defence object classification
            # -------------------------------
            categories = [
                "fighter aircraft",
                "helicopter",
                "tank",
                "military vehicle",
                "naval ship",
                "drone"
            ]

            results = model(
                image,
                candidate_labels=categories
            )

        # -------------------------------
        # STEP 5: Get best prediction
        # -------------------------------
        best_result = results[0]

        predicted_object = best_result["label"]
        confidence = best_result["score"]

        # -------------------------------
        # STEP 6: Display result
        # -------------------------------
        st.divider()

        st.header("🔍 Recognition Result")

        st.success(
            "Predicted Object: "
            + predicted_object.title()
        )

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        # -------------------------------
        # STEP 7: Confidence warning
        # -------------------------------
        if confidence < 0.45:

            st.warning(
                "⚠️ Low confidence prediction. "
                "Please verify the result."
            )

        else:

            st.info(
                "The model produced a relatively strong prediction."
            )

        # -------------------------------
        # STEP 8: Top 3 predictions
        # -------------------------------
        st.subheader("📊 Top 3 Predictions")

        for number, result in enumerate(
            results[:3],
            start=1
        ):

            label = result["label"]
            score = result["score"]

            st.write(
                f"{number}. {label.title()} - "
                f"{score * 100:.2f}%"
            )

        # -------------------------------
        # STEP 9: Explanation
        # -------------------------------
        st.subheader("💡 Explanation")

        st.write(
            "The AI model compared the uploaded image "
            "with the selected defence-related categories. "
            "The highest matching category was "
            + predicted_object.title()
            + " with a score of "
            + f"{confidence * 100:.2f}%."
        )

    except Exception:

        st.error(
            "❌ The image could not be processed."
        )

        st.write(
            "Please upload a valid JPG, JPEG, or PNG image."
        )

else:

    st.info(
        "Upload a defence-related image to begin."
    )


st.divider()

st.caption(
    "MissionVision AI | ASTRA VISION"
)