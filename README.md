# Profile Fit Prediction using Transfer Learning
proFIT.AI is a product that can be used by recruiters to find the ideal candidates for their company.

## Preparing an environment to run the code:

1. Install Anaconda or Miniconda Package Manager from [here](https://www.anaconda.com/products/individual)
2. Create a new virtual environment and install the required packages:
```bash
conda create -n profile_fit_prediction python
```
```bash
conda activate profile_fit_prediction
```
If using cuda:
```bash
conda install pytorch cudatoolkit=10.0 -c pytorch
```
3. Install all requirements
```bash
pip install -r requirements.txt 
```