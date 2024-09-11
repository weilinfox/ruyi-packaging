%global _name cffi
%global _summary C Foreign Function Interface for Python
%global _description \
C Foreign Function Interface for Python. Interact with almost any C code from Python,\
based on C-like declarations that you can often copy-paste from header files or documentation.

Name:		python-%{_name}
Version:	1.16.0
Release:	2
Summary:	%{_summary}
License:	MIT
URL:		http://cffi.readthedocs.org
Source0:	https://files.pythonhosted.org/packages/source/c/cffi/%{_name}-%{version}.tar.gz

Buildrequires:  libffi-devel gcc-c++ gcc python3-sphinx

%?python_enable_dependency_generator

%description %{_description}

%package -n python3-%{_name}
Summary:    %{_summary}
Buildrequires:  python3-devel python3-pycparser python3-pytest python3-setuptools
# for test
Buildrequires:  python3-py
%{?python_provide:%python_provide python3-%{_name}}

%description -n python3-%{_name} %{_description}

%package_help

%prep
%autosetup -n %{_name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest testing/

%files -n python3-%{_name}
%defattr(-,root,root)
%license LICENSE AUTHORS
%{python3_sitearch}/%{_name}/*
%{python3_sitearch}/%{_name}*info/
%{python3_sitearch}/_%{_name}*.so

%files help
%defattr(-,root,root)
%doc PKG-INFO README.md

%changelog
* Thu Mar 07 2024 weilinfox <caiweilin@iscas.ac.cn> - 1.16.0-2
- Fix "/usr/bin/python3 -m pytest c/ testing/" "ERROR: file or directory not found: c/"

* Wed Jan 10 2024 Dongxing Wang <dongxing.wang_a@thundersoft.com> - 1.16.0-1
- Update package to version 1.16.0

* Thu Jul 27 2023 shixuantong <shixuantong1@huawei.com> - 1.15.1-3
- Adjust tests for a last minute Python 3.11 change in the traceback format

* Sat Jul 08 2023 shixuantong <shixuantong1@huawei.com> - 1.15.1-2
- add python3-py to buildrequire

* Thu Jan 19 2023 chendh6<chendonghui6@huawei.com> - 1.15.1-1
- DESC:upgrade 1.15.1-1

* Mon Jun 20 2022 tanyulong <tanyulong@kylinos.cn> - 1.15.0-2
- Delete unnecessary gdb from BuildRequires

* Sat Dec 25 2021 tianwei <tianwei12@huawei.com> - 1.15.0-1
- upgrade version to 1.15.0

* Sat Jul 24 2021 shixuantong <shixuantong@huawei.com> - 1.14.6-1
- upgrade version to 1.14.6

* Mon Feb 1 2021 wangjie<wangjie294@huawei.com> - 1.14.4-1
- DESC:upgrade 1.14.4-1

* Fri Nov 20 2020 shixuantong <shixuantong@huawei.com> - 1.14.0-4
- Type:bufix
- CVE:NA
- SUG:NA
- DESC:fix test_init_once_multithread AssertionError for x86_64

* Fri Oct 30 2020 wuchaochao <wuchaochao4@huawei.com> - 1.14.0-3
- Type:bufix
- CVE:NA
- SUG:NA
- DESC:remove python2

* Mon Aug 10 2020 tianwei <tianwei12@huawei.com> - 1.14.0.-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:open make check

* Thu Jul 23 2020 dingyue<dingyue5@huawei.com> - 1.14.0-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:NA

* Thu Jun 18 2020 gaochao<gaochao52@huawei.com> - 1.11.5-11
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:potential fix for python3.8

* Tue Nov 5 2019 shenyangyang<shenyangyang4@huawei.com> - 1.11.5-10
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add provides of pythonx.7dist(cffi)

* Fri Sep 27 2019 shenyangyang<shenyangyang4@huawei.com> - 1.11.5-9
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:move license file

* Thu Sep 5 2019 shenyangyang<shenyangyang4@huawei.com> - 1.11.5-8
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:optimize the method to provide default version of python-name

* Wed Aug 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11.5-7
- Package init
