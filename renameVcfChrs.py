
# This script assumes that the input map file is a tab-separated file
# with no header and two columns. Column one contains the original 
# sequence IDs. Column two contains the new sequence ID. To speed up
# the process, assumptions about the original sequence IDs is baked-in
# to this script (namely, they match this regex: scaffold_[0-9]+.
# It also assumes that the input VCF file contains these names in
# some header lines and as the entire content of the first column
# for any data line. This code has not been optimized in any meaningful
# way, and it will run slowly as the number of header lines increases and
# the number of sequence names in the map file increases.

import sys
import re

def parseMapFile(fn):
	names = {}
	with open(fn, 'r') as ifd:
		for line in ifd:
			fields = line.rstrip('\n').split('\t')
			names[fields[0]] = fields[1]
	return names

if __name__ == "__main__":
	
	map_fn = sys.argv[1]
	vcf_fn = sys.argv[2]

	name_map = parseMapFile(map_fn)
	names_list = sorted(list(name_map.keys()))
	print("INFO: loaded names map from map file", file=sys.stderr)
	
	with open(vcf_fn, 'r') as ifd:
		i = 1
		line = ifd.readline()
		while line != '' and line[0] == '#':
			print(f"\rINFO: processing header #{i}...", end='', file=sys.stderr, flush=True)
			if not re.search(r"scaffold_", line) is None:
				out = str(line)
				for name in names_list:
					out = re.sub(r'\b' + name + r'\b', name_map[name], out)
					if out != line:
						break
				print(out, end='', file=sys.stdout)
			else:
				print(line, end='', file=sys.stdout)
			line = ifd.readline()
			i += 1

		print("\rINFO: finished header lines        ", file=sys.stderr, flush=True)

		while line != '':
			fields = line.rstrip('\n').split('\t')
			name = fields[0]
			fields[0] = name_map[name]
			print('\t'.join(fields), file=sys.stdout)
			print(f"\rINFO: processing {name}...   ", end='', file=sys.stderr, flush=True)
			line = ifd.readline()

		print("\rINFO: finished data lines                  ", file=sys.stderr, flush=True)

