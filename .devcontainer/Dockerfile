FROM ubuntu

# update
RUN apt-get update

# install nodejs
RUN printf 'y\n1\n\1n' | apt install nodejs

# install npm
RUN apt install -y npm

# check node is installed
RUN node -v

# check npm is installed
RUN npm -v

# install curl
RUN apt install -y curl

# install unzip
RUN apt install -y unzip

# Install noVNC (VNC client)
RUN cd /tmp && \
    curl --location --remote-name https://github.com/novnc/noVNC/archive/refs/tags/v1.5.0.zip && \
    unzip v1.5.0.zip && \
    rm --force v1.5.0.zip && \
    cd noVNC-1.5.0/utils && \
    curl --location --remote-name https://github.com/novnc/websockify/archive/refs/heads/master.tar.gz && \
    tar xzf master.tar.gz && \
    mv websockify-master websockify && \
    rm --force master.tar.gz && \
    cd ../.. && \
    mv noVNC-1.5.0 /opt/noVNC

# Install VS Code extensions
RUN npm install --global @vscode/vsce yarn && \
    mkdir --parents /opt/cs50/extensions && \
    cd /tmp && \
    git clone https://github.com/cs50/explain50.vsix.git && \
    cd explain50.vsix && \
    npm install && \
    vsce package && \
    mv explain50-1.0.0.vsix /opt/cs50/extensions && \
    cd /tmp && \
    rm --force --recursive explain50.vsix && \
    git clone https://github.com/cs50/cs50.vsix.git && \
    cd cs50.vsix && \
    npm install && \
    vsce package && \
    mv cs50-0.0.1.vsix /opt/cs50/extensions && \
    mv python-clients/cs50vsix-client /opt/cs50/extensions && \
    cd /tmp && \
    rm --force --recursive cs50.vsix && \
    git clone https://github.com/cs50/ddb50.vsix.git && \
    cd ddb50.vsix && \
    npm install && \
    vsce package && \
    mv ddb50-2.0.0.vsix /opt/cs50/extensions && \
    cd /tmp && \
    rm --force --recursive ddb50.vsix && \
    git clone https://github.com/cs50/phpliteadmin.vsix.git && \
    cd phpliteadmin.vsix && \
    npm install && \
    vsce package && \
    mv phpliteadmin-0.0.1.vsix /opt/cs50/extensions && \
    cd /tmp && \
    rm --force --recursive phpliteadmin.vsix && \
    git clone https://github.com/cs50/style50.vsix.git && \
    cd style50.vsix && \
    npm install && \
    vsce package && \
    mv style50-0.0.1.vsix /opt/cs50/extensions && \
    cd /tmp && \
    rm --force --recursive style50.vsix && \
    git clone https://github.com/cs50/design50.vsix.git && \
    cd design50.vsix && \
    npm install && \
    vsce package && \
    mv design50-1.0.0.vsix /opt/cs50/extensions && \
    cd /tmp && \
    rm --force --recursive design50.vsix && \
    npm uninstall --global vsce yarn

# Set virtual display
ENV DISPLAY=":0"

# Install Ubuntu packages
# Install acl for temporarily removing ACLs via opt/cs50/bin/postCreateCommand
# https://github.community/t/bug-umask-does-not-seem-to-be-respected/129638/9
RUN apt update && \
    apt install --no-install-recommends --no-install-suggests --yes \
        acl \
        dwarfdump \
        openbox \
        x11vnc \
        xvfb && \
    apt clean


# install pip3
RUN apt install -y python3-pip

# Install Python packages
RUN pip3 install --no-cache-dir --break-system-packages \
        black \
        "pydantic<2" \
        setuptools \
        pygame
