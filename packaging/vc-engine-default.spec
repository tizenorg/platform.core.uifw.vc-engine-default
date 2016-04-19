%define _optdir	/opt
%define _appdir	%{_optdir}/apps

Name:       vc-engine-default
Summary:    Voice control default engine library
Version:    0.2.0
Release:    1
Group:      Graphics & UI Framework/Voice Framework
License:    Flora-1.1
Source0:    %{name}-%{version}.tar.gz
Source1001: %{name}.manifest
BuildRequires:  cmake
BuildRequires:  pkgconfig(libtzplatform-config)

%description
Description: Voice control default engine library

%prep
%setup -q
cp %{SOURCE1001} .

cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIBDIR=%{_libdir} -DTZ_SYS_RO_SHARE=%TZ_SYS_RO_SHARE

%build
%if 0%{?tizen_build_binary_release_type_eng}
export CFLAGS="$CFLAGS -DTIZEN_ENGINEER_MODE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_ENGINEER_MODE"
export FFLAGS="$FFLAGS -DTIZEN_ENGINEER_MODE"
%endif
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{TZ_SYS_RO_SHARE}/license
cp %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}%{TZ_SYS_RO_SHARE}/license/%{name}

%files
%manifest vc-engine-default.manifest
%defattr(-,root,root,-)
%{TZ_SYS_RO_SHARE}/voice/vc/1.0/engine/lib*.so
%{TZ_SYS_RO_SHARE}/voice/vc/1.0/engine-info/vc-default-info.xml
%{TZ_SYS_RO_SHARE}/voice/vc/engine_data/*
%{TZ_SYS_RO_SHARE}/license/%{name}
