from flask import Flask, jsonify, request, make_response
import pandas as pd
import os

app = Flask(__name__)

@app.route('/datasets', methods=['GET'])
def get_dataset():
    dataset_name = request.args.get('name')+'.csv'

    if dataset_name in os.listdir('datasets'):
        path_dataset = './datasets/' + dataset_name
        df = pd.read_csv(path_dataset)
        dict_dataset = df.to_dict()
        return jsonify(dict_dataset)

    elif dataset_name == None:
        return jsonify({'message': 'Nenhum nome de dataset foi passado'})

    else:
        return jsonify({'message': 'Dataset nao encontrado'})

@app.route('/csv', methods=['GET'])
def get_csv():
    dataset_name = request.args.get('name')+'.csv'

    if dataset_name in os.listdir('datasets'):
        path_dataset = './datasets/' + dataset_name
        df = pd.read_csv(path_dataset)
        csv_string = df.to_csv(index=False)
        headers = {
            "Content-Type": "text/csv",
            "Content-Disposition": "attachment;filename=path_dataset"
        }
        response = make_response(csv_string, 200, headers)
        return response

    else:
        return jsonify({'message': 'Dataset nao encontrado'})

if __name__ == '__main__':
    app.run(debug=True)