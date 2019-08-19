pipeline{
agent any
stages {    
    stage(Run python) {
    steps{
git 'https://github.com/Iditbnaya/DockerRedisPython-idit.git' 
bat 'python' PythonProject2.py
	    }       
	}
 stage(Docker compose) {
        steps{
           bat docker-compose up -d
	    }
    
	}
	   	}
   
}


  
  
  
