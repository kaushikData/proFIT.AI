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

## Online Demo:
http://www.profilefitprediction.me:8000/

## Minimal Start:

1. Export Flask
```bash
export FLASK_APP=server.py
```

2. Run the Flask Server
```bash
flask run
```

3. The App is now runninng on localhost.

## From Scratch

1. Data Collection