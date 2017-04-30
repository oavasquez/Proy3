import tensorflow as tf
import os

class Red2048:
	def __init__(self):
		self.arg = 0


	def entrenar(self, tablero, movimiento):
		rutaCSV = os.getcwd() + '/entrenamiento/'

		tf.reset_default_graph()
		
		#nuestro modelo
		x = tf.placeholder(tf.float32, [None, 16]) #entrada
		W = tf.Variable(tf.zeros([16, 4]),name='W') #pesos
		b = tf.Variable(tf.zeros([4]),name='b') #bias
		y = tf.nn.softmax(tf.matmul(x, W) + b) #salida 

		#para implementar el cross-entropy
		y_ = tf.placeholder(tf.float32, [None, 4]) #salida esperada
		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))
		train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

		init_op = tf.global_variables_initializer()

		saver = tf.train.Saver(var_list={"W": W, "b": b})

		#bp=barraProgreso(1000, 0)
		#bp.start()

		with tf.Session() as sess:
		    sess.run(init_op)
		    for i in range(1000):
		    	#bp.setIndice(i)	
		    	sess.run(train_step, feed_dict={x:tablero, y_:movimiento})
		    	save_path = saver.save(sess, rutaCSV + 'model.ckpt')
		print "\nHa terminado el aprendizaje!"


	def predecir(self, tablero):
		rutaCSV = os.getcwd() + '/entrenamiento/'

		#Modelo
		x = tf.placeholder(tf.float32, shape=[None, 16])
		W = tf.Variable(tf.zeros([16, 4]))
		b = tf.Variable(tf.zeros([4]))
		y = tf.nn.softmax(tf.matmul(x, W) + b)

		init_op = tf.global_variables_initializer()

		saver = tf.train.Saver(var_list={"W": W, "b": b})

		with tf.Session() as sess:
			sess.run(init_op)
	        saver.restore(sess, rutaCSV + 'model.ckpt')
	        prediction = tf.argmax(y,1)
	        movimiento = (prediction.eval(feed_dict={x: tablero}, session=sess))
		return movimiento

	def function(self):
		pass