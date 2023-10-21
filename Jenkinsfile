pipeline {
    agent any
      stages {
        stage('Checkout') {
            steps {
                // Verifique o código do repositório
                checkout scm
                bat 'pip install xmlrunner'
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
                // Execute os testes e gere relatório em formato JUnit
                bat 'python -m unittest -v test_calculadora_estatistica.py --junit-xml test_results.xml'
            }
            post {
                always {
                    junit '**/test_results.xml'
                }
            }
        }

        stage('Cobertura de Código') {
            steps {
                // Execute os testes com cobertura de código e gere relatório HTML
                bat 'coverage run -m unittest discover -v -s . -p test_*.py'
                bat 'coverage xml'
                bat 'coverage html'
            }
            post {
                always {
                    // Arquivos de cobertura são gerados nos diretórios "coverage.xml" e "htmlcov"
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Cobertura de Código'
                    ])
                }
            }
        }
    }
}
