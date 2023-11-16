import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedStyle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

def analyze_sentiment(text, result_label, pos_scale, neu_scale, neg_scale):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)

    result_label.config(text="Sentiment Analysis", font=("Arial", 16, "bold"))
    
    # Update progress scales
    pos_scale["value"] = sentiment_scores['pos'] * 100
    neu_scale["value"] = sentiment_scores['neu'] * 100
    neg_scale["value"] = sentiment_scores['neg'] * 100

def perform_sentiment_analysis():
    text = text_entry.get("1.0", tk.END).strip()
    analyze_sentiment(text, result_label, pos_scale, neu_scale, neg_scale)

# GUI Setup
root = tk.Tk()
root.title("Sentiment Analysis Tool")
root.geometry("400x350")

style = ThemedStyle(root)
style.set_theme("clam")  # You can choose a different theme if needed

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

text_label = ttk.Label(frame, text="Enter Text:", font=("Arial", 12))
text_entry = scrolledtext.ScrolledText(frame, height=5, width=40, wrap=tk.WORD, font=("Arial", 10))

result_label = ttk.Label(frame, text="", font=("Arial", 16, "bold"))

analyze_button = ttk.Button(frame, text="Analyze Sentiment", command=perform_sentiment_analysis)

# Progress scales
pos_scale = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=100, mode="determinate", style="TProgressbar")
neu_scale = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=100, mode="determinate", style="TProgressbar")
neg_scale = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=100, mode="determinate", style="TProgressbar")

# Styling
style.configure("TProgressbar", thickness=30, troughcolor="light gray", background="seagreen")

# Grid layout
text_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
text_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

analyze_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

result_label.grid(row=3, column=0, columnspan=2, pady=(0, 10))

# Labels for progress scales
ttk.Label(frame, text="Positive:", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
ttk.Label(frame, text="Neutral:", font=("Arial", 12)).grid(row=5, column=0, sticky=tk.W, pady=(0, 5))
ttk.Label(frame, text="Negative:", font=("Arial", 12)).grid(row=6, column=0, sticky=tk.W, pady=(0, 5))

# Progress scales layout
pos_scale.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
neu_scale.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
neg_scale.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=(0, 5))

# Run the GUI
root.mainloop()
