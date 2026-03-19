an *OS* is called an operating system if it has a kernel and software, at least.

Linux is kernel,  it becomes an operating system when its added  with GNU.
Linux is ==a free, open-source operating system (OS) based on Unix==, designed by Linus Torvalds in 1991. It acts as the software layer managing hardware resources (memory, CPU, storage) for computers, servers, and devices. Known for security, stability, and flexibility, it powers nearly all supercomputers, most internet servers, and Android devices.
***Linux Kernel***
The Linux Kernel is the core part of the Linux operating system that connects software with hardware. It manages system resources and allows applications to function properly.
- The Linux Kernel acts as a bridge between hardware and software.
- It is open-source and freely available to everyone.
- It was developed by Linus Torvalds in 1991 as a personal project.
- Continuous community contributions made it powerful and popular.
##### Role of the Kernel in Resource Management
In a general-purpose computer, multiple processes run simultaneously. To manage these processes efficiently, a special software layer is required. This layer is known as the kernel.

- Allocates CPU time to processes
- Manages system memory
- Controls access to hardware devices
- Prevents conflicts between processes
- Provides virtual resources to applications
***what's shell?***
is a command line interpreter. it translates the commands entered by the user and converts them into a language that is understood by the Kernel.
there any many types of shells:
	SH
	ZSH
	FISH
	BASH ... and much more, around 500
they differ in coloring, piping, command compilation, etc. 
components of Linux:
***what's the difference between kernel and shell?***
The **kernel** is the core component of the operating system that directly manages hardware resources, while the **shell** is a user interface program that acts as a bridge between the user and the kernel.

Kernel vs. Shell

| Parameter       | Kernel                                                                | Shell                                                                           |
| --------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Function**    | Manages hardware and system resources like CPU, memory, and devices.  | Interprets user commands and sends requests to the kernel.                      |
| **Position**    | The innermost core layer of the operating system.                     | The outermost layer that the user interacts with.                               |
| **Interaction** | Interacts directly with the computer hardware.                        | Interacts with the user and then communicates with the kernel via system calls. |
| **Privilege**   | Runs in a privileged mode (kernel space) with complete system access. | Runs as a normal user program in user space.                                    |
| **Purpose**     | Makes the computer function by executing tasks at the hardware level. | Makes the computer usable for humans by providing an interface.                 |
| **Examples**    | Linux Kernel, Windows NT Kernel.                                      | Bash, Zsh, PowerShell (CLI shells).                                             |

How they work together
When a user types a command (e.g., `ls` to list files) into a terminal program: 
- The **terminal** sends the command to the **shell**.
- The **shell** interprets the command's syntax and translates it into system calls that the kernel can understand.
- The **kernel** receives the system calls, interacts with the hardware (e.g., the disk drive to fetch file information), and performs the requested task.
- The **kernel** then sends the result back to the **shell**, which formats the output and displays it in the terminal for the user to read

***Linux Architecture***

![[Pasted image 20260317173222.png]]

[more about linux](https://www.geeksforgeeks.org/linux-unix/introduction-to-linux-operating-system/)

Desktop environment
 *are the graphical interfaces that provide users with a visual way to interact with the operating system
### Linux Command Basics
syntax  ***command  -- option argument*** 
  *option* - additional settings they have
  *argument* - different inputs to have output  
  *commands* - small programs that do one task well
	  * ls {option}{file} 
		  *  -l (listed) ==used to display the contents of a directory in a long listing format==, which provides detailed information about each file and subdirectory. The output is presented in columns.
		  *  -a (hidden)  hidden file start with dot.
		  *  -filename
		  *  -R
	  * tree {folder}
	  * cd {directory}
		  * cd/  root
		  * cd    home
		  * cd..  1x back
		  * cd../..  2x back
	  * pwd {option} prints the path of the working directory
	  * echo {string} used to display line of text/string that are passed as an argument
		  * echo {text} > file.txt  output redirecting 
		  * echo {text} >> file.txt  append
	  * cat{file} show the content of a file right on the terminal below the command
	  * less{file} show the content of a file on new terminal
	  * head{file} display the first 10 lines of the file
	  * tail {file} display the last 10 lines of the file
	  * touch {file1}{file2}... creates any kind of file with empty inside
	  * mkdir {folder1}{folder2}...  make directory
		  * mkdir -p {folder1}/{folder2}
	  * clear
	  * rm {file1}{file2}...
		  * rm -r  recursive(4 folders)
		  * rm -i  for prompt(ask)
		  * rm -f  force delete
	 *  cp {oldFilePlace/name}{newFilePlace}
		 * cp -r   to copy folder which contains files 
	 * mv {oldFilePlace/name}{newFilePlace}  move a file to a directory
	 * mv {filename}{filename}  since the source and the destination are in the same directory, this action renames the file.
	 * mv {filename}{destination directory/newname}  a file moved and renamed simultaneously
	 * mv {directory/}{destination directory}  move a directory
	 * mv  {asterisk.fileformat} {destination directory}   this moves all files ending with the fileformat to the destination directory
	 * grep {options}{pattern}{files}   stands for global search for regular expression. Searches a file for a particular pattern of characters, and displays all lines that contain that pattern.
		 *  grep -i "search" file  case insensitive
		 *  grep -c "search" file   count number of lines on which the search is found
		 * grep - l "search" *   display file name
		 * grep  -r "search" foldername  search text in folders
		 * grep -v "term" filename   display without this term
		 * grep -n "term" file   display the line number the term is found on 
		 * grep -o "pattern" filename   display that specific word only
	  * wc {option}{filegrep} print newline, word, and byte counts for each file
		* wc -c  print the byte counts
		* wc  -l   print the newline counts
		* wc -w  print the word counts
	*multiple command executions*
		- And (&&)
		- Or(||)
		- Pipeing(|)  to use the output of the first command as an input for the second command
	   * Sed/ Stream Editor  sed{option} 'command' file
		   * substitute(replace): sed 's/old/new/' file (also 'S|old|new|' can be used). 's/old/new/g' to replace more than 1 time in one line
		   * sed '/pattern/d' file