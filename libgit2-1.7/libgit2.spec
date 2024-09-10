Name:           libgit2
Version:        1.7.2
Release:        1
Summary:        portable, pure C implementation of the Git core methods
License:        GPLv2 with exceptions
URL:            https://libgit2.org
Source0:        https://github.com/libgit2/libgit2/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc cmake >= 3.5.1 ninja-build http-parser-devel libcurl-devel
BuildRequires:  libssh2-devel openssl-devel python3 zlib-devel
BuildRequires:  pcre2-devel
Provides:       bundled(libxdiff)

%description
libgit2 is a portable, pure C implementation of the Git core methods provided as
a re-entrant linkable library with a solid API, allowing you to write native speed
custom Git applications in any language which supports C bindings.

%package        devel
Summary:        Development files for libgit2
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and headers for developing applications that use libgit2.

%prep
%autosetup -n %{name}-%{version} -p1
find examples -name ".gitignore" -delete -print
sed -i '/-sonline/s/^/#/' tests/libgit2/CMakeLists.txt
# Remove bundled libraries (except libxdiff)
pushd deps
find . -maxdepth 1 -not -name xdiff -exec rm -rf {} ';'
popd

%build
%cmake . -B%{_target_platform} -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DREGEX_BACKEND=pcre2 -DBUILD_CLI=OFF -DUSE_SHA1=HTTPS -DUSE_HTTP_PARSER=system \
  -DUSE_NTLMCLIENT=OFF -DUSE_HTTPS=OpenSSL -DUSE_SSH=ON %{nil}
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%check
%ninja_test -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%doc AUTHORS docs examples README.md
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/git2*

%changelog
* Wed Mar 06 2024 yaoxin <yao_xin001@hoperun.com> - 1.7.2-1
- Upgrade to 1.7.2

* Wed Feb 07 2024 yaoxin <yao_xin001@hoperun.com> - 1.6.5-1
- Upgrade to 1.6.5 for fix CVE-2024-24575 and CVE-2024-24577

* Fri Jul 7 2023 liyanan <thistleslyn@163.com> - 1.6.4-1
- Update to version 1.6.4
- Abi change: libgit2.so.1.3.2 -> libgit2.so.1.6.4

* Mon Jul 25 2022 xu_ping <xuping33@h-partners.com> - 1.3.2-1
- Upgrade 1.3.2

* Fri May 13 2022 liyanan <liyanan32@h-partners.com> - 0.27.8-5
- Remove error-prone, redundant test

* Fri Jul 23 2021 guoxiaoqi<guoxiaoqi2@huawei.com> - 0.27.8-4
- fix CVE-2020-12278 and CVE-2020-12279

* Thu Jan 16 2020 yangjian<yangjian79@huawei.com> - 0.27.8-3
- Change the Source to valid address

* Tue Dec 31 2019 lingsheng <lingsheng@huawei.com> - 0.27.8-2
- Package init
