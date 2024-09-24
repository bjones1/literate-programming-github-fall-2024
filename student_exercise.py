"""

    Digital Signal Processing

    Module 2.5 Student Exercise
    Example CNN code with two class problem - squares and circles

    Requires: TF 2.1, PIL

    To install PIL: conda install -c anaconda pillow

    29 Aug 2020, John Ball

"""

# Clear the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Force TF messages to disappear
from silence_tensorflow import silence_tensorflow
silence_tensorflow()

import tensorflow
import numpy as np
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt

from tensorflow.keras import backend
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Dropout, Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model

from confusion_matrix import confusion_matrix, print_confusion_matrix_stats

from PIL import Image


#______________________________________________________________________________________________________________________
#
# This function gets the layer output from a specific model
# For some reason, this code occasionally hangs Keras if running on a GPU.
#
# model              TF model.
# x                  Input data (numpy array or [x1,x2,...,xN] for multi-input network).
# layer_number       The layer number, a non-negative integer.
# network_mode       Set to 0 to run the network in test mode (things like Dropout will be in effect).
#                    Set to 1 to run the network in train mode.
#                    Defaults to 0 (test mode).
#______________________________________________________________________________________________________________________
#
def get_layer_output(model, x, layer_number, network_mode=0):

    network_mode = tensorflow.convert_to_tensor(network_mode)  # This allows the code to work in graph and eager modes!
    x = tensorflow.convert_to_tensor(x)

    partial_model = Model(model.inputs, model.layers[layer_number].output)
    if network_mode == 0:
        x_layer = partial_model([x], training=False)  # runs the model in test mode
    else:
        x_layer = partial_model([x], training=True)  # runs the model in training mode

    return x_layer.numpy()


#______________________________________________________________________________________________________________________
#
# This function gets the logit layer for a network that has last two layers as dense and softmax and plots the
# logit values and decision boundaries for training and testing.
#
# Inputs:
#
# model              TF model.
# epoch              The epoch number. Use epoch=0 to initialize the plot.
# Xtrain             Input training data.
# Xtest              Input testing data.
# Ytrain             Input training class (onehots). Currently supports only classes {0,1}.
# Ytest              Input testing class (onehots). Currently supports only classes {0,1}.
# train_acc          Training accuracy (0 to 1).
# fig                Figure number. Set to [] on initial call.
# network_mode       Set to 0 to run the network in test mode (things like Dropout will be in effect).
#                    Set to 1 to run the network in train mode.
#                    Defaults to 0 (test mode).
#______________________________________________________________________________________________________________________
#
def plot_logits_decision(model, epoch, Xtrain, Xtest, Ytrain, Ytest, train_acc, fignum, network_mode=0):

    # Create a figure if this is the first call or open the same figure
    if epoch == 0:
        fignum = 1
        plt.figure(fignum, figsize=(12, 8))
    else:
        plt.figure(fignum)
        plt.cla()

    # Find the number of layers in the model. The logit layer will be the next-to-last layer.
    model_dictionary = {v.name: i for i, v in enumerate(model.layers)}
    logit_layer = len(model_dictionary) - 2  # The last layer is len-1, so next-to-last is len-2

    # Convert onehots back to classes
    Ytrain = K.argmax(Ytrain).numpy()
    Ytest = K.argmax(Ytest).numpy()

    # Run the data through network and get outputs
    logit_train = get_layer_output(model, Xtrain, logit_layer, network_mode=network_mode)
    logit_test = get_layer_output(model, Xtest, logit_layer, network_mode=network_mode)

    # Plot
    colors = ['g', 'r']
    markers = ['s', 'o']
    marker_size_train = 50
    marker_size_test = 30

    # Split into classes and plot training and testing data
    num_classes = len(np.unique(Ytrain))

    for c in np.arange(num_classes):

        # Get indices for this class for training and testing
        train_class_indx = np.nonzero(Ytrain == c)
        test_class_indx = np.nonzero(Ytest == c)

        # Plot
        if len(train_class_indx) > 0:
            plt.scatter(logit_train[train_class_indx, 0], logit_train[train_class_indx, 1],
                        edgecolors=colors[c],
                        marker=markers[c],
                        facecolors='none',
                        label="Train Class {cls:1d}".format(cls=c),
                        s=marker_size_train
                        )

        if len(test_class_indx) > 0:
            plt.scatter(logit_test[test_class_indx, 0], logit_test[test_class_indx, 1],
                        edgecolors=colors[c],
                        marker=markers[c],
                        facecolors=colors[c],
                        label="Test Class {cls:1d}".format(cls=c),
                        s=marker_size_test
                        )

    plt.legend()
    plt.xlabel('Logit output 0')
    plt.ylabel('Logit output 1')
    plt.title("Training Epoch={eph:-3d} Accuracy ={acc:7.2f}%".format(eph=epoch, acc=train_acc*100))
    plt.pause(0.5)
    plt.draw()
    plt.show(block=False)

    return fignum


#______________________________________________________________________________________________________________________
#
# Main code starts here
#______________________________________________________________________________________________________________________
#
print("DSP - Square/Circle CNN example code.\n")

# Load data - Students, put your data path here. Do not remove the r in front of the string.
data_dir = r'.\Module_2dot5_data'

filenames_counter = 0
class_counter = -1  # First class is zero
for subdir, dirs, files in os.walk(data_dir):
    for file in files:

        # Read the image in, convert to numpy array
        fname = subdir + '\\' + file
        im = Image.open(fname)
        im = np.array(im).astype('float32')
        im = np.expand_dims(im, axis=0)
        # print("Added file %-20s (class %d)." % (file, class_counter))  # Uncomment to show files loading

        if filenames_counter == 0:
            X = im
            Y = [class_counter]
        else:
            X = np.append(X, im, axis=0)
            Y = np.append(Y, [class_counter], axis=-1)

        filenames_counter += 1
    class_counter += 1

# TF expects 2D images as 4D tensor (batches, num rows, num cols, num channels)
# Make out inputs a 4D array
X = np.expand_dims(X, axis=-1)

num_instances = X.shape[0]
num_classes = len(np.unique(Y))

print("\nRead in %d files.\n" % num_instances)
print("\nShape of X is", X.shape)
print("Shape of Y is", Y.shape)

# Run on CPU 0
print("\nRunning on CPU 0.")
with tensorflow.device('/cpu:0'):

    # Convert classes to onehots
    print("Converting %d class data to one-hots:" % num_classes)
    Y = to_categorical(Y, num_classes)

    # Normalize inputs to [0,1]
    xmin = np.min(X)
    xmax = np.max(X)
    X = (X - xmin) / (xmax - xmin)

    # Randomly split into training and testing
    train_frac = 0.80
    num_train = int(X.shape[0] * train_frac)
    all_indx = np.random.permutation(num_instances)
    train_indx = all_indx[0:num_train]
    test_indx = all_indx[(num_train+1):]

    Xtrain = X[train_indx, :, :, 0]
    Xtrain = np.expand_dims(Xtrain, axis=-1)
    Ytrain = Y[train_indx]

    Xtest = X[test_indx, :, :, 0]
    Xtest = np.expand_dims(Xtest, axis=-1)
    Ytest = Y[test_indx]

    # Print shapes
    print("Xtrain shape=", Xtrain.shape)
    print("Ytrain shape=", Ytrain.shape)

    # Convert one-hot tensors back to class labels (and make them numpy arrays)
    y_train_true_class = K.argmax(Ytrain).numpy()
    y_test_true_class = K.argmax(Ytest).numpy()

    # Define input shape - note: in TF, we don't include the batch index
    input_shape = [Xtrain.shape[1], Xtrain.shape[2], Xtrain.shape[3]]

    # Setup the CNN, using TF function form
    xin = Input(shape=input_shape)

    x = Conv2D(10, 3, activation='relu', input_shape=input_shape, padding='same', name='Conv2D_1')(xin)
    x = MaxPooling2D(2, name='Pool_1')(x)
    x = Dropout(0.25, name='Dropout_1')(x)

    x = Conv2D(10, 3, activation='relu', padding='same', name='Conv2D_2')(x)
    x = MaxPooling2D(2, name='Pool_2')(x)
    x = Dropout(0.25, name='Dropout_2')(x)

    x = Conv2D(10, 3, activation='relu', padding='same', name='Conv2D_3')(x)
    x = MaxPooling2D(2, name='Pool_3')(x)
    x = Dropout(0.25, name='Dropout_3')(x)

    x = Conv2D(10, 3, activation='relu', padding='same', name='Conv2D_4')(x)
    x = MaxPooling2D(2, name='Pool_4')(x)
    x = Dropout(0.25, name='Dropout_4')(x)

    x = Flatten(name='Flat')(x)
    x = Dense(2, name='Dense_1')(x)
    xout = Activation('softmax', name='Softmax_1')(x)    # output layer is 2-dim one-hot vector

    # Create the model
    model = Model(xin, xout, name='square_circle_model')

    # Print summary to screen
    model.summary()

    # Compile the model
    model.compile(loss='binary_crossentropy',
                  optimizer=tensorflow.keras.optimizers.Adam(learning_rate=1e-3),
                  metrics=['accuracy'])

    # Train the network
    print("\nTraining the network...\n")

    # Define some training parameters
    train_batch_size = 25
    test_batch_size = num_instances
    epochs = 20

    for this_epoch in np.arange(epochs):

        print("\nTraining epoch number: %d." % (this_epoch + 1))

        # Run training in a loop one epoch at a time. The variable history will contain training accuracies and losses
        history = model.fit(Xtrain, Ytrain, epochs=1, batch_size=train_batch_size)

        # Compute predictions (test mode) for training and testing data
        Ytrain_pred = model.predict(Xtrain, batch_size=test_batch_size, verbose=0)
        Ytest_pred = model.predict(Xtest, batch_size=test_batch_size, verbose=0)

        # Convert one-hot tensors back to class labels (and make them numpy arrays)
        y_train_pred_class = K.argmax(Ytrain_pred).numpy()
        y_test_pred_class = K.argmax(Ytest_pred).numpy()

        # Evaluate results on training data
        cm_train, cm_train_acc = confusion_matrix(y_train_true_class, y_train_pred_class)
        cm_test, cm_test_acc = confusion_matrix(y_test_true_class, y_test_pred_class)

        # Save accuracies for plotting
        if this_epoch == 0:
            train_acc = cm_train_acc
            train_loss = history.history['loss']
            test_acc = cm_test_acc
            fignum = []
        else:
            train_acc = np.append(train_acc, cm_train_acc)
            train_loss = np.append(train_loss, history.history['loss'])
            test_acc = np.append(test_acc, cm_test_acc)

        # Plot logits and decision boundaries
        fignum = plot_logits_decision(model, this_epoch, Xtrain, Xtest, Ytrain, Ytest, cm_train_acc, fignum)

    # Give final results for training and testing
    print("\nFinal results (training):")
    print_confusion_matrix_stats(cm_train, "Training", pos=1)

    print("\nFinal results (testing):")
    print_confusion_matrix_stats(cm_test, "Testing", pos=1)

    # Plot training and test accuracy
    plt.figure()
    plt.plot(train_acc, label="Train")
    plt.plot(test_acc, label="Test")
    plt.title('Train and Test Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend()
    plt.draw()
    plt.show(block=False)

    # Plot training loss
    plt.figure()
    plt.plot(train_loss)
    plt.title('Training Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.draw()

    # Leave figures up and wait for user to exit
    print("\nPress ctrl-break or close plot windows to exit program.")
    plt.show(block=True)
