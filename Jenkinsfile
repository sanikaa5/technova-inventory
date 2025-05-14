pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }
        stage('Setup Python & Flask') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install Flask
                '''
            }
        }
        stage('Run App') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 app.py
                '''
            }
        }
    }
}
