#!groovy

@Library('emt-pipeline-lib@master') _

repo_creds   = 'emt-jenkins-github-ssh'
version_file = 'setup.py'
version_key  = 'version'
domain_name  = getDnsDomainName()
artifact_repo_url = "http://nexus.${domain_name}:8082/repository/emt-pypi-internal/"
artifact_repo_creds = 'nexus-credentials'

node('docker-slave') {

  stage('Checkout') {
	checkout(scm)
  }

  stage('Release') {
    bumpPackageVersion(repo_creds,
					   'emt-jenkins',
					   "jenkinsci@${domain_name}",
					   version_file,
					   version_key)
    uploadToArtifactRepository(artifact_repo_url, artifact_repo_creds)
  }
}
