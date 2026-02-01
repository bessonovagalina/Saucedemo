pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/bessonovagalina/Saucedemo.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }
    }
}
