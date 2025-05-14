pipeline {
    agent any
    environment {
        // Optional: If you have a virtual environment, you can set it up here
        PYTHON_ENV = 'C:\\path\\to\\python\\env'  // Modify if using a specific virtual environment
        PATH = "${env.PYTHON_ENV}\\Scripts;${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sanikaa5/technova-inventory.git'
            }
        }
        stage('Run') {
            steps {
                echo 'Running Python app...'
                // Run the Python application
                bat 'python app.py'
            }
        }
    }
}
