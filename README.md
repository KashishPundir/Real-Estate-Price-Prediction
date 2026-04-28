# Real Estate Price Predictor for California

This project is an end-to-end machine learning application that predicts median house values in California districts, based on the California Housing dataset. The final product is an interactive web application built with Streamlit, where users can input housing features and receive a real-time price prediction.

## 🚀 Features

- **Interactive UI**: A user-friendly interface built with Streamlit, featuring sliders and number inputs for all features.
- **Real-Time Predictions**: Utilizes a pre-trained `RandomForestRegressor` model to deliver predictions instantly.
- **Data-Driven**: The model was trained and tuned on the classic California Housing dataset from `scikit-learn`.
- **Reproducible**: The entire pipeline, from data preprocessing to model training and deployment, is documented in the accompanying Jupyter Notebook.

## 🛠️ Tech Stack & Libraries

- **Language**: Python 3
- **Machine Learning**: Scikit-learn
- **Data Manipulation**: Pandas, NumPy
- **Web Framework**: Streamlit
- **Model Persistence**: Joblib

## ⚙️ Setup and Installation

To run this application locally, you'll need to set up a Python virtual environment and install the required packages.

**1. Clone the repository (or download the source code):**
```bash
git clone https://github.com/KashishPundir/Real-Estate-Price-Prediction.git
cd Real-Estate-Price-Prediction
```

**2. Create and activate a Python virtual environment: This keeps the project's dependencies isolated.**

#### For Windows
```
python -m venv venv
venv\Scripts\activate
```

**3. Install the required packages: Now, install all the necessary libraries from the requirements.txt file.**
```
pip install -r requirements.txt
```

**4. Generate model files using:**
```
jupyter notebook
```

## 🏃‍♂️**How to Run the Application:**
Once the setup is complete, you can launch the Streamlit web application with a single command.

Make sure you are in the root directory of the project and your virtual environment is activated. Then run:

```
streamlit run app.py
```

This will start a local web server and automatically open the application in your default web browser!

## 📂 **Project Structure:**
```
├── .gitignore                             # Hides files from GitHub
├── app.py                                 # The Python script for the Streamlit web application
├── Real Estate Price Prediction.ipynb     # Jupyter Notebook with the full ML workflow (analysis, training, etc.)
├── requirements.txt                       # List of Python dependencies for reproducibility
└── README.md               
```
## **🤝 Contributing:**

Contributions are welcome. If you’d like to improve the project:

- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request
  
## **📜 License:**

This project is for educational purposes. You may modify and use it with proper attribution.

