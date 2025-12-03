# Which Source is Driving Methane Spikes by Region?
### Project purpose
 The purpose of this project was to clean and analyze a dataset showing the amount of carbon emissions released by each country, determine the highest and lowest producers, and then come up with possibilities as to what is causing the highest emissions. 

### Why?
I decided to start my first analysis project by researching a topic I am passionate about-carbon emissions. Carbon emissions is the greatest contributor to climate change caused by human activities, and reducing the amount of fossil fuels we as a population are eitting is the only way to protect our environment. 

### Project Findings

### Installation and Libraries
The only library needed to execute this code is Pandas. When trying to run the command 'read_excel' after installing Pandas, I was encountering an issue. I kept getting this code:

AttributeError: module 'pandas' has no attribute 'read_excel'

This was because Pandas was not installed correctly. To fix this I installed this in the terminal: 

pip3 install --upgrade pandas openpyxl

Another issue that I was facing was that the code was not running when using the run in vscode, if this occurs, ensure you are using the Python selector SHIFT + CMD + P to open the command drop list and select Python Selector. 