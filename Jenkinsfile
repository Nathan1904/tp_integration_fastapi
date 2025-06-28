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

    stage('Code Analysis (pylint)') {
      steps {
        sh '''
          pylint app > pylint-report.txt || true
        '''
      }
    }

    stage('Publish Test Results') {
      steps {
        junit 'test-results.xml'
      }
    }

    stage('Archive pylint report') {
      steps {
        archiveArtifacts artifacts: 'pylint-report.txt', onlyIfSuccessful: true
      }
    }
  }

  post {
    always {
      echo 'Pipeline terminée.'
    }
    failure {
      echo 'Échec dans la pipeline.'
    }
  }
}
    