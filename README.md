# Book-project

**Book-project** is a Python-based application that utilizes Tesseract and Poppler for advanced text extraction and processing tasks. This README provides information on the prerequisites, installation steps, and configuration required to get started.

## Prerequisites

Before proceeding with the installation, ensure that you have the following prerequisites installed and configured:

1. **Python 3.9**  
   - Download from your private repository: [Python 3.9](https://cloud.w3datanet.com/index.php/s/L5cnEoW8NyHTem7)

2. **Anaconda**  
   - Download from your private repository: [Anaconda](https://cloud.w3datanet.com/index.php/s/LcdNiosAeJpTCZd)  

3. **Tesseract**  
   - Tesseract OCR must be installed on your system.  
     Download the appropriate version for your operating system:
     - [Tesseract Download](https://github.com/tesseract-ocr/tesseract)

4. **Poppler**  
   - Poppler is required for working with PDFs.  
     Install it via Conda (steps included below).

---

## Installation

### Step 1: Install Python 3.9
- Download and install Python 3.9 from the provided link.  
- Ensure you select the option to **Add Python to PATH** during installation.

### Step 2: Install Anaconda
- Download and install Anaconda from the provided link.  
- Follow the installation guide and set up Anaconda as your primary Python environment manager.

### Step 3: Clone the Project Repository
```bash
git clone https://github.com/riazsomc/book-project.git
cd book-project
```

### Step 4: Install Dependencies
- Install Poppler:
  ```bash
  conda install -c conda-forge poppler
  ```
- Install other dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Step 5: Configure Environment Variables (Windows)
- Add the following paths to your **System Environment Variables**:
  - Tesseract path:  
    `C:\Program Files\Tesseract-OCR`
  - Poppler path (e.g., if installed via Conda):  
    Find the location of your Conda environment (e.g., `C:\Users\<UserName>\Anaconda3\envs\myenv\Library\bin`) and add it to `PATH`.

### Step 6: Verify Installation
- Test Tesseract:
  ```bash
  tesseract --version
  ```
- Test Poppler (ensure `pdftotext` is accessible):
  ```bash
  pdftotext --version
  ```

---

## Contributing
Feel free to submit issues or pull requests to improve this project!

---

## License
This project is licensed under the [MIT License](LICENSE).

---

