***********************Wikipedia Racer Instructions****************

Our code operates on any directory of html Wikipedia articles that link to each other.  Within the zip folder of the project, we provide a sample directory consisting of over 200 articles to test the code.  To run the code on all of Wikipedia, download a static HTML dump of the entire site and then merge any sub-directories into one directory.  While our program consists of a few files, the user only needs to work with find.py.  There are two ways of running our code.  

1) If the user just wants to perform BFS on two articles and find the shortest path, they simply need to run from the command line using two arguments, first of which is the starting article and the second is the destination article.  Note that the articles must be entered without their paths, with the correct capitalization, and with underscores where spaces should occur.  For example:

	./find.py United_kingdom Norway

This will return the results of the BFS and will show the shortest path between the two articles. 

2) If the user would like to see the analytics for the directory as well as the analytics for the two pages, the user needs to add a third argument, “-analytics.”  For example:

	./find.py United_kingdom Norway -analytics
	
This will return the same BFS results fore the two articles as well as analytics for the entire wiki directory.  The analytics include the most popular Wikipedia page, the center of Wikipedia, as well as the pages that reference the starting and ending Wikipedia articles (the first and second command line arguments).  

