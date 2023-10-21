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
                // Execute os testes com cobertura
                bat 'coverage run -m unittest -v test_calculadora_estatistica'
            }
        }
        stage('Relatório de Cobertura HTML') {
            steps {
                // Gere o relatório HTML de cobertura
                bat 'coverage html'
            }
            post {
                always {
                    // Arquive o relatório HTML gerado
                    archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                }
            }
        }
    }
}

