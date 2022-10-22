FROM jenkins:alpine

USER root

RUN apt-get update && \
    apt-get -y install apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
      $(lsb_release -cs) \
      stable" 
      
RUN   apt-get update && \
      apt-get -y install docker-ce
   
COPY ./jenkins-plugins /usr/share/jenkins/plugins
RUN while read i ; \
                do /usr/local/bin/install-plugins.sh $i ; \
        done < /usr/share/jenkins/plugins

ENV JENKINS_USER admin
ENV JENKINS_PASS hackoctoberfest

RUN ssh-keygen -f /root/.ssh/id_rsa -t rsa -N ''

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/
VOLUME /var/jenkins_home
