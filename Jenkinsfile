pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/sanikaa5/technova-inventory'
            }
        }

        stage('Install Dependencies') {
            steps {
                # sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                # Add your test commands here if needed, for example:
                # sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t technova-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        sh 'docker push technova-app'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application (optional step)'
                # You can add your deployment script here
            }
        }
    }
}
