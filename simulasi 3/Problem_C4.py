# =====================================================================================================
# PROBLEM C4
#
# Build and train a classifier for the sarcasm dataset.
# The classifier should have a final layer with 1 neuron activated by sigmoid.
#
# Do not use lambda layers in your model.
#
# Dataset used in this problem is built by Rishabh Misra (https://rishabhmisra.github.io/publications).
#
# Desired accuracy and validation_accuracy > 75%
# =======================================================================================================

import json
import tensorflow as tf
import numpy as np
import urllib
from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences


def solution_C4():
    # data_url = 'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/sarcasm.json'
    # urllib.request.urlretrieve(data_url, 'sarcasm.json')

    # DO NOT CHANGE THIS CODE
    # Make sure you used all of these parameters or test may fail
    vocab_size = 1000
    embedding_dim = 16
    max_length = 120
    trunc_type = 'post'
    padding_type = 'post'
    oov_tok = "<OOV>"
    training_size = 20000

    sentences = []
    labels = []
    # YOUR CODE HERE
    with open('sarcasm.json', 'r') as f:
        data = json.load(f)
        for item in data:
            sentences.append(item['headline'])
            labels.append(item['is_sarcastic'])


    training_data = sentences[:training_size]
    training_labels = labels[:training_size]
    validation_data = sentences[training_size:]
    validation_labels = labels[training_size:]

    training_labels = np.array(training_labels)
    validation_labels = np.array(validation_labels)

    # Fit your tokenizer with training data
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_data)

    training_sequences = tokenizer.texts_to_sequences(training_data)
    validation_sequences = tokenizer.texts_to_sequences(validation_data)

    train_pad = pad_sequences(training_sequences,
                              maxlen=max_length,
                              padding=padding_type,
                              truncating=trunc_type
                              )
    validation_pad = pad_sequences(validation_sequences,
                                   maxlen=max_length,
                                   padding=padding_type,
                                   truncating=trunc_type
                                   )


    # model = tf.keras.Sequential([
    #     # YOUR CODE HERE. DO not change the last layer or test may fail
    #     tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    #     tf.keras.layers.GlobalAveragePooling1D(),
    #     tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    #     tf.keras.layers.Dense(1, activation='sigmoid')
    # ])

    model = tf.keras.Sequential([
        # YOUR CODE HERE. DO not change the last layer or test may fail
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.Conv1D(128, 5, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        tf.keras.layers.GlobalMaxPooling1D(),
        tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer=tf.optimizers.legacy.Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    es = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
    model.fit(train_pad,
              training_labels,
              validation_data=(validation_pad, validation_labels),
              epochs=10,
              callbacks=[es])

    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_C4()
    # model.save("model_C4.h5")
