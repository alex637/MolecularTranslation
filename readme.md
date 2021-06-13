# My Data Science project
Kaggle competition: https://www.kaggle.com/c/bms-molecular-translation

Short version: a very large train dataset is given which contains monochromatic differently-sized images of chemical (structural) formulae and their InChI (**In**ternational **Ch**emical **I**dentifier) strings. The goal is to train your model to generate an accurate InChI string for the image input.

Metric: Levenshtein distance (mean across predictions).

Best ideas can be found in the notebooks.

## Pretraining CNN.
Notebooks for pretraining CNN (possibly, ResNet) on a relatively simple regression task: predicting number of atoms in the molecule. Two options: regression on C counts and multiple target regression on the counts of 6 frequently found atoms. It turned out that a more complex encoder is necessary for accurate encoder-decoder predictions.

1. pretrain_regression $-$ first results, train_test_split, auxiliary materials.
2. pretrain_regression_C $-$ a neater notebook with C regression.
3. pretrain_regression_multiple $-$ a neater notebook with multiple targets regression.
4. pretrain-regression-multiple $-$ notebook from Kaggle (with actual computations).
5. compute_number_of_atoms.py $-$ python3 script for computing number of atoms from InChI strings. H atoms may not be computed accurately due to the InChI representaion. Uses RDKit module which has to be installed.

## Encoder-Decoder architecture.

1. prepare_decoder $-$ first results, train_test_split, auxiliary materials.
2. prepare_decoder_v2 $-$ a neater version to run.
3. inference_encoder_decoder $-$ inference notebook (actual inference notebooks were run on Kaggle).
4. decoder-kaggle-1 $-$ training encoder-decoder model, notebook downloaded from Kaggle, version 1.
5. ResNet.py $-$ ResNet architecture. Largely based on https://github.com/JayPatwardhan/ResNet-PyTorch.

## Other notebooks

1. getting_to_know_the_dataset $-$ getting familiar with the problem.
2. basic $-$ several submissions, including those from train dataset similar to test based on CNN encoder results.