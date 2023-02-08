pipeline {
    agent any
    stages {
        stage('stop running container') {
            steps {
                sh 'docker compose down'
            }
        }
        stage('start grocery shop background') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
    }
}