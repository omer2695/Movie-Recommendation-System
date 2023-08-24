# Movie Recommendation System

This is a Movie Recommendation System implemented in Python using a machine-learning model. 
The system takes user input (movie preferences) and provides a list of recommended movies based on that input.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Introduction

This project is a simple movie recommendation system that demonstrates how to build a GUI application using Tkinter for Python. 
It utilizes a machine learning model (CountVectorizer) to provide movie recommendations based on user input. Users can enter their movie preferences, and the system will return a list of recommended movies.

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

- Python (>=3.6)
- Tkinter
- Pandas
- NumPy
- scikit-learn (sklearn)
- NLTK (Natural Language Toolkit)


You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```
Getting Started
1. Clone the repository to your local machine:

  git clone https://github.com/omer2695/movie-recommendation-system.git
  ```bash
  cd movie-recommendation-system
  ```

1. Install the project's dependencies as mentioned in the Prerequisites section.

2. Run the main script to launch the GUI:
    python main.py

## Usage

1. Launch the GUI application by running main.py.
2. Enter your movie preferences in the input field.
3. Click the "Recommend Movies" button.
4. The recommended movies will be displayed in the application window.

## Project Structure

- main.py: The main script that launches the GUI.
- model.py: Contains the machine learning model for movie recommendations.
- data.py: Handles data preprocessing and loading (if applicable).
- requirements.txt: List of project dependencies.
- README.md: This file.












