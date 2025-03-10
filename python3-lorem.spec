%define		module		lorem
Summary:	Generator for random text that looks like Latin
Name:		python3-%{module}
Version:	0.1.1
Release:	2
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/lorem/
Source0:	https://files.pythonhosted.org/packages/source/l/lorem/%{module}-%{version}.tar.gz
# Source0-md5:	e3f0064a94c13e19780eb724affdb426
URL:		https://github.com/sfischer13/python-lorem
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generator for random text that looks like Latin.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
