import tensorflow as tf
import sys
import os

class Red2048:
	def __init__(self):
		self.dicc_movimientos = {
			(0, 0, 0, 1): 0, #O: arriba
			(0, 0, 1, 0): 1, #1: derecha
			(0, 1, 0, 0): 2, #2: abajo
			(1, 0, 0, 0): 3, #3: izquierda
		}
		self.one_hot_vector_movimientos = [
			[0, 0, 0, 1], 	#ARRIBA
			[0, 0, 1, 0],	#DERECHA
			[0, 1, 0, 0],	#ABAJO
			[1, 0, 0, 0]	#IZQUIERDA
		]


	def entrenar(self, tablero, movimiento):
		print "*"*30
		print "ENTRENANDO"
		print "*"*30
		rutaCSV = os.getcwd() + '/entrenamiento/data_2048/'

		tf.reset_default_graph()
		
		#nuestro modelo
		x = tf.placeholder(tf.float32, [None, 16]) #entrada
		W = tf.Variable(tf.zeros([16, 4]), name='W') #pesos
		b = tf.Variable(tf.zeros([4]), name='b') #bias
		y = tf.nn.softmax(tf.matmul(x, W) + b) #salida 

		#para implementar el cross-entropy
		y_ = tf.placeholder(tf.float32, [None, 4]) #salida esperada
		#OJO: labels y logits pueden estar al reves
		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
		train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

		init_op = tf.global_variables_initializer()

		saver = tf.train.Saver(var_list={"W": W, "b": b})


		with tf.Session() as sess:
			sess.run(init_op)
			for i in range(1000):	
				sess.run(train_step, feed_dict={x:tablero, y_:movimiento})
				save_path = saver.save(sess, rutaCSV + 'model.ckpt')
		print "\nHa terminado el aprendizaje!"


	def predecir(self, tablero):
		rutaCSV = os.getcwd() + '/entrenamiento/data_2048/'

		#Modelo
		x = tf.placeholder(tf.float32, [None, 16]) #entrada
		W = tf.Variable(tf.zeros([16, 4]), name='W') #pesos
		b = tf.Variable(tf.zeros([4]), name='b') #bias
		y = tf.nn.softmax(tf.matmul(x, W) + b) #salida 

		init_op = tf.global_variables_initializer()

		saver = tf.train.Saver(var_list={"W": W, "b": b})

		'''
		with tf.Session() as sess:
			sess.run(init_op)
			saver.restore(sess, rutaCSV + 'model.ckpt')
			prediction = tf.argmax(y, 1)
			movimiento = (prediction.eval(feed_dict={x: tablero}, session=sess))
		return movimiento
		'''

		sess = tf.Session()
		sess.run(init_op)
		saver.restore(sess, rutaCSV + 'model.ckpt')
		prediction = tf.argmax(y, 1)
		movimiento = (prediction.eval(feed_dict={x: tablero}, session=sess))
		sess.close()
		return movimiento

		'''
		sess = tf.Session()
		correct_prediction = tf.argmax(y, 1)
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		sess.run(accuracy, feed_dict={x: tablero})
		return accuracy
		'''


	def metodo_a(self):
		pass	