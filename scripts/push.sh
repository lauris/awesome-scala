#!/bin/sh

setup_git() {
  git config --local user.email "travis@travis-ci.org"
  git config --local user.name "Travis CI"
}

commit_files() {
  git checkout master
  git add README.md
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-pages https://${GITHUB_TOKEN}@github.com/MVSE-outreach/resources.git > /dev/null 2>&1
  git push --quiet master
}

setup_git
commit_files
upload_files