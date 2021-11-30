
import torch
from torch.utils.data import Dataset
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']

class FaceScan_Dataset(Dataset):
    def __init__(self, test_images , test_targets, transform=None):
        self.transform = transform
        self.test_targets = test_targets
        self.img_names_list = test_images 
        self.img_names_list.sort()

    def __len__(self):
        return len(self.img_names_list)

    def __getitem__(self, item):
        img = Image.open(self.img_names_list[item]).convert('RGB') # important
        label = self.test_targets[item]
        if self.transform is not None:
            try:
                img = self.transform(img)
            except:
                print("Cannot transform image: {}".format(self.img_names_list[item]))
        return img, label
