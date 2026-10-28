import json
from genlayer import *

class PriceOracleContract:
    def __init__(self):
        self.latest_price = 0
        self.status = "UNVERIFIED"

    @external
    def fetch_and_verify_price(self, api_url: str) -> str:
        # Fetching price from external source via GenLayer consensus
        response = net.get(api_url)
        data = json.loads(response.text)
        
        # Validating price consensus
        price = data.get("price", 0)
        
        if price > 0:
            self.latest_price = price
            self.status = "APPROVED"
        else:
            self.status = "DENIED"
            
        return self.status