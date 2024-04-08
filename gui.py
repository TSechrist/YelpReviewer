import tkinter as tk
from WeightedVector import WeightedVector

class MainApplication(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self)

        # window = tk.Tk()
        # window.title("Yelp Sentiment Analyzer")
        w = WeightedVector()
        w.loadVector()

        frame_greeting = tk.Frame(master=window)
        frame_error = tk.Frame(master=window)
        frame_text = tk.Frame(master=window)
        frame_button = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
        frame_result = tk.Frame(master=window)

        label_greeting = tk.Label(master=frame_greeting, text="Enter a review: (minimum 10 words)")
        label_greeting.pack()
        frame_greeting.grid(row=0, column=0, padx=5, pady=5)
        
        label_error = tk.Label(master=frame_greeting, text="")
        label_error.pack()
        frame_error.grid(row=1, column=0, padx=5, pady=5)

        text_box = tk.Text(master=frame_text)
        text_box.pack()
        frame_text.grid(row=2, column=0, padx=5, pady=5)

        button = tk.Button(
            master=frame_button,
            text="Click here to predict the star rating",
            # width=25,
            # height=5,
            bg="CadetBlue1",
            # command=handle_click
        )

        button_restart = tk.Button(
            master=frame_button,
            text="Start over",
            bg="CadetBlue1",
            # command=handle_click_restart
        )
        button.grid(row=0, column=0, padx=5, pady=5)
        button_restart.grid(row=0, column=1, padx=5)
        frame_button.grid(row=3, column=0, padx=5, pady=5)

        prediction = 4
        label_result = tk.Label(master=frame_result)
        label_result.pack()
        frame_result.grid(row=4, column=0, padx=5, pady=5)

        def handle_click(event):
            review = text_box.get(1.0, tk.END)
            if len(review.split(" ")) < 10:
                label_error["text"] = "Please enter a review with 10 or more words"
            else:
                label_error["text"] = ""
                # call eval here and store result to prediction
                prediction = w.predict_dec(review)
                label_result["text"] = f"Predicted rating is {prediction} stars."
            # print(review)

        def handle_click_restart(event):
            text_box.delete(1.0, tk.END)
            label_result["text"] = ""

        button.bind("<Button-1>", handle_click)
        button_restart.bind("<Button-1>", handle_click_restart)

        # window.mainloop()