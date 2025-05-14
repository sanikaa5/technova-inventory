pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'No dependencies to install'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat 'python3 -m unittest discover tests'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Python app...'
                bat 'python3 app.py'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
