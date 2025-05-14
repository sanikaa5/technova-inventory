pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }
        stage('Run') {
            steps {
                echo 'Running Python app...'
                sh 'python3 app.py'
            }
        }
    }
}
