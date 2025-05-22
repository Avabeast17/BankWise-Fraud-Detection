def retrain_model(model, new_data):
    model.fit(new_data)
    return model
