pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'inventory-app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                echo 'Setting up Python virtual environment and installing Flask...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install Flask
                    echo "Flask installed in virtual environment"
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python3 -m unittest discover tests
                    echo "Unit tests completed"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}..."
                sh '''
                    docker build -t ${DOCKER_IMAGE} .
                    echo "Docker image built successfully"
                '''
            }
        }

        stage('Deploy Docker Container') {
            steps {
                echo "Deploying Docker container from image ${DOCKER_IMAGE}..."
                sh '''
                    docker stop inventory-container || echo "No running container to stop"
                    docker rm inventory-container || echo "No container to remove"
                    docker run -d -p 5000:5000 --name inventory-container ${DOCKER_IMAGE}
                    echo "Docker container deployed and running on port 5000"
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
