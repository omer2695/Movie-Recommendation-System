import tkinter as tk
from tkinter import ttk
from model import ML_model

# Create a function to handle the recommendation
def recommend_GUI():
    # Get user input from the Entry widget
    movie = entry.get()

    # Call your machine learning model to get movie recommendations
    recommendations = ML_model(movie)

    # Clear any previous recommendations from the Text widget
    recommendations_text.delete(1.0, tk.END)

    # Display recommendations in the Text widget
    for recommendation in recommendations:
        recommendations_text.insert(tk.END, recommendation + '\n')

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Create a label
label = tk.Label(root, text="Enter your preferences:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to trigger the recommendation
recommend_button = tk.Button(root, text="Recommend Movies", command=recommend_GUI)
recommend_button.pack()

# Create a Text widget to display recommendations
recommendations_text = tk.Text(root, width=40, height=10)
recommendations_text.pack(pady=10)

# Run the GUI
root.mainloop()
