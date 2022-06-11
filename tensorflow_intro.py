import tensorflow as tf

x1 = tf.constant(5)
x1 = tf.constant(6)

result = tf.mul(x1,x2)
print(result)


sess = tf.session()

print(sess.run(result))