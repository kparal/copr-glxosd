%global     commit     7f0886eb271a72ab6a309c675fba2d59c8af1007
%global     githash    %(c=%{commit}; echo ${c:0:7})
%global     gitdate    20160210
%global     capsname   GLXOSD

Name:     glxosd
Version:  2.5.0
Release:  1.%{gitdate}git%{githash}%{?dist}
Summary:  An OSD for OpenGL applications. Monitor your framerate in games.

License:  MIT
URL:      https://glxosd.nickguletskii.com/
Source0:  https://github.com/nickguletskii/GLXOSD/archive/%{commit}/%{name}-%{version}-%{gitdate}git%{githash}.tar.gz

# fix CMakeLists.txt to install to /usr/lib64 instead of /usr/lib
Patch1:   %{name}-p01-lib64.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  mesa-libGLU-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  boost-devel
BuildRequires:  lm_sensors-devel

%description
GLXOSD is an on-screen display (OSD)/overlay for OpenGL applications running on Linux with X11. It
can show FPS, the temperature of your CPU, and if you have an NVIDIA graphics card (with
proprietary drivers), it will also show the temperature of the GPU. Also, it can log frame timings,
which is useful for benchmarking. This project aims to provide some of the functionality that
RivaTuner OSD (which is used by MSI Afterburner) provides under Windows.

%prep
%setup -q -n %{capsname}-%{commit}
%patch1 -p1

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DINSTALLATION_SUFFIX_64=lib64 \
      -DINSTALLATION_SUFFIX_32=lib \
      -G "Unix Makefiles"
make %{?_smp_mflags} all

%install
%make_install

%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/fonts/truetype/CPMono_v07
%doc README.md
%doc screenshots/glxgears.png
%doc AUTHORS
%license LICENSE

%changelog
* Sun Feb 21 2016 Kamil Páral <kparal@redhat.com> - 2.5.0-1.20160210git7f0886e
- initial release from 20160210 (git version)
