import * as tf from '@tensorflow/tfjs';
{{% load static %}}

console.log('load tfjs');
const model = await tf.loadLayersModel('https://rocopicker-gyrym.run.goorm.io/model/model.json');