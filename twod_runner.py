from twodunet import TwoDUnet
from imageparser import ImageParser
import numpy as np


parser = ImageParser()

utrech_dataset, singapore_dataset, amsterdam_dataset = parser.get_all_images_and_labels()

data_utrecht = [row[1] for row in utrech_dataset]
labels_utrecht = [row[0] for row in utrech_dataset]

data_singapore = [row[1] for row in singapore_dataset]
labels_singapore = [row[0] for row in singapore_dataset]

#data_amsterdam = [row[1] for row in amsterdam_dataset]
#labels_amsterdam = [row[0] for row in amsterdam_dataset]

all_data = data_utrecht + data_singapore # + list(data_amsterdam)
all_labels = labels_utrecht + labels_singapore # + labels_amsterdam


slice_shape = (240, 240)

data = parser.get_all_images_np_twod(all_data, slice_shape)
labels = parser.get_all_images_np_twod(all_labels, slice_shape, normalization=False)

data = np.stack(data, axis=0)
labels = np.asanyarray(labels)

print(data.shape, labels.shape)

unet = TwoDUnet(model_path=None, img_shape=data.shape[1:])

training_name = 'first_test'
base_path = '/home/pablo/Google Drive/UNED/Vision_Artificial/M2/WhiteMatterHyperintensities/'
test_size = 0.3

print(data.shape, labels.shape)

unet.train(data, labels, test_size, training_name, base_path, epochs=10, batch_size=1)