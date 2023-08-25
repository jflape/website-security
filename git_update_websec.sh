#!/bin/sh
reponame="website-security"
home_dir=/usr/local/src
git_dir=$home_dir/repository
#file=$home_dir/repolist.txt
comments="$(date +%d%b%y)"
#while read -r reponame;
#do
    echo "*****Updating Repository $reponame*****"
    cd $git_dir/$reponame
    git branch -M main
    git add . 
    git commit -a -m "$comments"
    git push origin main
    echo "*****Repository $reponame Updated*****"
#done < "$file"
