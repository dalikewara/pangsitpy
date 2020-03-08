import os
from pangsitpy.confusion_matrix import calc_cm

Y_true = [1,1,1,1,2,0,0,0,0,0]
Y_pred = [1,1,0,0,2,0,0,1,0,0]
cm = calc_cm(Y_true, Y_pred, output_file=None, labels=None,
             figsize=(8.5, 7.5), colorbar=True, show_absolute=True,
             show_normed=True, ylim=(1.5, -.5))
print(cm)
print('=====')
temp_dir = os.path.join(os.path.dirname(__file__), '../.temp')
output_file = temp_dir + '/confusion_matrix.png'
cm = calc_cm(Y_true, Y_pred, output_file=output_file, labels=["one", "two", "three"],
             figsize=(8.5, 7.5), colorbar=True, show_absolute=True,
             show_normed=True, ylim=None)
print(cm)