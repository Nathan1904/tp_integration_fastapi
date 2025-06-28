pipeline {
  agent {
    docker {
      image 'python:3.11'
    }
  }

  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run tests') {
      steps {
        sh 'PYTHONPATH=. pytest --junitxml=test-results.xml'
      }
    }

    stage('Publish Test Results') {
      steps {
        junit 'test-results.xml'
      }
    }
  }
}
