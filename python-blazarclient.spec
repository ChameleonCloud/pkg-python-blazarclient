%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%global commit 06460e0d75d98f540e4d8f661f374933a4a399d1

Name:		python-blazarclient
Version:	0.1.0
Release:	1.git%{commit}%{?dist}
Summary:	Python client for Blazar

License:	ASL 2.0
URL:            https://wiki.openstack.org/wiki/Blazar
Source0:	https://github.com/stackforge/python-blazarclient/archive/%{commit}.tar.gz

Patch0001:	0001-chameleon-blazarclient-Remove-runtime-dependency-on-python-pbr.patch

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools

Requires:	python-babel >= 1.3
Requires:	python-cliff >= 1.6.0
Requires:	python-prettytable >= 0.7
Requires:	python-keystoneclient >= 0.10.0
Requires:	python-six >= 1.7.0
Requires:	python-requests >= 1.2.1

%description
A python and command line client library for Blazar.

%prep
%setup -q -n %{name}-%{commit}

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATBLAZARCLIENTVERSION/%{version}/ climateclient/version.py

%build
PBR_VERSION=%{version} %{__python2} setup.py build

%install
PBR_VERSION=%{version} %{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE README.rst
%{_bindir}/*
%{python2_sitelib}/climateclient*
%{python2_sitelib}/python_climateclient*


%changelog
* Fri Jan 23 2015 Pierre Riteau <priteau@uchicago.edu> 0.1.0-1.git06460e0d75d98f540e4d8f661f374933a4a399d1.el7
- Initial packaging
