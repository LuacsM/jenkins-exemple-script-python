pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('teste') {
      steps {
        bat 'python test_calculadora_estatistica.py'
      }
    }
  }
}
