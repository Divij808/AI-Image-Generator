# Local AI Image Generator & Editor 🎨

A **local AI-powered image generation and editing application** built with Python and Stable Diffusion.

The project allows you to generate images from text prompts and edit existing images using an interactive command-line menu.

---

## ✨ Features

- 🖼️ **Text-to-Image Generation**
  - Generate images from natural-language prompts.
  - Uses the `runwayml/stable-diffusion-v1-5` Stable Diffusion model.
  - Generates images at **512 × 512** resolution.

- ✏️ **Image-to-Image Editing**
  - Load an existing image.
  - Provide an editing prompt.
  - Generate a modified version of the image.

- 💻 **Local AI Processing**
  - Runs the Stable Diffusion model locally.
  - Does not require an external image-generation API.

- 🧠 **CPU-Compatible Configuration**
  - Uses `torch.float32` for compatibility with CPU-based systems.
  - An NVIDIA GPU is optional but can significantly improve generation speed.

- 📋 **Interactive Menu**
  - Simple command-line interface.
  - Choose between generating a new image or editing an existing image.

- ⚙️ **Automated Installation**
  - Includes an `install.py` script to help install the required Python packages.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **PyTorch**
- **Diffusers**
- **Stable Diffusion v1.5**
- **Hugging Face**
- **Pillow**
- **Transformers**

---

## 📋 Requirements

Before installing the project, make sure you have:

- Python **3.10 or newer**
- Windows 10/11, Linux, or macOS
- A reasonably capable CPU
- NVIDIA GPU — **optional**
- Internet connection for downloading the model and required packages
- Hugging Face account — **may be required depending on model access**

> ⚠️ Stable Diffusion models can require significant storage, RAM and/or VRAM. Generation on a CPU may take considerably longer than generation on a supported GPU.

---

# 🚀 Installation

## 1. Clone or download the project

Download the project and open a terminal inside the project folder.

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

## 3. Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## 4. Install the dependencies

The project includes an automated installation script:

```bash
python install.py
```

Alternatively, if the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 5. Hugging Face authentication

If authentication is required for the model, install the Hugging Face CLI and log in:

```bash
hf auth login
```

Follow the instructions and enter your Hugging Face access token when prompted.

---

# ▶️ Running the Application

Once installation is complete, run the application from the project directory.

## Windows

```bash
.venv\Scripts\python main.py
```

## macOS / Linux

```bash
.venv/bin/python main.py
```

The application will display an interactive menu.

---

# 🖼️ Using the Image Generator

After launching the application, select the relevant option from the menu.

## Option 1 — Text-to-Image

Choose:

```text
1
```

You will be asked to enter a text prompt.

For example:

```text
A futuristic city at sunset with flying cars
```

The Stable Diffusion model will process the prompt and generate an image.

Generated images are saved using filenames such as:

```text
base_image_1.png
base_image_2.png
base_image_3.png
```

---

# ✏️ Using Image-to-Image Editing

Choose:

```text
2
```

You can then provide an existing image and an editing prompt.

For example:

```text
Make the sky look dramatic and add more clouds
```

The application generates an edited version of the image.

Edited images are saved using filenames such as:

```text
edited_image_1.png
edited_image_2.png
edited_image_3.png
```

---

# 📁 Project Structure

A typical project structure is:

```text
Local-AI-Image-Generator/
│
├── main.py
├── install.py
├── README.md
├── requirements.txt
│
├── base_image_1.png
├── base_image_2.png
│
├── edited_image_1.png
├── edited_image_2.png
│
└── .venv/
```

The exact files may vary depending on the current version of the project.

---

# ⚡ Performance

Stable Diffusion is a relatively large AI model, so performance depends heavily on your hardware.

### CPU

The project is configured to support CPU-based generation using:

```python
torch.float32
```

However, image generation can take significantly longer on a CPU.

### NVIDIA GPU

If a compatible NVIDIA GPU is available, generation can be substantially faster.

The amount of available VRAM can also affect which configurations are practical.

---

# 🔄 How It Works

The basic workflow is:

```text
User
 │
 ▼
Interactive Menu
 │
 ├───────────────┐
 ▼               ▼
Text-to-Image   Image-to-Image
 │               │
 ▼               ▼
Prompt          Existing Image
 │               │
 └───────┬───────┘
         ▼
 Stable Diffusion
         │
         ▼
 Generated Image
         │
         ▼
      PNG File
```

---

# 🧠 Model

This project uses:

```text
runwayml/stable-diffusion-v1-5
```

Stable Diffusion is a generative AI model capable of producing images based on text prompts and performing image-to-image transformations.

The model is downloaded and used locally through the Hugging Face ecosystem.

---

# 🔧 Troubleshooting

## Python is not recognised

If you receive an error such as:

```text
'python' is not recognized...
```

make sure Python is installed and added to your system PATH.

Check your installation with:

```bash
python --version
```

## Hugging Face authentication error

If the model cannot be downloaded, try logging in again:

```bash
hf auth login
```

Make sure the account has the required access to the model.

## Generation is very slow

CPU-based Stable Diffusion generation can be slow.

If available, using a compatible NVIDIA GPU can significantly improve performance.

## Out-of-memory errors

If you encounter memory or VRAM errors, make sure other memory-intensive applications are closed.

Stable Diffusion can require substantial system resources.

---

# 🔐 Local Processing

The application is designed to run the image-generation process locally after the required model and dependencies have been downloaded.

Your prompts and images are therefore processed by the local application rather than being sent to a separate image-generation API.

---

# 📜 License

This project is released under the **MIT License**.

You are free to use, modify and distribute the project in accordance with the terms of the MIT License.

---

# 👨‍💻 Author

**Divij Mekala**

A Python project exploring **generative AI, Stable Diffusion and local AI applications**.

---

⭐ If you find the project useful, feel free to improve it, experiment with different prompts and extend its functionality!
