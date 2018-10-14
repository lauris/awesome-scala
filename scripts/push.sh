#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git config core.filemode false # ignore chmod changes
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-repo https://${GITHUB_TOKEN}@github.com/sake92/awesome-scala.git > /dev/null 2>&1
  git push --quiet origin-repo HEAD:$TRAVIS_BRANCH
}

setup_git
commit_files
upload_files
