import tensorflow as tf

print("Available GPU's")
gpus = tf.config.list_physical_devices("GPU")
print(gpus)
