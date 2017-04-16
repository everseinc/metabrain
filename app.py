from flask import Flask, request, jsonify
import tensorflow as tf
from brain.analyze import Analyze
import json

app = Flask(__name__)
analyze = Analyze()


@app.route("/", methods = ['GET', 'POST'])
def index():

	api_input = json.loads(request.json)
	app.logger.debug(api_input)
	if (api_input is None or "records" not in api_input):
		return jsonify(error = "Need json includes image property which is 784(28 * 28) length, float([0, 1.0]) array")
	else:
		result = analyze.emotion(api_input["records"])
		return jsonify(emotions = result)

if __name__ == "__main__":
	app.debug = True
	app.run(port = 3000, host = '0.0.0.0')