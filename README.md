<h1>CV_Project</h1>
<b>Project name: </b>Re-thinking Face Detection<br>

<h2>The Dataset</h2>
The dataset used for this project is from github user X-zhangyang's <a href='https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset'>Real-World-Masked-Face-Dataset</a> repository.<br> 
Precisely, this one -> <a href='https://drive.google.com/open?id=1UlOk6EtiaXTHylRUx2mySgvJX9ycoeBp'>Click for the dataset</a> <- 
<br>
<br>

The dataset offers 90,000 face images without masks, 2203 face images with masks. In order to balance the mask/no_mask ratio and eliminate memory issues, we randomly removed 87,800 face images without masks. Then we trained the model on the remaining 4383 images for mask - no_mask classification.
<br>

<br>

<h2>Information About the Files</h2>

<strong>train_mask_detection_model.ipynb: </strong> The notebook we used to train our model.
<br>
<strong>detect_mask_on_image.ipynb: </strong> The notebook we tested our model on images.
<br>
<strong>detect_mask_on_video.ipynb: </strong> The notebook we tested our model on the live video captured by our webcams. 
<br>
<strong>remove_images_from_dataset.py: </strong> We had issues with memory on the training the full <a href='https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset'>Real-World-Masked-Face-Dataset</a>, hence, we used this method to randomly remove image files from the dataset. 
<br>
<strong>self-built-masked-face-recognition-dataset.zip: </strong> The dataset we used for the training the model. It's derived from the <a href='https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset'>Real-World-Masked-Face-Dataset,</a> with the usage of <i>remove_images_from_dataset.py</i>.
<br>

<strong>CV_Project_Report.pdf: </strong> Our report can be found in the folder <strong><i>"project_report"</i></strong>.
<br>

<strong>Note: </strong> All the sources we used building this project, weather it's for the code or the report, can be found on the <strong><i>"References"</i></strong> part of our report.