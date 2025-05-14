pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/sanikaa5/technova-inventory.git'  // Replace with your repo URL
        BRANCH_NAME = 'main'  // Replace with your branch
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository directly into Jenkins workspace
                bat 'git clone ${GIT_REPO}'
                bat 'cd technova-inventory && git checkout ${BRANCH_NAME}'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests (replace with your actual testing framework)
                bat 'cd technova-inventory && python -m unittest discover tests/'
            }
        }

    }

    post {
        success {
            echo 'Build and packaging successful!'
        }
        failure {
            echo 'Build or packaging failed.'
        }
    }
}
