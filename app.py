import io
import requests
import streamlit as st
from PIL import Image

# Free Hugging Face Serverless API endpoint for Stable Diffusion v1.5
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

# You can get a free token from huggingface.co -> Settings -> Access Tokens
# For public demos, you can use a free token or input field
st.title("🎨 Free AI Image Generator")
st.markdown("Generate images instantly using Stable Diffusion v1.5 without writing code or paying for hardware!")

prompt = st.text_input("Enter your prompt:", "A futuristic city at sunset, highly detailed")
hf_token = st.text_input("Hugging Face Access Token (Free):", type="password", help="Get a free token from huggingface.co settings")

if st.button("Generate Image", type="primary"):
  if not prompt:
    st.warning("Please enter a prompt first.")
  elif not hf_token:
    st.warning("Please enter your free Hugging Face token to call the API.")
  else:
    with st.spinner("Generating image via cloud API..."):
      headers = {"Authorization": f"Bearer {hf_token}"}
      payload = {"inputs": prompt}

      response = requests.post(API_URL, headers=headers, json=payload)

      if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        st.image(image, caption=prompt, use_column_width=True)
        st.success("Image generated successfully!")
      else:
        st.error(f"Error: {response.text}")
