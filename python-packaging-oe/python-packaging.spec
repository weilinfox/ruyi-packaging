%global _empty_manifest_terminate_build 0
%bcond_without test

Name:           python-packaging
Version:        24.0
Release:        1
Summary:        Core utilities for Python packages
License:        BSD and ASL 2.0
URL:            https://github.com/pypa/packaging
Source0:        https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz
BuildArch:      noarch
%description
Reusable core utilities for various Python Packaging interoperability specifications.

This library provides utilities that implement the interoperability specifications which have clearly one correct behaviour (eg: PEP 440) or benefit greatly from having a single shared implementation (eg: PEP 425).

The packaging project includes the following: version handling, specifiers, markers, requirements, tags, utilities.

%package -n python3-packaging
Summary:        Core utilities for Python packages
Provides:       python-packaging
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr python3-flit-core
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-pretend
%if %{with tests}
BuildRequires:  python3-pytest
%endif
BuildRequires:  python3-pyparsing
Requires:       python3-pyparsing
Provides:       python%{python3_pkgversion}dist(packaging) = %{version}
Provides:       python%{python3_version}dist(packaging) = %{version}

%description -n python3-packaging
Reusable core utilities for various Python Packaging interoperability specifications.

This library provides utilities that implement the interoperability specifications which have clearly one correct behaviour (eg: PEP 440) or benefit greatly from having a single shared implementation (eg: PEP 425).

The packaging project includes the following: version handling, specifiers, markers, requirements, tags, utilities.

%package help
Summary:        Core utilities for Python packages
Provides:       python3-packaging-doc
%description help
Reusable core utilities for various Python Packaging interoperability specifications.

This library provides utilities that implement the interoperability specifications which have clearly one correct behaviour (eg: PEP 440) or benefit greatly from having a single shared implementation (eg: PEP 425).

The packaging project includes the following: version handling, specifiers, markers, requirements, tags, utilities.

%prep
%autosetup -n packaging-%{version}

%build
%pyproject_build

%install
%pyproject_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%if %{with tests}
%{__python3} -m pytest tests/
%endif

%files -n python3-packaging -f filelist.lst
%dir %{python3_sitelib}/*
%{python3_sitelib}/packaging/__pycache__/

%files help -f doclist.lst
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst
%{_docdir}/*

%changelog
* Tue Apr 02 2024 weilinfox <caiweilin@iscas.ac.cn> - 24.0-1
- Update to version 24

* Mon Mar 4 2024 Dongxing Wang <dongxing.wang_a@thundersoft.com> - 23.2-1
- Update package with version 23.2
  Add python 3.12 support.
  Add types for packaging.version._Version.
  Add platform tag support for LoongArch.
  Update pyupgrade to Python 3.7+
  Support enriched metadata.

* Thu May 11 2023  liyanan <thistleslyn@163.com> - 23.1-1
- update version to 23.1

* Wed Dec 29 2021 shixuantong <shixuantong@huawei.com> - 21.3-3
- fix provides error

* Tue Dec 28 2021 shixuantong <shixuantong@huawei.com> - 21.3-2
- provide python3dist(packaging) and python3.xdist(packaging)

* Mon Dec 06 2021 shixuantong <shixuantong@huawei.com> - 21.3-1
- update version to 21.3

* Thu Dec 2 2021 shangyibin <shangyibin1@huawei.com> - 21.2-1
- Upgrade to version 21.2

* Sat Nov 27 2021 shixuantong <shixuantong@huawei.com> - - 20.9-2
- disable %check

* Tue Jul 13 2021 OpenStack_SIG <openstack@openeuler.org> - 20.9-1
- Upgrade to version 20.9

* Mon Feb 01 2021 shangyibin <shangyibin1@huawei.com> - 20.8-1
- Upgrade to version 20.8

* Thu Aug 06 2020 lingsheng <lingsheng@huawei.com> - 20.4-2
- Remove python2-packaging subpackage

* Fri Jul 24 2020 tianwei <tianwei122@huawei.com> - 20.4-1
- Package update to release 20.4

* Tue Nov 26 2019 Ling Yang <lingyang2@huawei.com> - 17.1-2
- Package init
