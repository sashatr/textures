import numpy as np


def get_features(image, model, layers):
    features = {}
    x = image
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x

    return features


def transformation_max(layer):
    layer_array = layer[0].numpy()
    content = layer_array.reshape(
        (layer_array.shape[0], layer_array.shape[1]*layer_array.shape[2])
    ).T

    result = content[np.arange(len(content)), np.argmax(content, axis=1)]
    result = result.reshape((layer_array.shape[1], layer_array.shape[2]))
    result *= (255.0 / result.max())
    return result.astype(int)


def transformation_mean(layer, weights):
    layer_array = layer[0].numpy()
    data_2 = layer_array.reshape(
        (layer_array.shape[0], layer_array.shape[1] * layer_array.shape[2])
    ).T
    result = np.average(data_2, weights=weights, axis=1)

    result = result.reshape((layer_array.shape[1], layer_array.shape[2]))
    result *= (255.0 / result.max())
    return result.astype(int)


def get_weights(number_layers):
    style_weights = [
        # convolution depth - weight
        (64, 1.0),
        (128, 0.75),
        (256, 0.2),
        (512, 0.2),
        (512, 0.2)
    ]
    weights = []

    for layer in range(number_layers):
        w_number, value = style_weights[layer]
        w = [value for _ in range(w_number)]
        weights.extend(w)

    return weights
