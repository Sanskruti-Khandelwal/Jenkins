pipeline {
    agent any
    stages {
        stage('Clean Up') {
            steps {
                cleanWs()
            }
        }
		stage('Check out SCM')	{
			steps{
				git pull https://github.com/Sanskruti-Khandelwal/Jenkins.git
			}
		}
    }
}
