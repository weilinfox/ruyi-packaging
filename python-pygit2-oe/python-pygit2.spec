%global _empty_manifest_terminate_build 0
%global module pygit2

Name:		python-%{module}
Version:	1.14.1
Release:	1
Summary:	Python bindings for libgit2
License:	GPL-2.0-only WITH GCC-exception-2.0
URL:		https://www.pygit2.org/
Source0:	https://github.com/libgit2/pygit2/archive/v%{version}.tar.gz#/%{module}-%{version}.tar.gz

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

%package -n python3-%{module}
Summary:        Python 3 bindings for libgit2
Provides:	python-%{module}

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	(libgit2-devel >= 1.7.0 with libgit2-devel < 1.8.0)
BuildRequires:	python3-cffi >= 1.16.0
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm


%description -n python3-%{module}
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

The python3-%{pkgname} package contains the Python 3 bindings.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%description    doc
Documentation for %{name}.


%prep
%autosetup -n %{module}-%{version} -p 1

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%license COPYING
%doc README.md
%{python3_sitearch}/%{module}-*.egg-info/
%{python3_sitearch}/%{module}/

%changelog
* Thu Mar 07 2024 weilinfox <caiweilin@iscas.ac.cn> - 1.14.1-1
- Package for pygit2 1.14.1

