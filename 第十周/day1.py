import numpy as np

returns = np.array([
    [0.01, -0.02, 0.03],
    [0.02, 0.01, -0.01],
    [-0.01, 0.03, 0.02],
    [0.03, -0.01, 0.01],
    [0.00, 0.02, 0.04]
])
weights = np.array([0.4, 0.35, 0.25])

mean_returns = np.mean(returns, 0)
demeaned = returns - mean_returns
portfolio_returns = (returns * weights).sum(axis=1)
mean_portfolio = np.sum(returns * weights) 

print(portfolio_returns)