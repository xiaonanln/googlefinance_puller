from __future__ import absolute_import
import ./googlefinance as gf

symbols = ['SPY', 'QQQ']


def main():
	try:
		mainloop()
	except KeyboardInterrupt:
		pass

def mainloop():
	while True:
		for quotes in gf.getQuotes(symbols):

			print quotes

if __name__ == '__main__':
	main()

