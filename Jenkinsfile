

pipeline { 
agent any 
stages { 
stage("test") { 



steps { 



script { 



try { 



git 'https://github.com/Iditbnaya/DockerRedisPython-idit.git' 
bat 'python' PythonProject2.py
bat docker-compose up -d


} catch (Exception e) { 

echo 'Handle the exception!' 


}
}
}
}
}
}

  
  
  
