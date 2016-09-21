%global     githash    9d07ca0
%global     gitdate    20160921

Name:     glxosd
Version:  3.2.0
Release:  1.%{gitdate}git%{githash}%{?dist}
Summary:  An OSD for OpenGL applications. Monitor your framerate in games.

License:  MIT
URL:      https://glxosd.nickguletskii.com/
# Please note that glxosd repo contains submodules, and they are not included in the github archive.
# You need to create the tarball manually, by cloning the repo with:
# git clone --recursive https://github.com/nickguletskii/GLXOSD.git
# or later by running:
# git submodule update --init --recursive
# Then tar it up like this:
# HASH=<hash>; tar -caf glxosd-$HASH.tar.gz --exclude-vcs -C <path/to/glxosd> --transform "s,^\.,glxosd-$HASH," .
Source0:  %{name}-%{githash}.tar.gz

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
%setup -q -n %{name}-%{githash}

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -G "Unix Makefiles"
make %{?_smp_mflags} all

%install
%make_install

%files
%{_sysconfdir}/%{name}
%attr(755, root, root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%doc README.md
%doc AUTHORS
%license LICENSE

%changelog
* Sun Feb 21 2016 Kamil Páral <kparal@redhat.com> - 2.5.0-1.20160210git7f0886e
- initial release. Use git to track future changes to the spec file.
