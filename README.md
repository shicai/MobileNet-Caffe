# MobileNet-Caffe

### Introduction

This is a Caffe implementation of Google's MobileNets. For details, please read the original paper:
- [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)


### Pretrained Models on ImageNet

We provide a pretrained MobileNet model on ImageNet, which achieves slightly better accuracy rates than the original one reported in the paper. 

The top-1/5 accuracy rates by using single center crop (crop size: 224x224, image size: 256xN):

Network|Top-1|Top-5|Download|Architecture
:---:|:---:|:---:|:---:|:---:
MobileNet| 70.81| 89.85| [caffemodel (16.2 MB)](https://drive.google.com/open?id=0B7ubpZO7HnlCVFFJQU5TQ0dkLUE)| [netscope](http://ethereon.github.io/netscope/#/gist/2883d142ae486d4237e50f392f32994e)


### Notes

- BGR mean values **[103.94,116.78,123.68]** are subtracted
- **scale: 0.017** is used as std values for image preprocessing
- please uncomment **engine: CAFFE** used in the conv layers with `group`, if you encounter memory problems.
