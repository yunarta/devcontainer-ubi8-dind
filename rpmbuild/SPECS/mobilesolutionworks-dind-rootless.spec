Name:           mobilesolutionworks-dind-rootless
Version:        27.3.1
Release:        %{getenv:BUILD_NUMBER}%{?dist}
Summary:        mobilesolutionworks dind-rootless
License:        INSERT_LICENSE_HERE
URL:            https://www.mobilesolutionworks.com
BuildArch:      x86_64
Requires:       ca-certificates, openssh-clients, wget, iptables, iproute, fuse-overlayfs, shadow-utils

%description
mobilesolutionworks dind-rootless

%prep
# Nothing to do here for a binary package

%build
# Nothing to do here for a binary package

%install
mkdir -p %{buildroot}/usr/local/bin/
cp -r %{_sourcedir}/* %{buildroot}/usr/local/bin/

%files
/usr/local/bin/containerd
/usr/local/bin/containerd-shim-runc-v2
/usr/local/bin/ctr
/usr/local/bin/dind
/usr/local/bin/docker
/usr/local/bin/docker-configure-user
/usr/local/bin/docker-entrypoint.sh
/usr/local/bin/docker-init
/usr/local/bin/docker-proxy
/usr/local/bin/dockerd
/usr/local/bin/dockerd-entrypoint.sh
/usr/local/bin/modprobe
/usr/local/bin/rootlesskit
/usr/local/bin/rootlesskit-docker-proxy
/usr/local/bin/runc
/usr/local/bin/vpnkit

%post
groupadd --system dockremap
useradd --system --gid dockremap dockremap
groupadd docker

echo 'dockremap:165536:65536' >> /etc/subuid
echo 'dockremap:165536:65536' >> /etc/subgid

mkdir -p /run/user
chmod 1777 /run/user
mkdir -p /certs/client
chmod 1777 /certs /certs/client

%changelog
* Tue Nov 07 2023 Yunarta Kartawahyudi <yunarta.kartawahyudi@gmail.com> - 1.0-1
- First build of mobilesolutionworks-dind-rootless