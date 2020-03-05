#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds   = 'emt-jenkins-github-ssh'
version_file = 'setup.py'
version_key  = 'version'

node('linux') {

  stage('Checkout') {
	checkout(scm)
  }

  stage('Release') {
    bumpPackageVersion(repo_creds,
					   'emt-jenkins',
					   'jenkinsci@emtegrity.com',
					   version_file,
					   version_key)
  }
}
