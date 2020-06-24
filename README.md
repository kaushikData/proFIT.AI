# Profile Fit Prediction : With better PROfile FIT, comes better PROFIT

## MOTIVATION
Screening resumes plays a crucial part in hiring the right talent for an organization. However, this process is laborious and so the organizations use automatic screening systems for filtering resumes which are often inaccurate. 62% of recruiters admit that qualified candidates are overlooked by current resume screening systems
There are many limitations in the current systems:

1. Current systems are naïve because they look for the exact keyword from the job description in resumes for filtering candidates.
2. Current systems are ambiguous as they don't capture the context of keywords.
3. Candidates can easily trick the current systems by adding important keywords from job descriptions to their resumes.

After researching about these screening systems and talking to some recruiter, I came up with a pipeline and built a tool for recruiters to overcome the limitations of the existing resume screening systems.  

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
3. clone the repository and change directory to downloaded repo

4. Install all requirements
```bash
pip install -r requirements.txt 
```

## Web App:
http://www.profilefitprediction.me:8000/

## Minimal Start:

1. Navigate to Source directory 
```bash
cd source
```

2. Download trained BERT model (~0.5 GB) 
```bash
https://drive.google.com/drive/folders/1M_LQEbf7POiRAibYDB25y1dNefcspH2C?usp=sharing
```

3. Run the Flask Server
```bash
python server.py
```

## From Scratch

1. Data Collection