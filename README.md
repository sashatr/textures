# Textures

-----

#### The pretrained convolutional network (VGG 19) is used to get texture.
#### For getting the Style Features  are used layers from the list (conv1_1, conv2_1, conv3_1, conv4_1, conv5_1) based on [original paper](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf). 

-----

## Below is an example of the results for full images and patches

#### Origin patches:

![Alt text](data/imgs/origin_patches.png)

-----

#### Using two first layers for patches

![Alt text](data/imgs/first_two_layers_patches.png)

-----

#### Origin images:

![Alt text](data/imgs/origin.png)

-----

#### Using all layers

*Merger tensor by maximum values*
![Alt text](data/imgs/all_layers_max.png)
*Merger tensor by mean*
![Alt text](data/imgs/all_layers_mean.png)

-----

#### Using first layer

*Merger tensor by maximum values*
![Alt text](data/imgs/first_layer_max.png)
*Merger tensor by mean*
![Alt text](data/imgs/first_layer_mean.png)

-----

#### Using two first layers

*Merger tensor by maximum values*
![Alt text](data/imgs/fwo_first_layers_max.png)
*Merger tensor by mean*
![Alt text](data/imgs/fwo_first_layers_mean.png)

-----

## TODO:
- *add padding to rectangular images*
- *etс*

