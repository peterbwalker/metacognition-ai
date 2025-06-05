class MetacognitiveModel:
    def __init__(self, base_model, confidence_model):
        """
        :param base_model: callable -> input -> prediction
        :param confidence_model: callable -> input, prediction -> confidence
        """
        self.base_model = base_model
        self.confidence_model = confidence_model

    def predict_with_confidence(self, x):
        pred = self.base_model(x)
        conf = self.confidence_model(x, pred)
        return pred, conf
