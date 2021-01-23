# Flask With TensorFlow Lite

![index_image](https://github.com/chrispmaag/flask_with_tensorflow_lite/blob/main/images/index_image.jpg)

In this project, we will deploy a TensorFlow Lite model using Flask to predict whether Rock, Paper, or Scissors has been thrown. After fine tuning a pre-trained MobileNetV2 model in TensorFlow, exporting the model using `tf.saved_model.save()`, and converting to TFLite format using `tf.lite.TFLiteConverter.from_saved_model()`, we are ready to use Flask for deployment.

The `app.py` file defines the route for Flask to render `index.html` for GET requests and `result.html` for POST requests. To help Flask grab the correct image for plotting, we make sure to pass in the current time as a variable to both the `plot_category` and `render_template` functions.

In `inference.py`, we load the converted tflite model and use it to predict the category of image (rock, paper, or scissors). We also save a .png version of the image to display back when we display `result.html`.

Finally, in `result.html` we utilize Jinja placeholders to allow for the predicted category name and image to be inserted into the HTML.

## Library Requirements
- tensorflow, flask, and matplotlib. See the `environment.yml` file for matching any library version numbers.

## Data
We are using a pre-trained model tuned on images of rock, paper, and scissors images. When you go to evaluate the model, you'll want to use images with three color channels, e.g. (224, 224, 3). 

## Get the Code
Download the repo. Then navigate to the directory where you saved the repo to in Terminal. Run the following commands to test out the model:

```
$export FLASK_APP=app.py
$flask run
```

Then navigate to http://127.0.0.1:5000/ (local host) to be able to insert an image and infer its class name.

## Results

Sample results from the model showing the input image and text for the predicted class name:

![rock_predicts_rock](https://github.com/chrispmaag/flask_with_tensorflow_lite/blob/main/images/rock_predicts_rock.jpg)
![scissors_predicts_scissors](https://github.com/chrispmaag/flask_with_tensorflow_lite/blob/main/images/scissors_predicts_scissors.jpg)
![rock_predicts_rock2](https://github.com/chrispmaag/flask_with_tensorflow_lite/blob/main/images/rock_predicts_rock2.jpg)