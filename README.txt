Created by Logan Walls

Installation Instructions
---------------------------
1. Install pymssql
	To do this, enter the following into your terminal:

		sudo pip install mssql

2. Run uSQL.py from the terminal
	To do this, type 'python' (without the quotes) into your terminal and then drag uSQL.py to the terminal and press enter.

	***If you get a 'file not found' error, make sure there is no trailing space after the text that appears when you drag the file to the terminal.***


Usage
--------------------------
-To execute multiple queries in the same file, seperate each query with three dashes '---' in your file.
-You can drag an SQL file into the terminal and press enter rather than typing out the path.


Known Issues
--------------------------
-If you SELECT a large number of columns the text will wrap around and the output can be
 difficult to read. Until a programatic solution is implemented you can fix this by resizing your terminal window.