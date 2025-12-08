
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    
    sym = sym.upper()

    # Find existing position
    pos = _find_position(self, sym)
    if pos is None:
        print("Symbol not found in portfolio.")
        return

    # Validate shares
    if shares <= 0:
        print("Number of shares must be greater than zero.")
        return

    owned_shares = pos.get("shares", 0.0)
    if shares > owned_shares:
        print("Cannot sell more shares than owned.")
        return

    # Proceeds from sale (use passed-in price)
    proceeds = price * shares

    # Average cost per share
    if owned_shares > 0:
        avg_cost = pos["cost"] / owned_shares
    else:
        avg_cost = 0.0

    # Cost reduction based on average cost accounting
    cost_reduction = avg_cost * shares

    # Update position
    pos["shares"] = owned_shares - shares
    pos["cost"] -= cost_reduction

    # Remove position if shares go to zero (handle float noise)
    if pos["shares"] <= 0:
        self.positions.remove(pos)

    # Add cash to portfolio
    self.cash += proceeds

    return
       
