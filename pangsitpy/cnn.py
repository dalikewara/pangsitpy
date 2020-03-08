from keras.utils.vis_utils import plot_model
from keras.layers import concatenate, Dense, Dropout, Input, Flatten
from keras.layers import Conv2D, Conv1D, MaxPooling2D, MaxPooling1D, BatchNormalization
from keras.models import Model


def cnn_audio_image_1(audio_shape=(), image_shape=(), total_labels=1,
                      plot_to_file=None, optimizer=None, loss=None,
                      metrics=None):
    input_1 = Input(shape=audio_shape)
    inpt1 = Conv1D(64, kernel_size=1, activation='relu')(input_1)
    inpt1 = MaxPooling1D(pool_size=1)(inpt1)
    inpt1 = BatchNormalization()(inpt1)
    inpt1 = Conv1D(32, kernel_size=1, activation='relu')(inpt1)
    inpt1 = MaxPooling1D(pool_size=1)(inpt1)
    inpt1 = BatchNormalization()(inpt1)
    inpt1 = Dropout(0.2)(inpt1)
    inpt1 = Flatten()(inpt1)
    inpt1 = Dense(total_labels)(inpt1)
    input_2 = Input(shape=image_shape)
    inpt2 = Conv2D(64, (3, 3), activation='relu')(input_2)
    inpt2 = MaxPooling2D(pool_size=(2, 2))(inpt2)
    inpt2 = BatchNormalization()(inpt2)
    inpt2 = Conv2D(32, (3, 3), activation='relu')(inpt2)
    inpt2 = MaxPooling2D(pool_size=(2, 2))(inpt2)
    inpt2 = BatchNormalization()(inpt2)
    inpt2 = Dropout(0.2)(inpt2)
    inpt2 = Flatten()(inpt2)
    inpt2 = Dense(total_labels)(inpt2)
    multi = concatenate([inpt1, inpt2])
    multi = BatchNormalization()(multi)
    multi = Dropout(0.2)(multi)
    out = Dense(total_labels, activation='softmax')(multi)
    model = Model(inputs=[input_1, input_2], outputs=out)
    if plot_to_file:
        plot_model(model, to_file=plot_to_file, show_shapes=True,
                   show_layer_names=True)
    model.compile(optimizer=(optimizer or 'adam'),
                  loss=(loss or 'categorical_crossentropy'),
                  metrics=(metrics or ['acc']))
    print(model.summary())
    return model
