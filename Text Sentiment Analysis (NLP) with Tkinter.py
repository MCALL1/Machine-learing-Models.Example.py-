# This script was writen with Spider 3.10 IDE
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 12:59:09 2023

@author: mcall
"""

import tkinter as tk
from textblob import TextBlob

def analyze_sentiment():
    text = text_entry.get("1.0", tk.END)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiment_label.config(text=f"Sentiment: {sentiment}")

# Create the GUI
window = tk.Tk()
window.title("Text Sentiment Analysis")
window.geometry("400x300")

text_entry = tk.Text(window, height=10, width=40)
text_entry.pack()

analyze_button = tk.Button(window, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

sentiment_label = tk.Label(window, text="Sentiment: ")
sentiment_label.pack()

window.mainloop()
