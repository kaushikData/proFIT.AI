# Profile Fit Prediction 
        -With better PROfile FIT, comes better PROFIT

## MOTIVATION
Screening resumes plays a crucial part in hiring the right talent for an organization. However, this process is laborious and so the organizations use automatic screening systems for filtering resumes which are often inaccurate. 62% of recruiters admit that qualified candidates are overlooked by current resume screening systems
There are many limitations in the current systems:

1. Current systems are naïve because they look for the exact keyword from the job description in resumes for filtering candidates.
2. Current systems are ambiguous as they don't capture the context of keywords.
3. Candidates can easily trick the current systems by adding important keywords from job descriptions to their resumes.

After researching about these screening systems and talking to some recruiter, I came up with a pipeline and built a tool for recruiters to overcome the limitations of the existing resume screening systems.  

## Web App:
http://www.profilefitprediction.me:8000/

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

Scraper to get candidates profile data from LinkedIn

(i) Notebook: LinkedIn_Data_Crawler.ipynb - Crawls user profile id from different roles (example: Data Scientist, Artist and Accountant etc.)

(ii) Once I scraped profiles, I used https://github.com/jvandenaardweg/linkedin-profile-scraper to get skills and experience from each user.

While crawling Data, I built role category tree

![Role Catehgory Tree] (https://drive.google.com/file/d/1MuRviD2TETBHsdDl9eHAqDyZW-T-fVSK/view?usp=sharing)

2. Data Modelling - Broad Role Classification

Notebook: Broad_Role_Classification_Using_Skills.ipynb

3. Data Modelling - Deep Role Classification

Notebook: Deep_Role_Classification_Using_Experience.ipynb

