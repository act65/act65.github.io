---
layout: post
title: Unsupervised skip connections
---

[Ladder nets](https://arxiv.org/abs/1507.02672) (aka [Unets](https://arxiv.org/abs/1505.04597)) are currently achieving state-of-the art results on image to image translation, for example [see here](https://phillipi.github.io/pix2pix/). This network architecture achieves such great results because the skip connetions allow higher frequency information, such as edges and gradients, to be easily communicated between the encoder and decoder. This is useful for image to image translation as typically we are translating between 'styles' (low frequency content such as palette, textures), while the high frequency content maps to the 'content' (see [style transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)). $\textbf{Q:}$ How can we use this architecutre for unsupervised learning?


## An autoencoder with skips

Given this architectures power for image processing, it would be nice to use in unsupervised setting as well. However, naive implementation of an autoencoder with these skip connections is just cheating... The skip connections allow information to be skipped straight to the output, making reconstruction rather easy.

<!-- TODO show example of pathology. Deeper layers dont need to learn anything... -->

$\textbf{Q:}$ How can we force the network to use the deeper layers? How can we constrain the capacity of the skip connections?

<img src="../images/ladder-net.png" width="250" height="250" class="center-image">


### Filter the frequency content

What if we enforced constrains on the skip connections to ensure the earlier skip connections can not communicate low freqency information? A high and low pass filter.

$$
\begin{align}
z_{low} &= \text{avg_pool}(x)\\
z_{high} &= x - z_{low}\\
\end{align}
$$


<div id="starry-night">
    <img height="224" width="224" id="starry-night-img" src="../images/starry-night.jpg"/>
</div>
<div id="albertina">    
  <img height="224" width="224" id="albertina-img" src="../images/albertina.jpeg"/>
</div>

<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@0.11.2"></script>
<script type="text/javascript">
  // supposedly can use https://github.com/envygeeks/jekyll-assets/blob/master/README.md
  // to move js into assets folder.

  const [width, height] = [224, 224];

  function draw(image, div, name) {
    const canvas = document.createElement('canvas');
    canvas.className = name;

    tf.toPixels(image.reshape([height, width,3]), canvas);

    div.appendChild(canvas);
  }

  function low_pass_filter(img){
    pool = tf.layers.averagePooling2d({"poolSize": [4,4],
                                       "strides": [4,4],
                                       "padding": "same",
                                       "dataFormat": "channelsLast"});
    low = pool.apply(img.reshape([1, width, height, 3]));
    return tf.image.resizeBilinear(low, [width, height]);
  }

  function decompose(name){
    const div = document.getElementById(name);

    const imgElement = document.getElementById(name + '-img');
    const img = tf.fromPixels(imgElement).toFloat();

    const low = low_pass_filter(img);
    const high = tf.sub(img, low);

    // not sure wtf is happening here. `other` renders, `low` doesnt so...
    // tf.sub(img, high) does work. so it is the content of the array that is the issue?!
    const other = tf.add(img, high)

    // draw(tf.sigmoid(low), div, 'low');
    draw(tf.sigmoid(other), div, 'low');
    draw(tf.sigmoid(high), div, 'high');
  }

  decompose("starry-night");
  decompose("albertina");
</script>
(_code for generating images is in [tfjs](https://js.tensorflow.org/) (see source). but is kinda buggy_)


### Structured latent space

<side>allowing you to have distinct priors on each one?</side>
Now our hidden space is structured. Earlier skips carry high frequency content and later skips carry low frequency content.

<img src="../images/freq-net.png" width="250" height="250" class="center-image">

### 'High' level content

What do we mean when we talk about high level content? Familiar definitions include invariance to transforms, or generality, or absractness. But another valid interpretation seems to be: low frequency content. Thus we hope to capture the high level content, by forcing the information through low pass filters.

__TODO.__

- Explore the connection to a recursive wavelet decomposition
- Actually test at scale

***

The idea was Paul Matthews', I just wrote it down.
