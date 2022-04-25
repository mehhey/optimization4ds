f = lambda x: x[0]**2 + x[1]**2 + x[2]**2
f_prime = grad(f)
x_0 = np.array([2,2,2], dtype=np.float32)
alpha = .1
x_opt = x_0
num_iter = 100
for i in range(num_iter):
    x_opt = x_opt - alpha * f_prime(x_opt)
print( f"Optimal point: {x_opt}, Objective function value:{f(x_opt)}")