pipeline{
agent any
stages {    
    stage('compose') {
    steps{
	    
	    bat 'docker-compose up -d'

	    }       
	}
 stage('python') {
        steps{
          git 'https://github.com/Iditbnaya/DockerRedisPython-idit.git' 
bat 'python PythonProject2.py'
	    }
    
	}
	   	}
   
}


  
  
  
