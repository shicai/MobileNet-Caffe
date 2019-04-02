# MobileNet-Caffe

### Introduction

This is a Caffe implementation of Google's MobileNets (v1 and v2). For details, please read the following papers:
- [v1] [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
- [v2] [Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation](https://arxiv.org/abs/1801.04381)


### Pretrained Models on ImageNet

We provide pretrained MobileNet models on ImageNet, which achieve slightly better accuracy rates than the original ones reported in the paper. 

The top-1/5 accuracy rates by using single center crop (crop size: 224x224, image size: 256xN):

Network|Top-1|Top-5|sha256sum|Architecture
:---:|:---:|:---:|:---:|:---:
MobileNet v1| 70.81| 89.85| 8d6edcd3 (16.2 MB) | [netscope](http://ethereon.github.io/netscope/#/gist/2883d142ae486d4237e50f392f32994e), [netron](http://lutzroeder.github.io/netron?gist=2883d142ae486d4237e50f392f32994e)
MobileNet v2| 71.90| 90.49| a3124ce7 (13.5 MB)| [netscope](http://ethereon.github.io/netscope/#/gist/d01b5b8783b4582a42fe07bd46243986), [netron](http://lutzroeder.github.io/netron?gist=d01b5b8783b4582a42fe07bd46243986)


### Evaluate Models with a single image

Evaluate MobileNet v1:

`python eval_image.py --proto mobilenet_deploy.prototxt --model mobilenet.caffemodel --image ./cat.jpg`

Expected Outputs:

```
0.42 - 'n02123159 tiger cat'
0.08 - 'n02119022 red fox, Vulpes vulpes'
0.07 - 'n02119789 kit fox, Vulpes macrotis'
0.06 - 'n02113023 Pembroke, Pembroke Welsh corgi'
0.06 - 'n02123045 tabby, tabby cat'
```

Evaluate MobileNet v2:

`python eval_image.py --proto mobilenet_v2_deploy.prototxt --model mobilenet_v2.caffemodel  --image ./cat.jpg`

Expected Outputs:

```
0.26 - 'n02123159 tiger cat'
0.22 - 'n02124075 Egyptian cat'
0.15 - 'n02123045 tabby, tabby cat'
0.04 - 'n02119022 red fox, Vulpes vulpes'
0.02 - 'n02326432 hare'
```

### Finetuning on your own data
Modify `deploy.prototxt` and save it as your `train.prototxt` as follows:
Remove the first 5 `input`/`input_dim` lines, and add `Image Data` layer in the beginning like this:
```
layer {
  name: "data"
  type: "ImageData"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform_param {
    scale: 0.017
    mirror: true
    crop_size: 224
    mean_value: [103.94, 116.78, 123.68]
  }
  image_data_param {
    source: "your_list_train_txt"
    batch_size: 32 # your batch size
    new_height: 256
    new_width: 256
    root_folder: "your_path_to_training_data_folder"
  }
}

```

Remove the last `prob` layer, and add `Loss` and `Accuracy` layers in the end like this:
```
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "fc7"
  bottom: "label"
  top: "loss"
}
layer {
  name: "top1/acc"
  type: "Accuracy"
  bottom: "fc7"
  bottom: "label"
  top: "top1/acc"
  include {
    phase: TEST
  }
}
layer {
  name: "top5/acc"
  type: "Accuracy"
  bottom: "fc7"
  bottom: "label"
  top: "top5/acc"
  include {
    phase: TEST
  }
  accuracy_param {
    top_k: 5
  }
}
```
### Related Projects
MobileNet in this repo has been used in the following projects, we recommend you to take a look:
- The MobileNet neural network using Apple's new CoreML framework
 [hollance/MobileNet-CoreML](https://github.com/hollance/MobileNet-CoreML)
- Mobile-deep-learning [baidu/mobile-deep-learning](https://github.com/baidu/mobile-deep-learning)
- Receptive Field Block Net for Accurate and Fast Object Detection [ruinmessi/RFBNet](https://github.com/ruinmessi/RFBNet)
- Depthwise Convolutional Layer [yonghenglh6/DepthwiseConvolution](https://github.com/yonghenglh6/DepthwiseConvolution)
- MobileNet-MXNet [KeyKy/mobilenet-mxnet](https://github.com/KeyKy/mobilenet-mxnet)
- Caffe2-MobileNet [camel007/caffe2-mobilenet](https://github.com/camel007/caffe2-mobilenet)


### Updates (Feb. 5, 2018)

- Add pretrained MobileNet v2 models (including deploy.prototxt and weights)
- Hold pretrained weights in this repo
- Add sha256sum code for pretrained weights
- Add some code snippets for single image evaluation
- Uncomment **engine: CAFFE** used in `mobilenet_deploy.prototxt`
- Add params (`lr_mult` and `decay_mult`) for `Scale` layers of `mobilenet_deploy.prototxt`
- Add `prob` layer for `mobilenet_deploy.prototxt`
