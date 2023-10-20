pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Verifique o código do repositório
                checkout scm
            }
        }
        stage('Main') {
            steps {
                // Execute o main.py
                bat 'python main.py'
            }
        }
        stage('Testes') {
            steps {
                // Execute os testes
                bat 'python -m unittest -o test_results.xml test_calculadora_estatistica.py'
            }
        }
        stage('Publish Test Results') {
          steps {
              // Use o plugin JUnit ou xUnit para publicar os resultados dos testes
              // Se estiver usando o JUnit Plugin:
              junit 'test_results.xml'
              // Se estiver usando o xUnit Plugin:
              xunit(tools: [JUnit(deleteOutputFiles: true, failIfNotNew: false, pattern: 'test_results.xml')])
          }
        }
    }
}
