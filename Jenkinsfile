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
				cd Jenkins
				echo <715d38e70ac944f4920860628cdfecfa> | sudo -S yum install python3
			'''
		}
	}
    }
}
