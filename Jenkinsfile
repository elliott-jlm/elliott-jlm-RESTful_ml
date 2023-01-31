pipeline {
    agent any

    environment {
        PATH = "C:/WINDOWS/SYSTEM32;C:/Users/ellio/AppData/Local/Programs/Python/Python310;C:/Program Files/Docker/Docker/resources/bin"
    }
    
    stages {
        stage('Testing app') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                bat 'python test_main.py'
            }
        }

        stage('Docker deploy') {
            steps {
                bat 'docker build -t my-app .'
                bat 'docker run -d my-app'
            }
        }
    }
}
