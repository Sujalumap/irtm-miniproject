import tkinter as tk
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment():
    review = text_input.get("1.0", tk.END)
    
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        result = "Positive 😊"
    elif polarity < 0:
        result = "Negative 😡"
    else:
        result = "Neutral 😐"
    
    result_label.config(text="Sentiment: " + result)

# Create main window
root = tk.Tk()
root.title("Product Sentiment Analyzer")
root.geometry("400x300")

# Title Label
title = tk.Label(root, text="🛒 Sentiment Analyzer", font=("Arial", 16))
title.pack(pady=10)

# Input Box
text_input = tk.Text(root, height=5, width=40)
text_input.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Sentiment: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run application
root.mainloop()