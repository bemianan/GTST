### Vim
  is a command line text editor.
  *vim filename.txt* -- to open file
  From **normal mode** to 
  - **insert mode** --- i,  you can only insert text
  - to **command mode** ---esc, save, save and quit, force quit and save, undo, execute bash commands
	  - :w---save
	  - :q---quit
	  - :wq---save and quit
	  - :wq!---force quit and save
	  - :u---undo
	  - :%! command---execute command
- **visual mode**
		*first enter to command mode*
		-  v --character-wise selection
		- shift+v -- line-wise selection
		- cntr+v or cntr+q --block-wise selection
		- y-- yank(copy)
		- d--delete
		- p--paste
### Nano
is also a command line text editor, but much more easier than vim.
- nano filename.txt -- to open a file with nano 
- cntrl+s -- save
- cntrl+x -- exit
- alt+u -- undo
- cntrl+shift+v -- paste
- alt+e -- redo
- cntrl+T -- to execute command
- cntrl+r --  to append text from other text files to the current file opened with nano
