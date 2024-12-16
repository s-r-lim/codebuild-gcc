Name: gcc-devel
Version: 14.2.0
Release: ${CODEBUILD_BUILD_NUMBER}%{?dist}
Summary: GCC Binary package
ExclusiveArch: x86_64 aarch64
License: GPL 
Provides: gcc-devel
Source0: gcc-devel-%{version}.tar.gz


%description
GCC binaries

%prep
%setup -q

%install
%define usrlocal %{_prefix}/local
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{usrlocal}
cp -r * $RPM_BUILD_ROOT%{usrlocal}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{usrlocal}/*
