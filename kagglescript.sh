mkdir /home/cxxnet/kaggle_bowl/data

#generate images from train data
python gen_train.py /home/data/bowl/train /home/cxxnet/kaggle_bowl/data/train/
python gen_test.py /home/data/bowl/test /home/cxxnet/kaggle_bowl/data/test/

python gen_img_list.py train sampleSubmission.csv data/train/ train.lst
python gen_img_list.py test sampleSubmission.csv data/test/ test.lst

../../tools/im2bin train.lst ./ train.bin                               
../../tools/im2bin test.lst ./ test.bin

mkdir models
../../bin/cxxnet bowl.conf
../../bin/cxxnet pred.conf

python make_submission.py sampleSubmission.csv test.lst test.txt out.csv

gzip out.csv
