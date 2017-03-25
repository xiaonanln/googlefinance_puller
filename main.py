import sys
import os
sys.path[0:0] = [ os.path.join(os.path.dirname(sys.argv[0]), 'googlefinance')]
import time
import googlefinance as gf

INTERVAL = 5
SYMBOLS = ['QQQ', 'SPY']

lastQuotesCache = {
	s: {} for s in SYMBOLS
}

def main():
	try:
		mainloop()
	except KeyboardInterrupt:
		pass

def mainloop():
	while True:
		for symbol, quotes in zip(SYMBOLS, gf.getQuotes(SYMBOLS)):
			lastQuotes = lastQuotesCache[symbol]
			diffQuotes = {k: v for k, v in quotes.iteritems() if v != lastQuotes.get(k)}
			missingKeys = [k for k in lastQuotes.iterkeys() if k not in quotes]
			if missingKeys:
				diffQuotes['_ms'] = missingKeys

			if diffQuotes:
				print diffQuotes
			else:
				print >>sys.stderr, '%s: quotes not changed' % symbol

			lastQuotesCache[symbol] = quotes

		time.sleep(INTERVAL)

if __name__ == '__main__':
	main()

