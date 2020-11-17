import flask
from flask_cors import CORS
import transformers
import functools
import traceback

app = flask.Flask(__name__)
app.config['TESTING'] = True
cors = CORS(app)

MODEL_NAME = "allenai/unifiedqa-t5-small"
tokenizer = transformers.AutoTokenizer.from_pretrained(MODEL_NAME)
model = transformers.T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

def run_model(question, context, **generator_args):
    input_string = question.strip() + " \\n " + context.strip()
    input_ids = tokenizer.encode(input_string, return_tensors="pt").cuda()
    res = model.generate(input_ids, **generator_args)
    return [tokenizer.decode(x) for x in res]

@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    try:
        request = flask.request.get_json(force=True)
        context = request["context"]
        question = request["question"]
        answer = run_model(question, context)
        data["success"] = True
        data["answer"] = answer
    except Exception as e:
        error_string = e + " - " + str(traceback.format_exc())
        print("Error:", error_string)
        data["error"] = error_string
    return flask.jsonify(data)

if __name__ == "__main__":
    print("Starting Flask server")
    app.run(host="0.0.0.0", port=5000, )
