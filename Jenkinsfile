pipeline {
    agent any

    environment {
        PY = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat "\"%PY%\" -m pip install --upgrade pip"
                bat "\"%PY%\" -m pip install -r requirements.txt"
            }
        }

        stage('Run tests') {
            steps {
                bat "\"%PY%\" -m pytest -q --alluredir=allure-results"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true, allowEmptyArchive: true
        }
    }
}
