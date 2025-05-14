pipeline {
    agent any

    environment {
        // Define variables (replace with actual values)
        REPO_URL = 'https://github.com/sanikaa5/technova-inventory.git'  // Your repo URL
        BRANCH = 'main'  // The branch to monitor (default is usually 'main' or 'master')
    }

    stages {
        stage('Clone Repo') {
            steps {
                // Clone the repository from GitHub
                git url: "${REPO_URL}", branch: "${BRANCH}"
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run Python tests using unittest (change if you're using pytest or other framework)
                    sh 'python3 -m unittest discover'
                }
            }
        }


        stage('Post-pipeline Steps') {
            steps {
                echo 'Pipeline completed.'
            }
        }
    }

    post {
        success {
            echo 'Build and tests were successful!'
        }

        failure {
            echo 'There was a failure during the pipeline execution.'
        }
    }
}
