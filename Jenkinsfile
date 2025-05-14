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
                echo 'Installing dependencies...'
                bat 'pip install flask'
            }
        }
        stage('Run Flask App') {
            steps {
                echo 'Running Flask app...'
                bat 'python app.py'
            }
        }
    }
}
