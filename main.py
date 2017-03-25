import sys
import os
sys.path[0:0] = [ os.path.join(os.path.dirname(sys.argv[0]), 'googlefinance') ]
print sys.path
import googlefinance as gf

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

