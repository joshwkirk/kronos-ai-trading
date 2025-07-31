# strategies.py
def get_strategy(name):
    def strategy(data):
        return "hold"
    return strategy
