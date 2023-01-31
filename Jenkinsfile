pipeline {
    agent any
    triggers {
        githubPush()
    }
    environment {
        PATH = "C:/WINDOWS/SYSTEM32;C:/Users/Elliott Joliman/AppData/Local/Programs/Python/Python310;C:/Program Files/Docker/Docker/resources/bin"
    }
    stages {
//         stage('Create Staging Branch') {
//             steps {
//                 echo 'Creating Staging Branch...'
//                 bat 'git branch -D staging'
//                 bat 'git branch staging'
//                 bat 'git push -u origin staging'
//             }
//         }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies...'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests...'
                bat 'python test_main.py'
            }
        }
        stage('Build and Run Docker') {
            steps {
                echo 'Building Docker Image...'
                bat 'docker build -t my-app .'
                bat 'docker run -d my-app'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing to Docker Hub...'
                bat 'docker login -u 971500 -p Elliottdocker971.'
                bat 'docker tag my-app 971500/my-app'
                bat 'docker push 971500/my-app'
            }
        }
//         stage('Merge to Main') {
//             steps {
//                 echo 'Merging to Main...'
//                 bat 'git checkout main'
//                 bat 'git merge staging'
//                 bat 'git push origin main'
//             }
//         }

    }
}
