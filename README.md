# Project: Logs Analyses

This repo is part of a series of project belonging to my [Full Stack Web Developer Nanodegree](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004). Purpose of this lesson is to master SQL databases and build multi-user web applications using the Flask framework, SQLAlchemy, and authentication providers such as Google and Facebook.

## Installation

The project uses [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [vagrant](https://www.vagrantup.com/) as development environment. For more info on setup look into the [VM configuration](/Vagrantfile). To get the VM up and running you need to have both tools (vortualbox and vagrant) installed on your computer. 

1.  `git clone git@github.com:tderleth/1-logs-analysis.git`
2.  `cd 1-logs-analysis`
3.  `vagrant up && vagrant ssh`

## Usage

### Import data

In order to use the tool you need to import the data into the VM database. Unzip the [data file](/newsdata.sql.zip) and run `psql -d news -f newsdata.sql` inside your vagrant machine. 

## Maintainer

-   [Thomas Derleth](mailto:thomas.derleth@moovel.com)
