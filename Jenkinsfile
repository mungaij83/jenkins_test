pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'docker build -t test/image:v1.0.0'
            }
        }
        stage("push_image"){
            steps{
                sh 'echo "Push image"'
            }
        }
    }
}