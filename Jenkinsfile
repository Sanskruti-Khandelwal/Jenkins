pipeline {
    agent any
    stages {
        stage('Clean Up') {
            steps {
                cleanWs()
            }
        }
	stage('Check out SCM') {
		steps {
			sh 'git clone https://github.com/Sanskruti-Khandelwal/Jenkins.git'
		}
	}
	stage('Build')	{
		steps{
			sh '''
				sudo yum install python3 -y
				python3 -m pip install virtualenv
				python3 -m venv 20921
				source 20921/bin/activate
			'''
		}
	}
    }
}
