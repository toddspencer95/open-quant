import sys
import datetime as dt
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class StockPlotter(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Stock Plotter')
        self.setGeometry(100, 100, 800, 600)

        # Create the stock symbol label and input box
        self.symbol_label = QLabel('Enter a stock symbol:', self)
        self.symbol_label.move(50, 50)
        self.symbol_input = QLineEdit(self)
        self.symbol_input.move(200, 50)
        self.symbol_input.resize(100, 30)

        # Create the plot button
        self.plot_button = QPushButton('Plot', self)
        self.plot_button.move(350, 50)
        self.plot_button.clicked.connect(self.plot_stock)

        # Create the matplotlib canvas to display the plot
        self.canvas = plt.figure(figsize=(8, 6)).canvas
        self.canvas.setParent(self)
        self.canvas.move(50, 100)

    def plot_stock(self):
        # Get the stock symbol from the input box
        symbol = self.symbol_input.text()

        # Download the historical price data from Yahoo Finance
        start_date = dt.datetime.now() - dt.timedelta(days=365)
        end_date = dt.datetime.now()
        data = yf.download(symbol, start=start_date, end=end_date)

        # Plot the price data using Matplotlib
        ax = self.canvas.figure.subplots()
        ax.plot(data['Close'])
        ax.set_title(f'{symbol} Price History')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        self.canvas.draw()


if __name__ == '__main__':
    # Create the application and show the main window
    app = QApplication(sys.argv)
    window = StockPlotter()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
