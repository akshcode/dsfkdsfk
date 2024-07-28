1)git --version (to check the version of git)

2)git config --global user.name "<username>"
3)git config --global user.email <email> (to configure the git)

4)git config --list (to check what are the config username and email)


5)git init (to start git tracking in a folder)

6)git add <file_name> 
git add main.py (to start tracking a file, this is now the staging area)

or you can do
git add -A  (to add to the staging area all files together)

7) Do not do init if you have all already cloned it from somewhere

8) From the staging area you can commit, 

for the first time, you have to do
git commit

opens a editor for you

press i

type the message

kfkjfkldsjklfjds

press escape and then :wq to exit

9) git status (to check the status)

10) agar app staging area me daalne ke baad changes krte ho toh firse add kro usko staging area mein

11) When we want to commit for the second time, we can directly do like

git commit -m "message>

12) clear (to clear the terminal)

13) How to checkout or bring your files to the last commit, lets say khraab ho gya

git checkout <filename>

or

git checkout -f (for all the files to be together)

 14)  git log (to show what are the commits that you did)

15) git log -p -1 (to see only the last commit) q to quit

16) git diff --staged (to compare staging area to the last commit)

17) How to directly commit without adding to the staging area, should be discouraged

git commit -a -m "<message>"

18) ls (to list all the files)

19) git rm --cached <filename> (to remove from the staging area)

or 

git rm <filename> (to delete the file, after adding to the staging area, waapis ni aata bhai ye git checkout se)

20)  git status -s (to check kahan hai vo modified) jo hara wala M hota hai that is staging area wala modified or doosra wala working directory

21) touch .gitignore (to make a gitignore file to ignore some files)

BRANCHESSSSSSSSSSSSSSSSSSSSSSSSSs

22) How to make a new branch 

git branch <branchname>

23) How to check on which branch you are or how many branches are there

git branch

24) How to change to another branch

git checkout <branchname> 

Now work here and you can do the changes

25) How to merge, first come into the master branch and then do

git merge <mybranch> (this will merge all the changes to the main branch)

26) After cloning a repo, go the main branch and then create a new branch

git branch <branchname>

git checkout <brachname> (to switch to that branch)



and then do stage pull push from there only
