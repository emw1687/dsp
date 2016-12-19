# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. `pushd [path]` add path to top of directory list and navigate to path
2. `pushd` navigate back to last path pushed (at top of directory stack)
3. `popd` move to last path pushed, but also remove that path from directory stack
4. `touch [filename]` make a new empty file
5. `cp [originalfilename][copyfilename]` copy a file
6. `cp -r [originaldirectoryname] [copydirectoryname]` copy a directory and its contents
7. `less [filename]` displays (paginated) file on screen
8. `rm [filename]` removes a file
9. `rm -r [directoryname]` removes a directory and all of its files (recursively)
10. `[command]|[command]` executes command on left and sends output to command on right (can be used to combine commands)

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * `ls` displays visible files in current working directory as bare format list
* `ls -a` displays visible and hidden (all) files in current working directory as bare format list
* `ls -l` displays visible files in current working directory as long format list
* `ls -lh` displays visible files in current working directory as long format list with units on file sizes
* `ls -lah` displays all files in current working directory as long format list with units on files sizes
* `ls -t` displays visible files in current working directory in descending order of time created
* `ls -Glp` displays visible files in current working directory as long format list with colors and indicators for different file types

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 1. `-1` to display each item in the list on its own line
2. `-m` to display as a comma-separated list
3. `-d` to display just directories
4. `-u` to display in descending order of last time accessed
5. `-r` to dislay in reverse (i.e. `-ur` to display in ascending order of last time accessed)

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` executes a command or commands on a list of arguments, which are created through standard input or piped from other commands (i.e. using `|`). For example, `find \temp . -name "*.txt" | xargs rm -rf ` could be used first to generate a list of all .txt files in the temp directory, and the pipe the output to xargs which would delete each file in the list.

 

