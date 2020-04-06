#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import socket
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from report_producer import ReportProducer
from db_session_fetcher import db_session_fetcher
import smtplib
from email.mime.text import MIMEText
import pkg_resources

__VERSION__ = pkg_resources.require("centos_package_cron")[0].version

def main():
    args = parse_args()

    repos_to_exclude_list = []
    if args.disablerepo is not None:
        repos_to_exclude_list = args.disablerepo.split(',')
    repos_to_include_list = []
    if args.enablerepo is not None:
        repos_to_include_list = args.enablerepo.split(',')

    skipold = not args.forceold
    producer = ReportProducer(repos_to_exclude_list, repos_to_include_list, skipold, args.skip_sqlite_file_path, include_depends_on=args.include_depends_on)

    if args.format == 'minimal':
        report_content = producer.get_report_content_minimal()
    elif args.format == 'json':
        report_content = producer.get_report_content_as_json()
    else:
        report_content = producer.get_report_content()
        
    if report_content != '':
        print report_content


def parse_args():
    parser = argparse.ArgumentParser(description="Emails administrators with CentOS security updates and changelogs of non-security updates. Version %s" % __VERSION__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-dr','--disablerepo',
                        type=str,
                        help='List of comma separated repos to exclude when dealing with Yum')

    parser.add_argument('-er','--enablerepo',
                        type=str,
                        help='List of comma separated repos to include when dealing with Yum')

    parser.add_argument('-fo','--forceold',
                        help='Instead of the default behavior to only complain once for a given advisory/package update notice, repeats them with each run.',
                        action="store_true")

    parser.add_argument('-db','--skip-sqlite-file-path',
                        type=str,
                        default=db_session_fetcher.DEFAULT_DB_PATH,
                        help='The location of the Sqlite DB used to track which notifications you have already received.')

    parser.add_argument('-do','--include-depends-on',
                        help='When a package update is listed, show what packages on your system depend on that package',
                        action="store_true")

    parser.add_argument('-f','--format',
                        type=str,
                        default='default',
                        choices=['default', 'json', 'minimal'],
                        help='Output the results in specific format: default (human-readable), json, minimal (prints only packages names, useful for scripting)')

    return parser.parse_args()

if __name__ == '__main__':
    sys.exit(main())
