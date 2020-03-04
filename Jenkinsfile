#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds   = 'emt-jenkins-git-ssh'
repo_url     = 'git@github.com:hlaf/centos-package-cron'
version_file = 'setup.py'
version_key  = 'version'

node('linux') {

  stage('Checkout') {
	checkoutFromGit(repo_creds, repo_url)
  }

  stage('Release') {
    bumpPackageVersion(repo_creds,
					   'emt-jenkins',
					   'jenkinsci@emtegrity.com',
					   version_file,
					   version_key)
  }
}
