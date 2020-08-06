# textures

-----

## Using a pretrained convolutional network to get texture. According to the [original paper](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf) not the entire list of layers is used, but only a part to get the *Style Features* (conv1_1, conv2_1, conv3_1, conv4_1, conv5_1).

-----

## Below is an example of the results

## Origin images:

![Alt text](data/imgs/origin.png)

-----

## Using all layers

### Merger tensor by maximum values
![Alt text](data/imgs/all_layers_max.png)
### Merger tensor by mean
![Alt text](data/imgs/all_layers_mean.png)

-----

## Using first layer

### Merger tensor by maximum values
![Alt text](data/imgs/first_layer_max.png)
### Merger tensor by mean
![Alt text](data/imgs/first_layer_mean.png)

-----

## Using wto first layers

### Merger tensor by maximum values
![Alt text](data/imgs/fwo_first_layers_max.png)
### Merger tensor by mean
![Alt text](data/imgs/fwo_first_layers_mean.png)

-----

## TODO:
- add padding to rectangular images
- etс

