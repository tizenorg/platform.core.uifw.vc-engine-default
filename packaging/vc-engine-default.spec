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

%description
Description: Voice control default engine library

%prep
%setup -q
cp %{SOURCE1001} .

cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIBDIR=%{_libdir}

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
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}/usr/share/license/%{name}

%files
%manifest vc-engine-default.manifest
%defattr(-,root,root,-)
%{_libdir}/voice/vc/1.0/engine/lib*.so
%{_libdir}/voice/vc/1.0/engine-info/vc-default-info.xml
/usr/share/voice/vc/engine_data/*
/usr/share/license/%{name}
