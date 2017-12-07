# Computer Vision - Assignment 02

## Identification

**[Github repository](https://github.com/EliaRigo/bike-tracking)**

**Elia Rigo**

**190487**

**elia.rigo@studenti.unitn.it**

## What this program does?
This Python program tries to detect and count the number of bicycles and pedestrians entering and leaving a roundabout.

**Note well: This program is intended to be mostly a didactic program**; it shows how to use the OpenCV library and one of the possible application of the background subtraction algorithm.



## Requirements
* **Python** >= v2.7
* **virtualenv**
* **OpenCV** >= v3 (You can install it following these [instructions](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/):)
* **[bgslibrary](https://github.com/andrewssobral/bgslibrary)** >= v2.0.0 

## How to run
You can easily run my script with the command:

```python bike-tracking.py```

## Futher possible improvements
* Convery python scirpt to C++
* Create a structure for the "tracking" of the detected objects and relative algorithms to understand which object is who

## Issue
* The counting may be not so accurate
* According to the developer of the [bgslibrary](https://github.com/andrewssobral/bgslibrary), there is a memory leak in the Python version of this library which tends to drain quickly the RAM available in the system. You can contribute to finding/solving the problem at this [public issue](https://github.com/andrewssobral/bgslibrary/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+python)
* Due to the RAM leak, the sample video last only 6 minutes (instead of the 7 minutes of the original video) however, I think, they are enough to understand how the program works

## Sample Video
The sample video is available at this [link](https://drive.google.com/file/d/1P6gPqIjUQcOQbR_xPJOXge7gHKrjQ8iG/view?usp=sharing).