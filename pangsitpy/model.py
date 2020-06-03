import matplotlib.pyplot as plt


def visualize_training(model, metrics=('acc', 'loss'), acc_output_file=None,
                       loss_output_file=None,
                       # disabled since (0.0.8)
                       output_file=None,
                       colors=('y', 'b')):
    h = model.history
    h_acc = h.history[metrics[0]]
    h_loss = h.history[metrics[1]]
    epochs = range(1, len(h_acc) + 1)
    plt.figure()
    plt.plot(epochs, h_acc, colors[0], label='Training ' + metrics[0])
    try:
        h_val_acc = h.history['val_' + metrics[0]]
        plt.plot(epochs, h_val_acc, colors[1], label='Validation ' + metrics[0])
        plt.title('Training and validation ' + metrics[0])
    except:
        plt.title('Training ' + metrics[0])
    plt.xlabel("epoch")
    plt.ylabel(metrics[0])
    plt.legend()
    if output_file:
        print('This argument was removed. Please use (acc_output_file=None) or (loss_output_file=None) instead.')
    if acc_output_file:
        plt.savefig(acc_output_file)
    else:
        plt.show()
    plt.figure()
    plt.plot(epochs, h_loss, colors[0], label='Training ' + metrics[1])
    try:
        h_val_loss = h.history['val_' + metrics[1]]
        plt.plot(epochs, h_val_loss, colors[1], label='Validation ' + metrics[1])
        plt.title('Training and validation ' + metrics[1])
    except:
        plt.title('Training ' + metrics[1])
    plt.xlabel("epoch")
    plt.ylabel(metrics[1])
    plt.legend()
    if loss_output_file:
        plt.savefig(loss_output_file)
    else:
        plt.show()
