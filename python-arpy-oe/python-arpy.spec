%global _empty_manifest_terminate_build 0
Name:		python-arpy
Version:	2.3.0
Release:	1
Summary:	Library for accessing "ar" files
License:	BSD
URL:		https://github.com/viraptor/arpy
Source0:	https://files.pythonhosted.org/packages/d1/d5/a1985a4a645a1d66825e4cbb9fa7e8c5d10bf5b41fd32badb38b6b5e55ea/arpy-2.3.0.tar.gz
BuildArch:	noarch


%description
arpy is a library for accessing the archive files and reading the contents.
It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.


%package -n python3-arpy
Summary:	Library for accessing "ar" files
Provides:	python-arpy
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-unittest2
BuildRequires:	python3-coverage
BuildRequires:	python3-flake8
%description -n python3-arpy
arpy is a library for accessing the archive files and reading the contents.
It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%package help
Summary:	Development documents and examples for arpy
Provides:	python3-arpy-doc
%description help
arpy is a library for accessing the archive files and reading the contents.
It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%prep
%autosetup -n arpy-%{version}

%build
%py3_build

%install
%py3_install
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
%{__python3} -m unittest discover -v


%files -n python3-arpy -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Oct 21 2022 guozhengxin <guozhengxin@kylinos.cn> - 2.3.0-1
- Upgrade package to version 2.3.0

* Mon Jun 20 2022 yangzhao <yangzhao1@kylinos.cn> - 2.2.0-2
- Remove BuildRequires python3-nose

* Fri Jul 16 2021 yinyongkang <yinyongkang@kylinos.cn> - 2.2.0-1
- Init Package
