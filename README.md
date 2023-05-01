# SCDV490-FinalProject-BlakeRivers

## Description
Blake Rivers' Final Project for SCDV490.  Focusing on United States Census Data through the years.
Looking at the change in different demographics of states over the years and some of the causes behind those changes.

#### Plans of Project are to:
- Look at the Change in Population vs Change In Income by State 
- Find clusters of states that are similiar to each other
- Do a clustering algorithm on them that clusters similiar ones together
- Talk about the states that get clustered together and similarites between them



## Where to access Data
### These Datasets are also located within this repository in the [Data Sets Folder](https://github.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/tree/main/Data%20Sets)

#### Original Data Files
This is the dataset I used for my midterm project that started the questions for this project:


*The URL to access the dataset*:
[Click Here For Midterm Dataset](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/county_census_and_election_result.csv)

*The URL to access the Meta Data about this dataset*:
[Click Here For Meta Data](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/county_census_election_results_META_DATA.csv)



#### New Census Data Files
*Link to US Census Bureau Datasets*:
[Click Here For Census Bureau](https://data.census.gov/)


*The URL to access 2000 Income Data*:
[Click Here For 2000 Income](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/2000%20Income%20Cleaned.csv)


*The URL to access 2000 Population Data*:
[Click Here For 2000 Population](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/2000%20Population%20Cleaned.csv)


*The URL to access 2010 Income Data*:
[Click Here For 2010 Income](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/2010%20Income%20Cleaned.csv)


*The URL to access 2010 Population Data*:
[Click Here For 2010 Population](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/2010%20Population%20and%20Demographics%20Cleaned.csv)


*The URL to access 2020 Income Data*:
[Click Here For 2020 Income](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/2020%20Income%20Cleaned.csv)


*The URL to access 2020 Population Data*: 
[Click Here For 2020 Population](https://raw.githubusercontent.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers/main/Data%20Sets/2020%20Population%20and%20Demographics%20Cleaned.csv)




## How to Install 
### These installation instructions are for Windows users.  MAC users may need to find different ways.
#### To Download/Run Anaconda and Jupyter Lab
These are the applications I used to do this project.

To download Anaconda onto your local computer: [Click HERE](https://www.anaconda.com/products/distribution)

On the page, simply click "download" and once downloaded, open the file download, located at the bottom of your screen, and finish the setup process.  

Once completely downloaded, start up Anaconda and launch a Jupter Lab environment.

#### To Download Git Bash
To download Git Bash on your local computer: [Click HERE](https://gitforwindows.org/)

Once downloaded you are ready to use.


#### Cloning the Repository
To clone this repository and run for yourself:
1. Go to the [main page](https://github.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers) of this repository.
2. Click the green CODE button and you will see a unique URL.
3. Copy this URL into your Git Bash command promt using the line "git clone https://github.com/BlakeRivers25/SCDV490-FinalProject-BlakeRivers.git"
4. Once this is done, you should be able to locate this project folder withing the file directory in Jupyter Lab.





## How to Run Code

#### What Each File Is
*Data Sets:*  Holds the datasets that are used for this project.

*README.md:*  Explains what everything does and how it works.

*analysis.ipynb:*  Jupyter notebook that runs analysis on my datasets and creats graphs.

*bellis_analysis.ipynb:*  Jupyter notebook used by Dr. Bellis with helpful code examples to use/follow.

*test_cases.ipynb:*  Jupyter notebook that was used to test graphs and functions until they worked properly.

*utilities.py:*  Python file that holds functions to clean up datasets and convert State names to abbreviations.


#### Running the Analysis
Once the repository is cloned and open within a Jupyter Lab Environment:
1. Open analysis.ipynb
2. Simply run the code

The graphs and findings of this research should appear right there!

*A Quick Note :*
Each section of the project sits within its own markdown of code.  To view that section of code/analysis simply open up the section you want and run that section.



## Analysis/Findings

#### Analysis
1. Simple comparison graphs of value changes from 2010 - 2020
2. Performed clustering on 2020 Data
3. Perfromed clustering on 2010 - 2020 change in values data

#### Findings
Similiar States:
1. Arizona and Pennsylvania
2. Maine and Louisiana

Addional Findings:
1. States were similiar to each other in 2020
2. States had similiar changes to each other from 2010 - 2020
3. Population age range graphs so similarities with Arizona and Louisiana have more of a younger population and Pennsylvania and Maine having an older population.
