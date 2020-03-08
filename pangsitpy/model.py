import matplotlib.pyplot as plt

def visualize_training(model, output_file=None):
    h = model.history
    h_acc = h.history['acc']
    h_val_acc = h.history['val_acc']
    h_loss = h.history['loss']
    h_val_loss = h.history['val_loss']
    epochs = range(1, len(h_acc) + 1)
    plt.figure()
    plt.plot(epochs, h_acc, 'bo', label='Training acc')
    plt.plot(epochs, h_val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    if output_file:
        plt.savefig(output_file + '.acc.png')
    else:
        plt.show()
    plt.figure()
    plt.plot(epochs, h_loss, 'bo', label='Training loss')
    plt.plot(epochs, h_val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    if output_file:
        plt.savefig(output_file + '.loss.png')
    else:
        plt.show()