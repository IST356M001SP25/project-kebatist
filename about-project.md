# About My Project

Student Name:  Katharine Batista
Student Email:  kebatist@syr.edu

### What it does
My project shows the top 250 movies in the last 100 years. The dataset is dervived from Kaggle.

### How you run my project
Run everything in this order  IN THE TERMINAL. You may run into errors if you do not run things in the terminal
First, ensure that the exmaple tests pass. If they do not make sure eeverything is downloaded correctly. 

THEN BEGIN:
1. python code/extract.py This will extract the necessary files. 
    YOU SHOULD SEE THIS IN TERMINAL:
    ✅ Loaded 250 records from data\IMDB Top 250 Movies.csv
    ✅ Saved 250 items to cache\raw_data.json
    1a. python code/unzip.py. *There should be an unzipped file. cache/clean_data.csv and raw_data.json important to run before you process any data*
2. python code/transform.py this will scrape the data 
    *Cleans and formats the data for analysis and visualization*
    YOU SHOULD SEE THIS IN TERMINAL:
    Transformed data saved to cache\clean_data.csv
    rank                      name  ...             directors                                          writers
    0     1  The Shawshank Redemption  ...        Frank Darabont                      Stephen King,Frank Darabont      
    1     2             The Godfather  ...  Francis Ford Coppola                  Mario Puzo,Francis Ford Coppola      
    2     3           The Dark Knight  ...     Christopher Nolan  Jonathan Nolan,Christopher Nolan,David S. Goyer      
    3     4     The Godfather Part II  ...  Francis Ford Coppola                  Francis Ford Coppola,Mario Puzo      
    4     5              12 Angry Men  ...          Sidney Lumet                                    Reginald Rose      

    [5 rows x 13 columns]
3. python code/check_columns.py to ensure that the data is being displayed correctly. 
    Columns: ['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time', 'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers']
4. streamlit run code/dashboard.py to run the dashboard and see how I made a visualization with streamlit. 
    YOU SHOULD SEE THIS:
    A histo plot vis, slider, and top 10 movies. 
5. No need to run app.py (tester) or utils.py (a vessel for all other programs)

Run the tests. The examples tests are tests that should pass with no issues. 

Go right into the test column or into the code to run these tests. Once you do everything above you should pass all the tests necesssary. If you do not you will know that something went wrong with downloading the data. If this should happen, please attempt to reclean and process the data!

### Other things you need to know
PLEASE READ THIS FIRST NOTHING WILL RUN WITHOUT THIS!!!
 
Download the pip dependencies: uv pip install -r requirements.txt

THERE IS A CHANCE THIS WONT BE NEEDED!
You may have to create a Kaggle API. For this you can create an account with Google, go to settings and find the API activation feature. Activate it and download it to your machine. 

Ensuring that it is under My PC/ [username]/ .kaggle/ kaggle.json
This will contain your information! In terminal, type in pip install kaggle to download it.
If you open up that json file you can view your username and KEY. 

TYPE THIS INTO THE TERMINAL TO CHECK EVERYTHING IS WORKING WITH YOUR FILE.
set KAGGLE_USERNAME= username
set KAGGLE_KEY= key
