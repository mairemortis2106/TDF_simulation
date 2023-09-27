# =============================================================================
# PROBLEM B2
#
# Build a classifier for the Fashion MNIST dataset.
# The test will expect it to classify 10 classes.
# The input shape should be 28x28 monochrome. Do not resize the data.
# Your input layer should accept (28, 28) as the input shape.
#
# Don't use lambda layers in your model.
#
# Desired accuracy AND validation_accuracy > 83%
# =============================================================================

import tensorflow as tf

class Callbacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get('acc') > 0.85 and logs.get('val_acc') > 0.85:
            print("\nCriteria Have Been Met")
            self.model.stop_training = True
def solution_B2():
    fashion_mnist = tf.keras.datasets.fashion_mnist

    # NORMALIZE YOUR IMAGE HERE
    (train_data, train_label),(test_data,test_label) = fashion_mnist.load_data()

    train_data = train_data/255
    test_data = test_data/255

    # DEFINE YOUR MODEL HERE
    # End with 10 Neuron Dense, activated by softmax
    model=tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, input_shape=(28,28,1), kernel_size=3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
        ])

    # COMPILE MODEL HERE
    model.compile(optimizer=tf.optimizers.legacy.Adam(),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.fit(train_data,train_label,validation_data=(test_data,test_label),epochs=100)

    # TRAIN YOUR MODEL HERE

    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_B2()
    # model.save("model_B2.h5")
