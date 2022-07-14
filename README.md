# Selenium-Intro

## Description
- Two web scraping scripts.
 1. github_webscraper.py Opens the provided github repository link and saves the Names of the repos and Languages used to a .json file 
 2. scrungy_cats.py Opens a subreddit and downloads all images from the top posts until reddit stops displaying results.

Ended up installing 952 cat photos in 10 minutes. Could be repurposed to download photos from many different subreddits. Eventually will try to pull videos as well.

## Start App

Install PIP, Python 3, Google Chrome

The chromium driver is encapsulated within runtime to avoid manual setup.

Step 1) Create Virtual Environment:

    (Windows Shell)                 >>> cd ~\SeleniumProject
    (Windows Shell)                 >>> py -m venv .venv

Step 2) Activate Virtual Environment:

    (Windows Shell)                 >>> .\venv\Scripts\activate

Step 3) Install Requirements:

    (Windows Shell)                 >>> pip install -r requirements.txt

Step 4) Run Program

    (Windows Shell)                 >>> py github_webscraper.py OR py scrungy_cats.py
    
