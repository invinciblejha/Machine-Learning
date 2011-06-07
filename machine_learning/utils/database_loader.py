

def load_database(string, separator = "\t"):
	try:
		f = open(string, "r")
		s = list(set([line for line in f]))
		f.close()
	except:
		s = []
	
	l_tmp = [v.strip().split(separator) for v in s]
	l_floats = [[float(e) for e in v[:-1]] + [v[-1]] for v in l_tmp]
	return l_floats

