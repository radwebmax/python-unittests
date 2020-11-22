pipeline{
  options{timestamps}
  agent none
  stages{
    stage("Check scm"){
      agent any
      steps{
        checkout scm
       }
     }
     stage("Test"){
      agent{docker {image 'alpine'
              args '-u=\"root\"'
              }
            }
       steps{
        sh 'apk add --update python3 py-pip'
        sh 'pip install xmlrunner'
        sh 'python3 test.py'
       }
       post{
        always{
          junit "test-reports/*.xml"
            }
        success{
          echo 'Application testing successfully completed'
        failure{
          echo 'F#ck, smth went wrong =('
        }
      }
    }
  }
 }
}
}
     
      
