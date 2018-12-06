# Run tests in check section
%bcond_without check

%global goipath         github.com/xanzy/ssh-agent
Version:                0.2.0

%global common_description %{expand:
Create a ssh-agent on any type of OS from any Go application.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Create a ssh-agent on any type of OS from any Go application
License:        ASL 2.0
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: golang(golang.org/x/crypto/ssh/agent)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Update to release 0.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitba9c9e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314gitba9c9e3
- Fix BuildRequires

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gitba9c9e3
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20151215gitba9c9e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20151215gitba9c9e3
- First package for Fedora

