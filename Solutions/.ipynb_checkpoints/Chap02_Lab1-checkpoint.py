def sample(num):
    x = np.random.randn(num)
    y = 2 * x + 1 + np.random.randn(num)
    return x,y

trn_x, trn_y = sample(100)

def mse(beta):
    errs = trn_y - (beta[0] + beta[1] * trn_x)
    return np.dot(errs,errs)

mse_prime = grad(mse)

beta_0 = np.random.randn(2)
alpha = .001
beta_opt = beta_0
num_iter = 400
for i in range(num_iter):
    beta_opt = beta_opt - alpha * mse_prime(beta_opt)
print( f"Optimal point: {beta_opt}, Objective function value:{mse(beta_opt)}")

# plotting
fig, ax = plt.subplots()
ax.plot(trn_x, trn_y, '.')
t = np.linspace(trn_x.min(), trn_x.max(), 100)
ax.plot(t, beta_opt[0] + beta_opt[1] * t)
