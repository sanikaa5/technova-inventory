pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'inventory-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install Flask
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python3 -m unittest discover tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Deploy Docker Container') {
            steps {
                sh '''
                    docker stop inventory-container || true
                    docker rm inventory-container || true
                    docker run -d -p 5000:5000 --name inventory-container ${DOCKER_IMAGE}
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
