# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
from options.train_options import TrainOptions
from loaders import aligned_data_loader
from models import pix2pix_model

BATCH_SIZE = 1
eval_num_threads = 2
opt = TrainOptions().parse()  # set CUDA_VISIBLE_DEVICES before import torch
model = pix2pix_model.Pix2PixModel(opt)
torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = True
best_epoch = 0
global_step = 0
model.switch_to_eval()
video_list = 'D:/A-Eye For The Blind/2dtodepth/infile/'
save_path = 'D:/A-Eye For The Blind/2dtodepth/outfile/'

user_uid = 23 # set up once

def main():

	video_data_loader = aligned_data_loader.DAVISDataLoader(video_list, BATCH_SIZE)
	video_dataset = video_data_loader.load_data()
	for i, data in enumerate(video_dataset):
#	    print(i)
	    stacked_img = data[0]
	    targets = data[1]
	    model.run_and_save_DAVIS(stacked_img, targets, save_path)

if __name__ == '__main__':
    main()
