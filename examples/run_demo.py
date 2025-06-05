from metacog.base_agent import DummyAgent
from metacog.confidence_estimator import SimpleConfidenceEstimator
from metacog.metacognitive_model import MetacognitiveModel

if __name__ == "__main__":
    base = DummyAgent()
    conf = SimpleConfidenceEstimator()
    meta = MetacognitiveModel(base, conf)

    x = [1, 2, 3]
    pred, confidence = meta.predict_with_confidence(x)

    print(f"Input: {x}")
    print(f"Prediction: {pred}, Confidence: {confidence:.2f}")
