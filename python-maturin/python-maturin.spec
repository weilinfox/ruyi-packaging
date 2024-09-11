%global _empty_manifest_terminate_build 0
%global pypi_name maturin

Name:           python-%{pypi_name}
Version:        1.6.0
Release:        1
Summary:        Build and publish Rust crates as Python packages.

License:        MIT OR Apache-2.0
URL:            https://github.com/PyO3/maturin
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        cargo-vendor.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-rust
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:	python3-hatchling
BuildRequires:	rust-packaging

%description
Miscellaneous utilities for dealing with filesystems, paths, projects, subprocesses, and more.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Miscellaneous utilities for dealing with filesystems, paths, projects, subprocesses, and more.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
tar xzvf %{SOURCE1} -C .
mkdir .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
%pyproject_build

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.md Changelog.md
%license license-apache license-mit
%{_bindir}/maturin
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}*.dist-info/

%changelog
* Sun Aug 18 2024 weilinfox <caiweilin@iscas.ac.cn> - 1.6.0-1
- Update to version 1.6.0

* Tue Jun 27 2023 Dongxing Wang <dxwangk@isoftstone.com> - 1.1.0-1
- Initial package
