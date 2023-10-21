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
        unstable {
            // Marque o build como instável se os testes falharem
            always {
                script {
                    currentBuild.resultIsBetterOrEqualTo("SUCCESS")
                }
            }
        }
    }
}
