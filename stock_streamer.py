import websocket
import json
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define a function to handle incoming WebSocket messages
def on_message(ws, message):
    global stock_data
    data = json.loads(message)
    stock_data.append(float(data['2. price']))
    plot_stock_data()

# Create a WebSocket connection to Alpha Vantage
def start_websocket():
    global ws
    ticker_symbol = ticker_entry.get().upper()
    ws = websocket.WebSocketApp(f"wss://streamer.alphavantage.co/v2/subscribe?symbol={ticker_symbol}&apikey=GETFNQ5SDYN8OV2N",
                                on_message=on_message)
    ws.run_forever()
    print("WebSocket connection started")

# Define a function to plot the live stock data
def plot_stock_data():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(stock_data, color='b')
    ax.set_title(f"Live {ticker_entry.get().upper()} Stock Data")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price ($)")
    plt.close(fig)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the GUI
root = tk.Tk()
root.title("Live Stock Data Streaming App")

# Create an editable field for the ticker symbol
ticker_frame = tk.Frame(root)
ticker_frame.pack()
tk.Label(ticker_frame, text="Ticker Symbol:").pack(side=tk.LEFT)
ticker_entry = tk.Entry(ticker_frame)
ticker_entry.pack(side=tk.LEFT)
ticker_entry.insert(0, "TICKER")

# Create a button to start the WebSocket connection
start_button = tk.Button(root, text="Start", command=start_websocket)
start_button.pack()

# Create a label to display the live stock data
stock_data = []
stock_data_label = tk.Label(root)
stock_data_label.pack()

# Start the GUI event loop
root.mainloop()
