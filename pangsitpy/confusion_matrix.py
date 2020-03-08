import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix


def calc_cm(Y_true, Y_pred, output_file=None, labels=None,
       figsize=(8.5, 7.5), colorbar=True, show_absolute=True,
       show_normed=True, ylim=None):
    cm = confusion_matrix(Y_true, Y_pred)
    acc = np.trace(cm) / np.sum(cm).astype('float')
    loss = 1 - acc
    if output_file:
        plot_confusion_matrix(conf_mat=cm, colorbar=colorbar, show_absolute=show_absolute,
                              show_normed=show_normed, class_names=labels, figsize=figsize)
        plt.title("Confusion Matrix\nAccuracy={:0.4f}; Loss={:0.4f}".format(acc, loss))
        plt.tight_layout()
        if ylim:
            plt.ylim(ylim)
        plt.savefig(output_file)
    return (cm, acc, loss)
