To load the graphs and tables, please locate the "new" data sources when prompted for "nibrs ..." excel sheets. They
are the cleaned tables located within the zip file with the corresponding year. I have attached the extracted data given
by Tableau in case that does not work. You can find this within the zip folder.

There may be an error with the state not being in the table, just remove that as it does not affect anything.

All final visualizations are located on the last tab, the story tab called "Crime Distribution Analysis".

In my Tableau visualization, I wanted to analyze the density of different types of crime within the United States.
Initially, I wanted to specify each of the different types of crimes listed in the FBI's NIBRS dataset, but
I felt that it would look sloppy, so I decided on their more broad categories ("Crimes against Violence, Property,
and Society") listed in their dataset.


I decided to compare the NIBRS dataset for 2020 and 2012 and compare the difference in distribution between them.




US Graph
--------------------
There are two sets, 2020 and 2012 and share similar colors for their legend. I wanted to show the distribution of 
different types of crimes across the US and the difference between 2020 and 2012.

Scatterplots
---------------------
I wanted to show the change in amounts of crime by type and show any outliers that we may want to look into more.
Green to Red gradient indicates higher crime rates in that area in 2012.

The 2nd scatterplot has the same concept as earlier, except instead we plot the ratio of type of crime to the total
offenses committed in that area.