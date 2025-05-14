pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'your_image_name'  // Replace with your image name
        EC2_USER = 'ubuntu'  // EC2 user
        EC2_HOST = 'your_ec2_ip'  // Your EC2 IP address
        KEY_PATH = '/path/to/your/technova-key.pem'  // Path to the private key
    }
    stages {
        stage('Clone Code') {
            steps {
                // Clone the latest code from GitHub
                git 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Deploy to EC2') {
            steps {
                script {
                    // Deploy the image on EC2
                    sh """
                        ssh -i ${KEY_PATH} ${EC2_USER}@${EC2_HOST} '
                            docker pull ${DOCKER_IMAGE}:latest || true  # Pull if exists
                            docker stop ${DOCKER_IMAGE} || true  # Stop the container if it exists
                            docker rm ${DOCKER_IMAGE} || true  # Remove the stopped container
                            docker run -d --name ${DOCKER_IMAGE} -p 80:80 ${DOCKER_IMAGE}:latest  # Run the container
                        '
                    """
                }
            }
        }
    }
}
