# Laptop Price Predictor

A machine learning-based web application that estimates the price of a laptop based on its hardware and display specifications. The project uses a CatBoost regression model and a simple Streamlit interface so users can select laptop features and instantly get a predicted price.

## Overview

This project is designed to help users quickly estimate how much a laptop might cost based on key attributes such as:

- Brand and laptop type
- Screen size and display quality
- RAM and storage configuration
- CPU and GPU brand
- Operating system
- Weight and display features

The app is built for quick, interactive price estimation and is suitable for educational, demo, or prototype use.

## Features

- Interactive web UI built with Streamlit
- Real-time laptop price prediction
- Input fields for major laptop specifications
- CatBoost machine learning model for prediction
- User-friendly, lightweight dashboard
- Supports common laptop categories and brands

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- CatBoost
- Scikit-learn
- Matplotlib and Seaborn

## Project Structure

```text
laptop_price_predictor/
├── app.py                          # Streamlit application
├── catboost_laptop_model.pkl      # Trained CatBoost model
├── laptop_price_predictor.ipynb   # Notebook for exploration and training
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── venv/                          # Local virtual environment
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/laptop_price_predictor.git
cd laptop_price_predictor
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal in your browser.

## How It Works

The app collects user input for laptop specifications and passes them into the trained CatBoost model. The model predicts an estimated price and displays it in Indian Rupees (₹).

Example inputs:

- Company: Dell, HP, Apple, Lenovo, etc.
- Type: Notebook, Ultrabook, Gaming, Workstation
- Screen size: Inches
- RAM: 4GB, 8GB, 16GB, 32GB, 64GB
- Storage: HDD, SSD, Hybrid, Flash Storage
- CPU and GPU brand
- Operating system
- Display settings: Touchscreen and IPS

## Model Information

The prediction model is saved in `catboost_laptop_model.pkl` and is loaded by the app at runtime. The trained model uses structured laptop feature data to estimate market price.

## Example Output

```text
Estimated Laptop Price: ₹ 1,12,450.00
```

## Notes

- The app is optimized for demo and educational use.
- Model predictions are estimates and depend on the training dataset and feature values provided.
- The project includes a notebook for data exploration and model development.

## Future Improvements

- Add model accuracy evaluation and validation metrics
- Improve UI with visual charts and price ranges
- Support more laptop brands and feature options
- Add dataset preprocessing documentation
- Deploy the app to a cloud platform such as Streamlit Community Cloud

## License

This project is for learning and demonstration purposes. You can modify and extend it as needed for personal or educational use.
