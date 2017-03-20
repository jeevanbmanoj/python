stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
def get_max_profit(stock):
	maxProfit =0
	minimum = stock[0]
	for item in stock[1:]:
		if item < minimum:
			minimum = item
		if item - minimum > maxProfit:
			maxProfit = item - minimum
	return maxProfit
print (get_max_profit(stock_prices_yesterday))
