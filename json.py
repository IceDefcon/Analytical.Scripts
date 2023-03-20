import os
import json
import jsbeautifier
opts = jsbeautifier.default_options()
opts.indent_size = 4

os.system('cls') 
path = os.getcwd()

log = path + "file.in"
if not os.path.exists(log):
	print("\nMissing path: .../...")
	os.system('pause')
	exit()

file = open(log, "r")
data = json.load(file)
file.close()

file = open("file.out", "w")
file.write(jsbeautifier.beautify(json.dumps(data), opts))

