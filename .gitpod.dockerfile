FROM gitpod/workspace-full

# Install Graphviz
RUN sudo apt-get update \
    && sudo apt-get -y install graphviz

# Install JHipster
RUN npm install -g generator-jhipster

# Install Java
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh && \
    sdk install java 17.0.8-tem && \
    sdk default java 17.0.8-tem"

# Install Gradle
RUN sudo apt-get install -y gradle
