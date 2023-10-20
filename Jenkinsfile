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
                bat 'python -m unittest -v test_calculadora_estatistica.py'
            }
        }
    }
    post {
        always {
            // Publique resultados dos testes JUnit
            step([$class: 'JUnitResultArchiver', testResults: 'test-reports/**/*.xml'])
        }
    }
}
