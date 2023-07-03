#!/bin/sh
reponame="website-security"
home_dir=/usr/local/src
git_dir=$home_dir/gitrepos
#file=$home_dir/repolist.txt
comments="$(date +%d%b%y)"
#while read -r reponame;
#do
    echo "*****Updating $reponame from server to git*****"
    cd $git_dir/$reponame
    git add . 
    git commit -a -m "$comments"
    git push origin main
#done < "$file"
