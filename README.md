# Centos-Package-Cron

[![Build Status](https://img.shields.io/travis/wied03/centos-package-cron/master.svg?style=flat)](https://travis-ci.org/unitedtraders/centos-package-cron)
[![Quality](https://api.codeclimate.com/v1/badges/ce1d686b27f9ba2f4f2a/maintainability)](https://codeclimate.com/github/unitedtraders/centos-package-cron/maintainability)

Attempts to offer Apticron (Ubuntu) style package update emails and also bring security notifications to CentOS via Meier's script

## What does it do?

* Checks for updates using Yum's Python API and changelogs for those updates using Yum's changelog plugin
* Checks security errata from CentOS mailing list via [Steve Meier's XML file](https://cefs.steve-meier.de/) and reports advisories related to packages installed on your machine
* Provides report to stdout in JSON or plain text forms
* By default, only reminds about a given security advisory / package update once to avoid annoying you.  You can change this using the --forceold option (see -h)

## Why does this exist?

`yum --security` is an ideal solution, but it does not work on CentOS since the `updateinfo.xml` file in the CentOS repository does not include RHEL style security updates (see discussion [here](https://www.centos.org/forums/viewtopic.php?t=30967)). The options, which all depend on something like Steve's XML file (as of March 2016) that I know of are:

1. Use Spacewalk (see Steve site)
2. Generate `updateinfo.xml` with security information (see [VM farms post](https://web.archive.org/web/20170309083728/https://blog.vmfarms.com/2013/12/inject-little-security-in-to-your.html))
3. This tool

Some of these are good options but if you don't want Spacewalk and want more Apticron/apt type features like the DB/remember piece, this might be a good option for you.

## Requirements

Tested on CentOS 7, Python 2.7.

## Development in Docker

* Build Docker image from `docker/centos7/run.Dockerfile`: `docker build -t centos-package-development -f docker/centos7/run.Dockerfile docker/centos7`
* Launch image with code folder: `docker run --rm -v $(pwd):/app -w /app -u nonrootuser -ti centos-package-development`
* Run tests: `python setup.py test`

## Installation

### Using Python

From pypi:

From checked out copy:

```shell
sudo yum install yum-plugin-changelog
./setup.py install
# For the SQLite DB that avoids reminding you of updates that were already sent (see above)
mkdir /var/lib/centos-package-cron
```

### Using RPM

```shell
sudo yum install rpm-build yum-utils
# copy centos-package-cron.spec.in to centos-package-cron.spec and put the proper version numbers in those placeholders
sudo yum-builddep -y --disablerepo=updates centos-package-cron.spec
# Download a tar gzip of the source to /some/path/containing/source/centos_package_cron_src.tgz
rpmbuild -bb --verbose -D "_topdir `pwd`" -D "_sourcedir /some/path/containing/source" -D "_builddir `pwd`" centos-package-cron.spec
sudo yum install centos-package-cron-1.0.6-0.1.el7.centos.x86_64.rpm
```

## Usage

```shell
# See centos-package-cron -h for all options

# show all security updates
centos-package-cron -fo

# install all security updates except postgresql and docker
centos-package-cron -f minimal -fo | grep -v postgresql | grep -v docker | grep -v containerd | xargs sudo yum upgrade
```

## TODO

* Add CentOS 8 compability and test suites

## License

Copyright (c) 2016, BSW Technology Consulting LLC
              2020, UnitedTraders

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
