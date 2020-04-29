import os
import json

output = {}
unclean_output = {}

output['adminPasswordOrKey'] = os.getenv('adminPasswordOrKey')

with open("uncleanOutput.json") as input_file:
	unclean_output = json.load(input_file)

for item in unclean_output:
	output[item] = unclean_output[item]["value"]

with open("output.json", "w") as output_file:
	json.dump(output, output_file, sort_keys=True, indent=4)
