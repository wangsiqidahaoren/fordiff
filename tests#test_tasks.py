from __future__ import print_function
import numpy as np
import pytest

from keras.utils.test_utils import get_test_data
from keras.models import Sequential
from keras.layers.core import Dense, Activation, TimeDistributedDense, Flatten
from keras.layers.recurrent import GRU
from keras.layers.convolutional import Convolution2D
from keras.utils.np_utils import to_categorical


def test_vector_classification():
    np.random.seed(1337)
    nb_hidden = 10

    print('vector classification data:')
    (X_train, y_train), (X_test, y_test) = get_test_data(nb_train=1000,
                                                         nb_test=200,
                                                         input_shape=(10,),
                                                         classification=True,
                                                         nb_class=2)
    print('X_train:', X_train.shape)
    print('X_test:', X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:', y_test.shape)

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model = Sequential([
        Dense(nb_hidden, input_shape=(X_train.shape[-1],), activation='relu'),
        Dense(y_train.shape[-1], activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    history = model.fit(X_train, y_train, nb_epoch=15, batch_size=16,
                        validation_data=(X_test, y_test),
                        show_accuracy=True, verbose=0)
    assert(history.history['val_acc'][-1] > 0.8)


def test_vector_reg():
    np.random.seed(1337)
    nb_hidden = 10
    print('vector regression data:')
    (X_train, y_train), (X_test, y_test) = get_test_data(nb_train=1000,
                                                         nb_test=200,
                                                         input_shape=(10,),
                                                         output_shape=(2,),
                                                         classification=False)
    print('X_train:', X_train.shape)
    print('X_test:', X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:', y_test.shape)

    model = Sequential()
    model.add(Dense(nb_hidden, input_shape=(X_train.shape[-1],)))
    model.add(Activation('tanh'))
    model.add(Dense(y_train.shape[-1]))
    model.compile(loss='hinge', optimizer='adagrad')
    history = model.fit(X_train, y_train, nb_epoch=12, batch_size=16,
                        validation_data=(X_test, y_test), verbose=0)
    assert (history.history['val_loss'][-1] < 0.9)


def test_temporal_clf():
    np.random.seed(1337)
    print('temporal classification data:')
    (X_train, y_train), (X_test, y_test) = get_test_data(nb_train=1000,
                                                         nb_test=200,
                                                         input_shape=(3, 5),
                                                         classification=True,
                                                         nb_class=2)
    print('X_train:', X_train.shape)
    print('X_test:', X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:', y_test.shape)

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model = Sequential()
    model.add(GRU(y_train.shape[-1], input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adadelta')
    history = model.fit(X_train, y_train, nb_epoch=12, batch_size=16,
                        validation_data=(X_test, y_test),
                        show_accuracy=True, verbose=0)
    assert(history.history['val_acc'][-1] > 0.9)


def test_temporal_reg():
    np.random.seed(1337)
    print('temporal regression data:')
    (X_train, y_train), (X_test, y_test) = get_test_data(nb_train=1000,
                                                         nb_test=200,
                                                         input_shape=(3, 5),
                                                         output_shape=(2,),
                                                         classification=False)
    print('X_train:', X_train.shape)
    print('X_test:', X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:', y_test.shape)

    model = Sequential()
    model.add(GRU(y_train.shape[-1], input_shape=(X_train.shape[1], X_train.shape[2])))
    model.compile(loss='hinge', optimizer='adam')
    history = model.fit(X_train, y_train, nb_epoch=12, batch_size=16,
                        validation_data=(X_test, y_test), verbose=0)
    assert(history.history['val_loss'][-1] < 0.8)


def test_seq_to_seq():
    np.random.seed(1337)
    print('sequence to sequence data:')
    (X_train, y_train), (X_test, y_test) = get_test_data(nb_train=1000,
                                                         nb_test=200,
                                                         input_shape=(3, 5),
                                                         output_shape=(3, 5),
                                                         classification=False)
    print('X_train:', X_train.shape)
    print('X_test:', X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:', y_test.shape)

    model = Sequential()
    model.add(TimeDistributedDense(y_train.shape[-1], input_shape=(X_train.shape[1], X_train.shape[2])))
    model.compile(loss='hinge', optimizer='rmsprop')
    history = model.fit(X_train, y_train, nb_epoch=12, batch_size=16,
                        validation_data=(X_test, y_test), verbose=0)
    assert(history.history['val_loss'][-1] < 0.8)


def test_img_clf():
    np.random.seed(1337)
    print('image classification data:')
    (X_train, y_train), (X_test, y_test) = get_test_data(nb_train=1000,
                                                         nb_test=200,
                                                         input_shape=(3, 8, 8),
                                                         classification=True,
                                                         nb_class=2)
    print('X_train:', X_train.shape)
    print('X_test:', X_test.shape)
    print('y_train:', y_train.shape)
    print('y_test:', y_test.shape)

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model = Sequential()
    model.add(Convolution2D(8, 8, 8, input_shape=(3, 8, 8)))
    model.add(Activation('sigmoid'))
    model.add(Flatten())
    model.add(Dense(y_test.shape[-1]))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='sgd')
    history = model.fit(X_train, y_train, nb_epoch=12, batch_size=16,
                        validation_data=(X_test, y_test),
                        show_accuracy=True, verbose=0)
    print(history.history['val_acc'][-1])
    assert(history.history['val_acc'][-1] > 0.9)


if __name__ == '__main__':
    print('Test different types of classification and regression tasks')
    pytest.main([__file__])
