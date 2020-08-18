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
				git clone https://github.com/Sanskruti-Khandelwal/Jenkins.git
			}
		}
    }
}
