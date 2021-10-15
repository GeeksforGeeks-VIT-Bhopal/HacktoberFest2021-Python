import pandas as pd
import numpy as np
import random


import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime
from matplotlib.lines import Line2D
import matplotlib.lines as mlines



def stop_loss(df, trades, price_drop_limit = .99):

	additional_trades = []

	x = []
	stop_loss = []
	curr_stop_loss = df.iloc[0]['Close']

	stoped = 1

	trade_times = []
	trade_types = []
	for tim, typ in trades:
		trade_times.append(tim)
		trade_types.append(typ)
	# form price drop limit line
	for index, row in df.iterrows():


		x.append(row['Date'])
		stop_loss.append(curr_stop_loss)

		# if there are no trades
		if len(trade_times) == 0:
			continue

		trade_type = trade_types[0]

		if row['Date'] >= trade_times[0]:
			# if we sold our stocks already we can't sell it again
			curr_stop_loss = row['Close'] * price_drop_limit
			if trade_type == 1:
				stoped = 0
			trade_times.pop(0)
			trade_types.pop(0)


		# plot when to stop loss
		if stoped == 0 and curr_stop_loss >= row['Close']:
			plt.plot(row['Date'], row['Close'], 'xy')
			stoped = 1
			additional_trades.append((row['Date'], -1))

	plt.plot(x, stop_loss, '-.')
	# additional trades
	return additional_trades

def plot_profits(df, trades, start_money=1000., commision=.01):

	trade_times = []
	trade_types = []
	for tim, typ in trades:
		trade_times.append(tim)
		trade_types.append(typ)

	bought = 0
	current_money = start_money
	current_stocks = 0

	x = []
	profits = []

	for index, row in df.iterrows():

		close = row['Close']

		profits.append( current_money + current_stocks * close - start_money)
		x.append(row['Date'])

		if len(trade_types) == 0:
			continue

		# if we traded
		if row['Date'] >= trade_times[0]:
			trade_type = trade_types[0]
			trade_types.pop(0)
			trade_times.pop(0)
			# if we buy stocks
			if trade_type == 1:
				current_stocks = current_stocks + (current_money / close) * (1-commision)
				current_money = 0

			# if we sell stocks
			if trade_type == -1:
				current_money = current_money + current_stocks * close * (1-commision)
				current_stocks = 0

	# plot second plot of profits
	plt.figure()
	ax = plt.subplot()
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
	plt.plot(x, profits, 'g')

	return profits[-1]



class AlligatorIndicator():

	def __init__(self, df, jaw_length=13, jaw_displace=-8, teeth_length=8, teeth_displace=-5, lips_length=5, lips_displace=-3):
		self.data = df.copy()
		self.data = self.data[['Date', 'Close']]
		self.jaw_length = jaw_length
		self.jaw_displace = jaw_displace
		self.teeth_length= teeth_length
		self.teeth_displace = teeth_displace
		self.lips_length = lips_length
		self.lips_displace = lips_displace

	# displace - shift graph forward (into future)
	def __smoothed_average(self, length, displace):
		# we'll get data - length entries

		smma = [np.sum(self.data['Close'].iloc[:length])/length]

		x = self.data['Date'].iloc[:-length] - displace

		for i in range(1, self.data.shape[0]-length):

			prevsum = smma[i-1] * length
			new_smma = (prevsum-smma[i-1]+self.data['Close'].iloc[i])/length
			smma.append(new_smma)

		return (x, smma)
		

	def __get_jaw(self):
		return self.__smoothed_average(length=self.jaw_length, displace=self.jaw_displace)

	def __get_teeth(self):
		return self.__smoothed_average(length=self.teeth_length, displace=self.teeth_displace)

	def __get_lips(self):
		return self.__smoothed_average(length=self.lips_length, displace=self.lips_displace)

	def plot_indicator(self):
		jaw = self.__get_jaw()
		teeth = self.__get_teeth()
		lips = self.__get_lips()

		plt.plot(jaw[0], jaw[1], 'cyan', lw=0.5)
		plt.plot(teeth[0], teeth[1], 'red', lw=0.5)
		plt.plot(lips[0], lips[1], 'yellow', lw=0.5)


	# Buy signal : YELLOW > RED > CYAN
	# Sell signal : YELLOW < RED < CYAN
	# Ploting signals relative to jaw position, not in sync with real data
	def __get_signals(self):
		jaw = self.__get_jaw()
		teeth = self.__get_teeth()
		lips = self.__get_lips()


		# lips start earliest, then teeth, take that into account
		jaw_offset = 0
		teeth_offset = (-self.jaw_displace) - (-self.teeth_displace)
		lips_offset = (-self.jaw_displace) - (-self.lips_displace)
		x = jaw[0].reset_index(drop=True)

		signals = []

		# we'll form array which indicates if Sell, No or Buy signal is satisfied (-1, 0, 1)

		for i in range(len(jaw[0])):

			# buy signal
			if jaw[1][i+jaw_offset] < teeth[1][i+teeth_offset] and teeth[1][i+teeth_offset] < lips[1][i+lips_offset]:
				signals.append(1)
				#plt.plot(x[i], jaw[1][i], 'og')
			# sell signal
			elif jaw[1][i+jaw_offset] > teeth[1][i+teeth_offset] and teeth[1][i+teeth_offset] > lips[1][i+lips_offset]:
				signals.append(-1)
				#plt.plot(x[i], jaw[1][i], 'or')
			else:
				signals.append(0)
				#plt.plot(x[i], jaw[1][i], 'ow')

		return x, signals

	def plot_signals(self):
		times, signals = self.__get_signals()
		bought = 0
		sold = 1

		# pair of numbers indicating time and if it was buying or selling trade
		trades = []

		for t, signal in zip(times, signals):

			if signal == 1 and bought == 0:
				trades.append((t, 1))
				bought = 1
				sold = 0
				plt.axvline(t, color='lime', linestyle='--', lw=.4)

			elif signal == -1 and sold == 0:
				trades.append((t, -1))
				sold = 1
				bought = 0
				plt.axvline(t, color='orange', linestyle='--', lw=.4, label='{:5.0f}')

		# fixing displace
		return trades

	def plot_legend(self):
		colors = ['lime', 'orange', 'blue']
		lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='--') for c in colors]
		sell_stop_loss = mlines.Line2D([], [], color='yellow', marker='x',
                          markersize=15, label='sell stop loss')
		lines.append(sell_stop_loss)
		labels = ['buy signal', 'sell signal', 'stop loss', 'sell stop loss']
		plt.legend(lines, labels)
		
def plot_candles(df):

	ax = plt.subplot()
	ax.set_facecolor('black')

	df = df[['Date', 'Open', 'High', 'Low', 'Close']]

	ls, rs = candlestick_ohlc(ax, df.values, colorup='green', width=.5)
	for r in rs:
		r.set_edgecolor('w')
		r.set_linewidth(.4)
		

	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))




# N samples ,7 features


# The Alligator indicator consists of three smoothed moving averages. When the lines are inter-twinned the 'alligator' is at rest and out of the market. When the lines are separated in an up or down direction the 'alligator' is hungry to buy on the up trend and to sell on the down trend.

if __name__ == "__main__":

	df = pd.read_csv('tsla.csv') # tsla, aapl
	df['Date'] = pd.to_datetime(df['Date'])
	df["Date"] = df["Date"].apply(mdates.date2num)
	df = df.iloc[-150:]

	plot_candles(df.iloc[:-4])
	#alligator = AlligatorIndicator(df, jaw_length=21, jaw_displace=-13, teeth_length=13, teeth_displace=-8, lips_length=8, lips_displace=-5)

	
	#optimizing parameter
	"""
	best_para = []
	best_profit = []

	cur_para = [13,-8,8,-5,5,-3]

	for i in range(100):
		# 3 positive and 3 negative, increasing numbers:

		alligator = AlligatorIndicator(df, jaw_length=cur_para[-1], jaw_displace=cur_para[0], teeth_length=cur_para[-2], teeth_displace=cur_para[1], lips_length=cur_para[-3], lips_displace=cur_para[2])

		trades = alligator.plot_signals()

		additional_trades = stop_loss(df, list(trades))

		for x in additional_trades:
			trades.append(x)
		trades.sort()

		profit = plot_profits(df, list(trades))

		if profit > best_profit:
			best_profit = profit
			best_para = new_para

		cur_para[::2] += 1
		cur_para[1::2] -= 1
	
	print(best_para)
	"""

	alligator = AlligatorIndicator(df, jaw_length=13, jaw_displace=-8, teeth_length=8, teeth_displace=-5, lips_length=5, lips_displace=-3)
	alligator.plot_indicator()
	alligator.plot_legend()

	trades = alligator.plot_signals()

	additional_trades = stop_loss(df, list(trades))

	### add in additional trades if needed ###
	for x in additional_trades:
		trades.append(x)
	trades.sort()
	###

	#profits = plot_profits(df, list(trades), start_money=1000., commision=.5)

	plt.show()