pipeline {
    agent any

    environment {
        IMAGE_NAME = "inventory-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Run Docker Container') {
            steps {
                sh "docker rm -f inventory-app || true"
                sh "docker run -d --name inventory-app -p 8081:8080 $IMAGE_NAME:$IMAGE_TAG"
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed.'
        }
    }
}
