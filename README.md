# University Shortlisting and Prediction System

This repository contains a project focused on shortlisting universities for prospective students based on their profiles and predicting the likelihood of admission. The project leverages machine learning techniques to provide recommendations and predictions.

## Table of Contents

- [University Shortlisting and Prediction System](#university-shortlisting-and-prediction-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Files](#files)
  - [Model Training](#model-training)


## Introduction

This project aims to assist students in shortlisting universities based on their profiles and predicting the chances of admission. It uses a trained machine learning model to make predictions based on input features such as GRE scores, TOEFL scores, university rating, and more.

## Features

- **Profile-Based University Shortlisting**: Recommends universities based on student profiles.
- **Admission Prediction**: Predicts the likelihood of admission to a specific university.
- **Interactive Notebook**: Provides a Jupyter Notebook for interactive data analysis and model training.

## Requirements

- Python 3.x
- Pandas
- Scikit-Learn
- Jupyter Notebook

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/university-shortlisting.git
    cd university-shortlisting
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Jupyter Notebook:

    ```bash
    jupyter notebook Shortlisting_universities.ipynb
    ```

2. Execute the cells in the notebook to load data, analyze it, and make predictions.

3. To use the prediction script directly, run:

    ```bash
    streamlit run app.py
    ```

## Files

- `app.py`: Main script for making predictions based on input data.
- `dataset.csv`: Dataset used for training and testing the model.
- `mlr.pkl`: Pre-trained machine learning model.
- `Shortlisting_universities.ipynb`: Jupyter Notebook for data analysis and model training.

## Model Training

The model is trained using the dataset provided in `dataset.csv`. The training process involves:

1. Loading and preprocessing the data.
2. Splitting the data into training and testing sets.
3. Training a machine learning model (Multiple Linear Regression) on the training data.
4. Evaluating the model on the testing data.
5. Saving the trained model as `mlr.pkl`.

To retrain the model, modify and run the relevant cells in the `Shortlisting_universities.ipynb` notebook.
