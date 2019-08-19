pipeline{
agent any
stages {    
    stage('python') {
    steps{
	    
	    bat 'docker-compose up -d'

	    }       
	}
 stage('compose') {
        steps{
          git 'https://github.com/Iditbnaya/DockerRedisPython-idit.git' 
bat 'python PythonProject2.py'
	    }
    
	}
	   	}
   
}


  
  
  
