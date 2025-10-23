class TTTensorTest(tf.test.TestCase):
  def testCastFloat(self)
  def testCastIntFloat(self)
class TTMatrixTest(tf.test.TestCase):
  def testCastFloat(self)
  def testCastIntFloat(self)
class TTMatrixTestBatch(tf.test.TestCase):
  def testCastFloat(self):
    tt_mat = initializers.random_matrix_batch(((2, 3), (3, 2)), tt_rank=2, batch_size=3)
    with self.test_session() as sess:
      for dtype in [tf.float16, tf.float32, tf.float64]:
        casted = ops.cast(tt_mat, dtype)
        casted_val = sess.run(ops.full(casted))
        self.assertEqual(dtype, casted.dtype)
        self.assertTrue(dtype, casted_val.dtype)
  def testCastIntFloat(self):
    np.random.seed(1)
    K_1 = np.random.randint(0, high=100, size=(1, 2, 2, 2))
    K_2 = np.random.randint(0, high=100, size=(2, 3, 3, 2))
    K_3 = np.random.randint(0, high=100, size=(2, 2, 2, 1))
    tt_int = TensorTrain([K_1, K_2, K_3], tt_ranks=[1, 2, 2, 1])
    tt_int_batch = shapes.expand_batch_dim(tt_int)
    with self.test_session() as sess:
      for dtype in [tf.float16, tf.float32, tf.float64]:
        casted = ops.cast(tt_int_batch, dtype)
        casted_val = sess.run(ops.full(casted))
        self.assertEqual(dtype, casted.dtype)
        self.assertTrue(dtype, casted_val.dtype)
