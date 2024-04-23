python client/entrypoint init_seed
python client/entrypoint train --in_model_path=seed.npz --out_model_path=trained_model.npz --data_path=iris_data/iris.json
python client/entrypoint validate --in_model_path=trained_model.npz --out_json_path=metrics.json --data_path=iris_data/iris.json