# Which Source is Driving Methane Spikes by Region?
### Project purpose
 The purpose of this project was to clean and analyze a dataset showing the amount of carbon emissions released by each country, determine the highest and lowest producers, and then come up with possibilities as to what is causing the highest emissions. 

### Why?
I decided to start my first data analysis project by researching a topic I am passionate about: carbon emissions and their contribution to climate change. Climate change is one of the greatest environmental challenges facing our planet, and the burning of fossil fuels is a major source of human-caused greenhouse gas emissions. Understanding how emissions vary between countries and over time is important for identifying trends, recognizing where the greatest sources of emissions are coming from, and understanding the progress being made toward reducing them.

### Installation and Libraries
The only library needed to execute this code is Pandas. When trying to run the command 'read_excel' after installing Pandas, I was encountering an issue. I kept getting this code:

AttributeError: module 'pandas' has no attribute 'read_excel'

This was because Pandas was not installed correctly. To fix this I installed this in the terminal: 

pip3 install --upgrade pandas openpyxl

Another issue that I was facing was that the code was not running when using the run in vscode, if this occurs, ensure you are using the Python selector SHIFT + CMD + P to open the command drop list and select Python Selector. 

### Project Findings
After analyzing the dataset, there were some notable findings which will be discussed below:

The country with the lowest carbon emissions was Niue, with an average of 0.00164 million tonnes of carbon per year. Niue is a small island nation in the South Pacific Ocean, with a population of roughly 1,500 people. Niue having the lowest carbon emissions makes sense due to the small population and limited industrial activity on the island. 

The country with the highest emissions is China, with an average of 2326 million tonnes of carbon per year. China ranks second in the world with the highest population, and with its large population, extensive manufacturing, and high energy demand, this contributes to its high emission production. 

At the end of this project, I included some data visualizations. The first two visualizations are simple and show the top 5 highest emitting countries, as well as the bottom 5 lowest emitting countries. The next two visualizations include a box plot showing the top 5 and bottom 5 countries. These visualizations are rather simple, and were mainly used to familiarize myself with creating graphs and understanding the coding needed to make them aesthetically pleasing.
