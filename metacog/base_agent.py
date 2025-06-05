class DummyAgent:
    def __call__(self, x):
        """
        A trivial 'model' that returns the sum of inputs
        """
        return sum(x)
