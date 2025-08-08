# 1. Base image with Python
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies (including tesseract-ocr)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    poppler-utils \
    && apt-get clean

# 4. Copy app files
COPY . .

# 5. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Expose Streamlit port
EXPOSE 8501

# 7. Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
