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
				sudo python3 -m pip install virtualenv
				python3 -m venv 20921
				source 20921/bin/activate
				pip install pylint
				echo $PATH
			'''
		}
	}
	stage('Test')	{
		steps{
			sh '''
				python Jenkins/tests/test_name.py
				python Jenkins/tests/test_email.py
				python Jenkins/tests/test_gender.py
				python3 Jenkins/tests/test_phone.py
			'''
		}
	}
	stage('Deploy')	{
		steps{
			sh '''
				sudo scp -i  'Jenkins/20921-Sanskruti.pem' -o StrictHostKeyChecking=no -r Jenkins/ ec2-user@54.167.150.109:~
				chmod 700 Jenkins/20921-Sanskruti.pem
				sudo ssh -T -i Jenkins/20921-Sanskruti.pem ec2-user@ec2-18-234-89-64.compute-1.amazonaws.com
				sudo yum install python3 -y
				sudo python3 -m pip install virtualenv
				python3 -m venv 20921
				source 20921/bin/activate
				pip install pylint
			'''
		}
	}
    }
}
