#Type code here
from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import BB
from surmount.logging import log

class TradingStrategy(Strategy):
    @property
    def assets(self):
        # Strategy applies to gcusd
        return ["AAPL","AMZN", "KO", "BA"]

    @property
    def interval(self):
        return "1hour"

    def run(self, data):
        holdings = data["holdings"]
        data = data["ohlcv"]

        return TargetAllocation({"AAPL": 0.25,"AMZN":0.25, "KO":0.25, "BA":0.25})