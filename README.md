These are few scripts used in Kaggle competition - https://www.kaggle.com/c/datasciencebowl

* Resize all image to 48 X 48 and create augmented train - with rotation, flip, introduce noise and transforms.
```
mkdir /home/cxxnet/example/kaggle_bowl/data
python gen_train.py /home/data/bowl/train/ /home/cxxnet/example/kaggle_bowl/data/train/
python gen_test.py /home/data/bowl/test/ /home/cxxnet/example/kaggle_bowl/data/test/
```

* Generate img list
```
python gen_img_list.py train /home/data/bowl/sampleSubmission.csv data/train/ train.lst
python gen_img_list.py test /home/data/bowl/sampleSubmission.csv data/test/ test.lst
```

* Generate binary image file
First build im2bin at ```../../tools```, then run
```
../../tools/im2bin train.lst ./ train.bin
../../tools/im2bin test.lst ./ test.bin
```

* Run CXXNET
```
mkdir models
../../bin/cxxnet bowl.conf
```
It take 2+ days to train on your PC without GPU

* Run Prediction
```
../../bin/cxxnet pred.conf
```
It will write softmax result in test.txt

* Make a submission file

```
python make_submission.py /home/data/bowl/sampleSubmission.csv test.lst test.txt out.csv
```

* Submit out.csv

* Change parameters of training, form an ensemble to get better results.

