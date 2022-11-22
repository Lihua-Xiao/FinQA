import json
from collections import OrderedDict
with open('nbest_predictions.json') as f:
    nbest_predictions = json.load(f)
output = []
for key, list_of_pred in nbest_predictions.items():
    for pred in list_of_pred:
        item = OrderedDict()
        item['id'] = pred['id']
        item['predicted'] = pred['pred_prog']
        output.append(item)
with open('predictions_to_evaluate.json', "w") as writer:
    writer.write(json.dumps(output, indent=4)+ "\n")

