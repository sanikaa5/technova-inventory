pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'inventory-app'
        DOCKER_REGISTRY = 'your-docker-registry'  // Set your Docker registry (if applicable)
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any dependencies if needed (this step is optional if you don't have a requirements.txt)
                echo 'No dependencies to install'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image for the Flask app
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest discover tests'
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    // Run the Docker container from the built image
                    docker.image(DOCKER_IMAGE).run('-d -p 5000:5000')
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace after the pipeline is done
        }

        success {
            echo 'Deployment was successful!'
        }

        failure {
            echo 'Something went wrong, check the logs.'
        }
    }
}
