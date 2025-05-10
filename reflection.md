# Reflection

Student Name:  kebatist
Student Email:  kebatist@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This project took me way longer than I wanted it to. First we started off by trying to use the iSchool APIs.That was not going well for me as my program was having trouble downloading the data and recognizing the path it needed to pull from. 

I decided to switch to the movies API. Originally I wanted to use a link and pull it like that but I could not find the element (h1, p) and there were too many movies with too many elements so I bagged that too. I found the same API on Kaggle which I already have an understanidng of and have used in the past. I downloaded the API to my computer adn directly to my PC and then I importedd it to my program. I actually used ChatGPT to figure this out since I found the directions on Kaggle unhelpful. 

Through this project, I widened my understanding of the data pipeline process because I used extracting and transforming data processes to build the the dashboard. I had previous experience with STreamlit which helped me in this course but after assignments 6 and 8 I felt way more comfortable writing a simple pipline to visualize the data I loaded. 

I also learned how to modularize Python code using functions and utility files. How to write simple unit tests using pytest. Working with Pandas, Matplotlib, and Seaborn helped me explore data visualization in a more physical. I also became more comfortable working with the file system and organizing a structured project with code/, cache/, and tests/ folders.

This was my first time writing tests by myself and I learned that once you have the functions written the tests are actually VERY simple to write and are simply a path that loads the data to check if it is there. The tests were one of the easier parts of tthis project which I was NOT expecting. 

I practiced modular programming, wrote and ran tests, and worked with libraries like pandas, matplotlib, and streamlit. 
*to be noted:*
I initially tried using relative imports, but ran into the ImportError: attempted relative import beyond top-level package. This led me to learn about modifying sys.path to ensure pytest could find and test utils.py. 

Most importantly, I learned how to troubleshoot common but confusing Python issues. Such as import paths and data file handling, which gave me more confidence working on real-world projects.

One major challenge was managing file paths and import errors. Especially making sure that my test files could correctly import functions from other modules like utils.py. I definitely spent mot of my time with this project on ensuring that all of my program were properly accepting the imports and data. I knew that msot of porgram would be unable to run if I could not extract the files from the zipped file. Despite it taking me a while, unzip.py was a small little program that I used CoPilot to write but it absolutely changed the game. 

Once the files were uploading I could continue to work on the dashbord which would visualize all the data.  It took some troubleshooting to understand how Python's import system works and how to correctly configure relative imports or adjust sys.path. The sys.path was somethign that I had to do some research on becuase we had not used it in class but I determined that by manually importing the path my program could reocngize the data without seaarching for a path in data/ or cache/ that was unavailable. 

I also encountered issues with Streamlit throwing warnings and had to learn to distinguish between critical errors and harmless ones. There was a run issue that is cuased by the overdrive to streamlit programs. I used CoPilot to explain that to me and it was helpful because it showed that my program was going to continue to run its slider, histogram, and ranking in dashboard.py depsite the program itself having a lot of calls coming towards it.

I would spend more time customizing the visualizations and improving the user interface of the dashboard. I would also add more robust error handling and allow the user to dynamically upload their own dataset via Streamlit. More tests would help catch edge cases, especially around file handling and data transformation.

