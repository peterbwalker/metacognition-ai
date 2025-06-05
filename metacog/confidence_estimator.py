class SimpleConfidenceEstimator:
    def __call__(self, x, prediction):
        """
        Example: estimate confidence as a function of input variance
        """
        return 1.0 - float(abs(prediction) % 1)  # placeholder confidence
