# =============================================================================
# PROBLEM C2
#
# Create a classifier for the MNIST Handwritten digit dataset.
# The test will expect it to classify 10 classes.
#
# Don't use lambda layers in your model.
#
# Desired accuracy AND validation_accuracy > 91%
# =============================================================================

import tensorflow as tf


def solution_C2():
    mnist = tf.keras.datasets.mnist

    # NORMALIZE YOUR IMAGE HERE
    (train_data, train_label),(test_data,test_label) = mnist.load_data()

    train_data = train_data.astype('float32')/255
    test_data = test_data.astype('float32')/255

    train_data = train_data[..., tf.newaxis]
    test_data = test_data[..., tf.newaxis]

    # DEFINE YOUR MODEL HERE
    # End with 10 Neuron Dense, activated by softmax
    model=tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, input_shape=(28,28,1), kernel_size=3, activation='relu'),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(212, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
        ])

    # COMPILE MODEL HERE
    model.compile(optimizer=tf.optimizers.legacy.Adam(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy']
                  )
    # TRAIN YOUR MODEL HERE
    model.fit(train_data,train_label,validation_data=(test_data,test_label),epochs=10)

    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_C2()
    # model.save("model_C2.h5")
