# Which Source is Driving Methane Spikes by Region?
### Project purpose
 The purpose of this project was to clean and analyze a dataset showing the amount of carbon emissions released by each country, determine the highest and lowest producers, and then come up with possibilities as to what is causing the highest emissions. 

### Why?
I decided to start my first analysis project by researching a topic I am passionate about-carbon emissions. Carbon emissions is the greatest contributor to climate change caused by human activities, and reducing the amount of fossil fuels we as a population are emitting is the only way to protect our environment. 

### Installation and Libraries
The only library needed to execute this code is Pandas. When trying to run the command 'read_excel' after installing Pandas, I was encountering an issue. I kept getting this code:

AttributeError: module 'pandas' has no attribute 'read_excel'

This was because Pandas was not installed correctly. To fix this I installed this in the terminal: 

pip3 install --upgrade pandas openpyxl

Another issue that I was facing was that the code was not running when using the run in vscode, if this occurs, ensure you are using the Python selector SHIFT + CMD + P to open the command drop list and select Python Selector. 

### Project Findings
After analyzing the dataset, there were some notable findings which will be discussed below:
The country with the lowest carbon emissions was Niue with an average of 0.00164 million tonnes of carbon per year. Niue is a small island nation in the South Pacific Ocean, with a population of roughly 1,500 people. Niue having the lowest carbon emissions makes sense due to the small population and limited industrial activity on the island. 
The country with the highest emissions is China, with an average of 2326 million tonnes of carbon per year. China ranks second in the world with the highest population, and with its large population, extensive manufacturing, and high energy demand all contribute to its high emission production. 
At the end of this project, I included some data visualizations. The first two visualizations are simple and show the top 5 highest emmitting countries, as well as the bottom 5 lowest emmitting countries. The next two visualizations include a box plot showing the top 5 and bottom 5 countries.