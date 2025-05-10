pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'mubashirzaidi/mlops-model:latest'  // 🔁 Replace with your Docker Hub image name
  }

  stages {
    stage('Build Docker Image') {
      steps {
        echo '🔧 Building Docker image...'
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Push to Docker Hub') {
      steps {
        echo '🚀 Pushing Docker image to Docker Hub...'
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push $DOCKER_IMAGE
          '''
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
