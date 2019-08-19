

pipeline { 
agent any 
stages { 
stage("test") { 



steps { 



script { 



try { 



git 'https://github.com/Iditbnaya/DockerRedisPython-idit.git' 
bat 'python' PythonProject2.py
docker-compose up


} catch (Exception e) { 

echo 'Handle the exception!' 


}
}
}
}
}
}

  
  
  
