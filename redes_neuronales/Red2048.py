import tensorflow as tf
import numpy as np
import sys
import os

class Red2048:
	def __init__(self):
		self.dicc_movimientos = {
			(1, 0, 0, 0): 0, #0: arriba
			(0, 1, 0, 0): 1, #1: derecha
			(0, 0, 1, 0): 2, #2: abajo
			(0, 0, 0, 1): 3, #3: izquierda
		}


	def entrenar(self, tablero, movimiento):
		print "*"*30
		print "			ENTRENANDO"
		print "*"*30
		rutaCSV = os.getcwd() + '/entrenamiento/2048/'

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

		sess = tf.Session()
		sess.run(init_op)
		for i in range(2000):	
			sess.run(train_step, feed_dict={x:tablero, y_:movimiento})
			save_path = saver.save(sess, rutaCSV + 'model.ckpt')
		sess.close()		
		print "\n... Ha terminado el aprendizaje."


	def predecir(self, tablero):
		rutaCSV = os.getcwd() + '/entrenamiento/2048/'

		#Modelo
		x = tf.placeholder(tf.float32, [None, 16]) #entrada
		W = tf.Variable(tf.zeros([16, 4]), name='W') #pesos
		b = tf.Variable(tf.zeros([4]), name='b') #bias
		y = tf.nn.softmax(tf.matmul(x, W) + b) #salida 

		init_op = tf.global_variables_initializer()

		saver = tf.train.Saver(var_list={"W": W, "b": b})

		#FUNCIONA
		sess = tf.Session()
		sess.run(init_op)
		saver.restore(sess, rutaCSV + 'model.ckpt')
		prediction = tf.argmax(y, 1)
		movimiento = (prediction.eval(feed_dict={x: tablero}, session=sess))
		sess.close()
		return movimiento


	def todos_los_cvs(self, path_to_dir, suffix=".csv" ):
		archivos_csv = os.listdir(path_to_dir)
		return [ archivo for archivo in archivos_csv if archivo.endswith(suffix) ]


	def vectores_del_tablero(self, ruta):
		vctr_de_entrada = []
		vctr_del_tablero = []
		archivos_csv = self.todos_los_cvs(ruta)
		for archivos in archivos_csv:
			vctr_de_entrada = np.genfromtxt(ruta + archivos, delimiter=',', dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
			for entrada in vctr_de_entrada:
				vctr_del_tablero.append(entrada)
		return vctr_del_tablero


	def vectores_de_movimientos(self, ruta):
		vctr_de_salida = []
		vctr_de_movimientos = []
		archivos_csv = self.todos_los_cvs(ruta)
		for archivos in archivos_csv:
			vctr_de_salida = np.genfromtxt(ruta + archivos, delimiter=',', dtype=int, usecols=(16, 17, 18, 19))
			for salida in vctr_de_salida:
				vctr_de_movimientos.append(salida)
		return vctr_de_movimientos