%global pypi_name tomlkit

%global common_description %{expand:
TOML Kit is a 1.0.0-compliant TOML library.

It includes a parser that preserves all comments, indentations, whitespace and
internal element ordering, and makes them accessible and editable via an
intuitive API.}

Name:           python-%{pypi_name}
Summary:        Style preserving TOML library
Version:        0.12.4
Release:        1
License:        MIT

URL:            https://github.com/sdispater/tomlkit
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:	python3-editables
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling
BuildRequires:	python3-poetry-core

# test dependencies
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.dist-info/

%changelog
* Tue Apr 02 2024 weilinfox <caiweilin@iscas.ac.cn> - 0.12.4-1
- Update to version 0.12.4

* Tue Feb 27 2024 Dongxing Wang <dongxing.wang_a@thundersoft.com> - 0.12.3-1
- Update package to version 0.12.3
  chore(deps-dev): bump urllib3 from 1.26.14 to 1.26.18
  fix: Newline lost when updating a table
  fix: Significant slowdown on nested tables depending on syntax
  fix: Fix division for integers
  fix: error when overwriting a sub table

* Tue Oct 24 2023 jiangxinyu <jiangxinyu@kylinos.cn> - 0.12.1-1
- Update package to version 0.12.1

* Wed Jun 21 2023 chendexi <chendexi@kylinos.cn> - 0.11.8-1
- Update package to version 0.11.8

* Mon May 22 2023 Dongxing Wang <dxwangk@isoftstone.com> - 0.11.4-2
- Use poetry-core to build

* Tue May 16 2023 Dongxing Wang <dxwangk@isoftstone.com> - 0.11.4-1
- Init package version 0.11.4
