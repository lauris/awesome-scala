#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# by Erik Osheim
#
# Reads README.md, and writes a README.md.new. If the format of
# README.md changes, this script may need modifications.
#
# Currently it rewrites each section, doing the following:
#  1. alphabetizing
#  2. querying GitHub for stars and days since active
#  3. formatting the link title to show this info
#  4. bolding projects with lots of stars
#
# Once README.md has the stars/days info in the links, the
# repo_regex will need slight modification.
#
# In order to use GH authentication, create a file in this directory
# called .access-token, whose contents are: "$user:$token" where $user
# is your github username, and $token is a Personal Access Token.

import base64
import datetime
import json
import os.path
import random
import re
import shutil
import sys
import urllib2

# we use these regexes when "parsing" README.md
empty_regex = re.compile(r"^ *\n$")
section_regex = re.compile(r"^## (.+)\n$")
repo_regex = re.compile(r"^\* (?:\*\*)?\[?([^*★]+[^ ★])(?: ★ ([^ ]+) ⧗ ([^ *]+))?\]\((.+?)\)(?:\*\*)?(?: (?:-|—|–) (.+))?\n$")
end_regex = re.compile(r"^# .+\n$")
github_regex = re.compile(r"^https://github.com/(.+?)/(.+?)(?:/?)$")

# some paths
readme_path = 'README.md'
temp_path = 'README.md.new'

# these will be updated if .access-token exists.
user = None
token = None

# use fake to avoid hitting github API
fake = True

# whether to query all projects, or just those lacking scores/days.
full_update = False

# right now.
now = datetime.datetime.now()

# ask github for the number of stargazers, and days since last
# activity, for the given github project.
def query(owner, name):
    if fake:
        print '    {0}/{1}: ok'.format(owner, name)
        return (random.randint(1, 1000), random.randint(1, 300))
    else:
        try:
            req = urllib2.Request('https://api.github.com/repos/{0}/{1}'.format(owner, name))
            if user is not None and token is not None:
                b64 = base64.encodestring('{0}:{1}'.format(user, token)).replace('\n', '')
                req.add_header("Authorization", "Basic {0}".format(b64))
            u = urllib2.urlopen(req)
            j = json.load(u)
            t = datetime.datetime.strptime(j['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            days = max(int((now - t).days), 0)
            print '    {0}/{1}: ok'.format(owner, name)
            return (int(j['stargazers_count']), days)
        except urllib2.HTTPError, e:
            print '    {0}/{1}: FAILED'.format(owner, name)
            return (None, None)

def output_repo(outf, name, stars, days, link, rdesc):
    popular = stars is not None and int(stars) >= 500
    if stars is None and days is None:
        title = name
    else:
        title = '%s ★ %s ⧗ %s' % (name, stars, days)
    if popular:
        outf.write('* **[{0}]({1})** - {2}\n'.format(title, link, rdesc))
    else:
        outf.write('* [{0}]({1}) - {2}\n'.format(title, link, rdesc))

def flush_section(outf, section, sdesc, repos):
    print '  ' + section.strip()
    outf.write(section)
    outf.write('\n')
    if sdesc:
        outf.write(sdesc)
        outf.write('\n')
    repos.sort(key=lambda t: t[0].lower())
    for name, stars, days, link, rdesc in repos:
        if not full_update and stars is not None and days is not None:
            output_repo(outf, name, stars, days, link, rdesc)
            continue

        m = github_regex.match(link)
        if not m:
            print '    {0}: not a repo'.format(link)
            output_repo(outf, name, stars, days, link, rdesc)
            continue

        stars, days = query(m.group(1), m.group(2))
        output_repo(outf, name, stars, days, link, rdesc)
    outf.write('\n')

def run():
    if full_update:
        print 'querying for all entries'
    else:
        print 'querying for new entries only'

    if fake:
        print 'running in fake mode -- no GH queries will be made'

    if os.path.exists('.access-token'):
        global user, token
        user, token = open('.access-token').read().strip().split(':')
        print 'using Personal Access Token {0}:{1}'.format(user, token)
    else:
        print 'no Personal Access Token found in .access-token'

    inf = open(readme_path, 'r')
    lines = list(inf)
    inf.close()
    print 'read {0}'.format(readme_path)

    started = False
    finished = False
    section = None
    sdesc = None
    repos = []
    outf = open(temp_path, 'w')

    total_repos = 0

    print 'writing {0}'.format(temp_path)
    for line in lines:
        if finished:
            outf.write(line)
        elif started:
            if end_regex.match(line):
                total_repos += len(repos)
                flush_section(outf, section, sdesc, repos)
                outf.write(line)
                finished = True
            elif empty_regex.match(line):
                continue
            elif section_regex.match(line):
                total_repos += len(repos)
                flush_section(outf, section, sdesc, repos)
                section = line
                sdesc = None
                repos = []
            else:
                m = repo_regex.match(line)
                if m:
                    name, stars, days, link, rdesc = m.groups()
                    repos.append((name, stars, days, link, rdesc))
                elif sdesc is None:
                    sdesc = line
                else:
                    raise Exception("cannot parse {0}".format(line))
        else:
            if section_regex.match(line):
                section = line
                started = True
            else:
                outf.write(line)
    outf.close()
    print 'wrote {0} repos to {1}'.format(total_repos, temp_path)

    print 'moving {0} to {1}'.format(temp_path, readme_path)
    shutil.move(temp_path, readme_path)

if __name__ == "__main__":
    #global fake, full_update

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-f", "--fake", action="store_true", dest="fake",
                      default=False, help="don't query github, use fake data")
    parser.add_option("-u", "--update", action="store_true", dest="update",
                      default=False, help="update all entries to newest data")

    opts, _ = parser.parse_args()
    fake = opts.fake
    full_update = opts.update
    run()
