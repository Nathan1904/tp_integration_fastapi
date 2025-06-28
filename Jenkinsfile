pipeline {
  agent any

  environment {
    VENV_DIR = ".venv"
  }

  stages {
    stage('Install Python & Dependencies') {
      steps {
        // Vérifie que pip est là, crée un environnement virtuel et installe les deps
        sh '''
          python -m venv $VENV_DIR
          . $VENV_DIR/Scripts/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Unit Tests') {
      steps {
        sh '''
          . $VENV_DIR/Scripts/activate
          pytest --junitxml=test-results.xml
        '''
      }
    }

    stage('Publish Test Results') {
      steps {
        junit 'test-results.xml'
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
