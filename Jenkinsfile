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
				python3 -m venv 20921/env
				source ~/20921/env/bin/activate
				sudo yum install python3 -y				
			'''
		}
	}
    }
}
