import matplotlib.pyplot as plt


def visualize_training(model, metrics=('acc', 'loss'), acc_output_file=None,
                       loss_output_file=None,
                       # removed since (0.0.8)
                       output_file=None):
    h = model.history
    h_acc = h.history[metrics[0]]
    h_loss = h.history[metrics[1]]
    epochs = range(1, len(h_acc) + 1)
    plt.figure()
    plt.plot(epochs, h_acc, 'bo', label='Training ' + metrics[0])
    try:
        h_val_acc = h.history['val_' + metrics[0]]
        plt.plot(epochs, h_val_acc, 'b', label='Validation ' + metrics[0])
        plt.title('Training and validation ' + metrics[0])
    except:
        plt.title('Training ' + metrics[0])
    plt.legend()
    if output_file:
        print('This argument was removed. Please use (acc_output_file=None) or (loss_output_file=None) instead.')
    if acc_output_file:
        plt.savefig(acc_output_file)
    else:
        plt.show()
    plt.figure()
    plt.plot(epochs, h_loss, 'bo', label='Training ' + metrics[1])
    try:
        h_val_loss = h.history['val_' + metrics[1]]
        plt.plot(epochs, h_val_loss, 'b', label='Validation ' + metrics[1])
        plt.title('Training and validation ' + metrics[1])
    except:
        plt.title('Training ' + metrics[1])
    plt.legend()
    if loss_output_file:
        plt.savefig(loss_output_file)
    else:
        plt.show()
