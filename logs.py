#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import psycopg2
import sys
from termcolor import colored

DBNAME = "news"


def init(action=''):
    if action == 'authors':
        get_popular_authors()
    elif action == 'articles':
        get_popular_articles()
    elif action == 'errors':
        get_bad_devops_days()
    else:
        print colored("Pass an argument to the analysis tool:", 'red')   \
            + colored("\n - python logs.py authors", 'yellow') \
            + colored("\n - python logs.py articles", 'yellow') \
            + colored("\n - python logs.py errors", 'yellow')


"""
Task:       Which articles have been accessed the most?
Output:     Sorted list with the most popular article at the top.
Example:    Princess Shellfish Marries Prince Handsome — 1201 views
"""


def get_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT articles.title, count(*) as views
               FROM articles
               JOIN log
               ON log.path LIKE('%' || articles.slug)
               GROUP BY articles.title
               ORDER BY views DESC """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print "\n\n"
    print colored("Which articles have been accessed most?", 'green')
    for row in rows:
        print colored(str(row[1]), 'red') + " views" + " - " + row[0]
    print "\n"
    return rows


"""
Task:       Who are the most popular authors of all time?
Help:       Sum up all articles per author, which author get the most views?
Output:     Sorted list with the most popular author at the top.
Example:    Ursula La Multa — 2304 views
"""


def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT authors.name, sum(articles.views) as views
               FROM authors
               JOIN ( SELECT articles.author, count(*) as views
                      FROM articles
                      JOIN log
                      ON log.path LIKE('%' || articles.slug)
                      GROUP BY articles.author) as articles
               ON authors.id = articles.author
               GROUP BY authors.name
               ORDER BY views DESC """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print "\n\n"
    print colored("Who are the most popular authors of all time?", 'green')
    for row in rows:
        print colored(str(row[1]), 'red') + " views" + " - " + row[0]
    print "\n"
    return rows


"""
Task:       On which days did more than 1 % of requests lead to errors?
Help:       The log table includes a column status that indicates
            the HTTP status code that the news site sent to the user's browser.
Example:    July 29, 2016 — 2.5 % errors
"""


def get_bad_devops_days():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT stats.date,
        (CAST(stats.error as FLOAT) / CAST(stats.success as FLOAT) * 100)
        FROM (
            SELECT  DATE(time) as date,
                count(*) FILTER (WHERE status = '200 OK') AS success,
                count(*) FILTER (WHERE status != '200 OK') AS error
            FROM log
            GROUP BY DATE(time)
            ORDER BY date DESC
        ) AS stats
        WHERE (CAST(stats.error as FLOAT) /
                CAST(stats.success as FLOAT) * 100) > 1 """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print "\n\n"
    print colored("Days with more then 1% error rate:", 'green')
    for row in rows:
        print row[0].strftime("%B %d, %Y") + " - " \
            + colored(str(row[1])[:3] + "%", 'red') + " errors"
    print "\n"
    return rows


if __name__ == '__main__':
    init(*sys.argv[1:])
