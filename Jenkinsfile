pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'yourdockerhubusername/mlops-model:latest'
  }

  stages {
    stage('Checkout Code') {
      steps {
        git url: 'https://github.com/mubashirzaidi1/mlops-innovate-analytics.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker push $DOCKER_IMAGE'
        }
      }
    }
  }

  post {
    success {
      echo '✅ Docker image built and pushed successfully!'
    }
    failure {
      echo '❌ Build or push failed!'
    }
  }
}
