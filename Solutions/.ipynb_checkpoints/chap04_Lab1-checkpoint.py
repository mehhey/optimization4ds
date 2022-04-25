# Training Data Prep
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

a = tf.constant(-1.)
b = tf.constant(2.)
c = tf.constant(3.)
noise_std = tf.constant(0.04)
x = tf.random.uniform(shape=(1,100))
y = a * x ** 2 + b * x + c + noise_std * tf.random.normal(shape=(1,100))

a_hat = tf.Variable(1.)
b_hat = tf.Variable(1.)
c_hat = tf.Variable(1.)
opt = tf.keras.optimizers.SGD(learning_rate=0.006, momentum=0.1, nesterov=True)
for i in range(1100):
    loss = lambda: tf.reduce_sum(((a_hat * x**2 + b_hat * x + c_hat)-y)**2)
    
    step_count = opt.minimize(loss, [a_hat, b_hat, c_hat]).numpy()
    
print(a_hat.numpy(), b_hat.numpy(), c_hat.numpy())