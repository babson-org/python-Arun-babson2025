

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    sym = sym.upper()

    # Validate ticker symbol
    if sym not in _prices.DOW30:
        print("Invalid ticker symbol.")
        return

    # Validate share quantity
    if shares <= 0:
        print("Number of shares must be greater than zero.")
        return

    # Get last close price
    last_close_map = _prices.get_last_close_map([sym])
    stock_price = last_close_map.get(sym)
    if stock_price is None:
        print("Price data unavailable for symbol.")
        return

    total_cost = stock_price * shares

    # Check for sufficient cash
    if total_cost > self.cash:
        print("Insufficient funds.")
        return

    # Find existing position (ensure only one per symbol)
    pos = _find_position(self, sym)

    if pos is None:
        # Create new position as a dictionary
        pos = {
            "sym": sym,
            # name is optional for core logic; using symbol as fallback
            "name": sym,
            "shares": 0.0,
            "cost": 0.0,
        }
        self.positions.append(pos)

    # Update position
    pos["shares"] += shares
    pos["cost"] += total_cost

    # Deduct cash
    self.cash -= total_cost

    # No success print here; UI handled in main.py
    return
    
    
    return



