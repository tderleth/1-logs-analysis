# Project: Logs Analyses

This repo is part of a series of project belonging to my [Full Stack Web Developer Nanodegree](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004). Purpose of this lesson is to master SQL databases and build multi-user web applications using the Flask framework, SQLAlchemy, and authentication providers such as Google and Facebook.

## Installation

The project uses [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [vagrant](https://www.vagrantup.com/) as development environment. For more info on setup look into the [VM configuration](/Vagrantfile). To get the VM up and running you need to have both tools (vortualbox and vagrant) installed on your computer. 

1.  `git clone git@github.com:tderleth/1-logs-analysis.git`
2.  `cd 1-logs-analysis`
3.  `vagrant up && vagrant ssh`
4.  Within the VM run `sudo pip install termcolor` (adds a package to easily highlight shell output)

## Import data

In order to use the tool you need to import the data into the VM database. Unzip the [data file](/newsdata.sql.zip) and run `psql -d news -f newsdata.sql` inside your vagrant machine. 

## Usage

After performing all previous steps you can interact with the analysis tool. You have the following options (first make sure that your pwd is `/vagrant`):

-   `python logs.py articles` - What are the three most popular three articles of all time?
-   `python logs.py authors` - Who are the most popular article authors of all time?
-   `python logs.py errors` - On which days did more than 1% of requests lead to errors?
-   `python logs.py all` - Dumps all statistics to all above listed methods

## References

[VM configuration](/Vagrantfile) duplicate of [udacity/fullstack-nanodegree-vm/](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)

## Dependencies

[psycopg2](http://initd.org/psycopg/), [sys](https://docs.python.org/2/library/sys.html), [colored](https://pypi.org/project/colored/)

## Maintainer

-   [Thomas Derleth](mailto:thomas.derleth@moovel.com)
