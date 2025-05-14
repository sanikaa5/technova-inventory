pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'inventory-technova'
        EC2_USER = 'ubuntu'
        EC2_HOST = '13.53.38.114'
        EC2_SSH_KEY_PATH = 'C:\\Users\\Sanika Dhakite\\Downloads\\technova-key.pem'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Assuming you have a test script or pytest setup in the app
                    sh 'python3 -m unittest discover'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with the name 'inventory-technova'
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Optional step: Push the image to Docker Hub (if needed)
                    // sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    // SSH into EC2 instance and run the Docker container
                    sh """
                        ssh -i ${EC2_SSH_KEY_PATH} ${EC2_USER}@${EC2_HOST} "
                        docker pull ${DOCKER_IMAGE}:latest
                        docker run -d --name ${DOCKER_IMAGE} -p 80:80 ${DOCKER_IMAGE}:latest
                        "
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
