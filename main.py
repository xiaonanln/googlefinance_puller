import sys
import os
sys.path[0:0] = [ os.path.join(os.path.dirname(sys.argv[0]), 'googlefinance')]
import time
import googlefinance as gf

INTERVAL = 59
SYMBOLS = ['SPY', 'QQQ']

def main():
	try:
		mainloop()
	except KeyboardInterrupt:
		pass

def mainloop():
	while True:
		for quotes in gf.getQuotes(SYMBOLS):
			print quotes
		time.sleep(INTERVAL)

if __name__ == '__main__':
	main()

