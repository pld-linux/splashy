# TODO:
# - init script
# - test everything
Summary:	Next generation boot splashing system
Summary(pl.UTF-8):	System ekranu startowego nowej generacji
Name:		splashy
Version:	0.3.13
Release:	13
License:	GPL v2
Group:		Applications/System
Source0:	http://alioth.debian.org/frs/download.php/2691/%{name}_%{version}.tar.gz
# Source0-md5:	03b7ee4f31c56ee61463772f74bad8a0
Patch0:		format-security.patch
URL:		http://splashy.alioth.debian.org/
BuildRequires:	DirectFB-devel >= 0.9.22
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libmagic-devel
BuildRequires:	libtool
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	splashy-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Splashy is a next generation boot splashing system for Linux systems.
Unlike other splashing systems, it needs no patches to the kernel and
it's installed like a normal package. Make your boot process eye-candy
with Splashy!

Some of Splash's most noticable features include:
- Require zero kernel patches/full functionality in user-space
- Boot/halt/reboot/runlevel-switch support
- Progressbar support (with optional border)
- Verbose mode (with F2/ESC keys)
- Configuration file in XML
- Cope with any video-mode resolution/size
- Cope with 8, 16, and 24 bit framebuffers
- Alpha channel (transparency) support
- Video mode detection
- Initramfs support
- TrueType2 fonts support
- Lots of image/animation file formats supported: jpg, png, gif, mpg,
  swf
- Low dependencies and code in C to best perform
- Full LSB support
- Multiple themes support
- Really easy to create new themes
- X detection on exit
- Smooth progressbar movement
- Animations support
- Fade in/out effects
- Totally configurable

%description -l pl.UTF-8
Splashy to system ekranu startowego nowej generacji dla Linuksa. W
przeciwieństwie do innych takich systemów nie wymaga łatania jądra i
jest instalowany jako zwykły pakiet. Pozwala upiększyć proces
uruchamiania systemu.

Najbardziej widoczne możliwości pakietu Splashy to:
- brak potrzeby łatania jądra, pełna funkcjonalność w przestrzeni
  użytkownika
- obsługa uruchamiania/wyłączania/restartowania komputera oraz wyboru
  poziomu (runlevelu)
- obsługa paska postępu (z opcjonalną ramką)
- tryb szczegółowy (z obsługą klawiszy F2/ESC)
- plik konfiguracyjny w formacie XML
- działanie z dowolną rozdzielczością/rozmiarem trybu graficznego
- działanie z framebufferami 8-, 16- i 24-bitowymi
- obsługa kanału alpha (przezroczystości)
- obsługa initramfs
- obsługa fontów TrueType
- obsługa wielu formatów obrazów/animacji: jpg, png, gif, mpg, swf
- małe zależności i kod w C dla najlepszej wydajności
- pełna obsługa LSB
- obsługa wielu motywów
- naprawdę łatwe tworzenie nowych motywów
- wykrywanie X przy kończeniu pracy
- płynne przesuwanie paska postępu
- obsługa animacji
- efekty fade in/fade out
- pełna konfigurowalność

%package libs
Summary:	Splashy libraries
Summary(pl.UTF-8):	Biblioteki Splashy
Group:		Libraries

%description libs
Splashy libraries.

%description libs -l pl.UTF-8
Biblioteki Splashy.

%package devel
Summary:	Header files for Splashy libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Splashy
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Splashy libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Splashy.

%package static
Summary:	Static Splashy libraries
Summary(pl.UTF-8):	Statyczne biblioteki Splashy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Splashy libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Splashy.

%package theme-default
Summary:	Default theme for splashy
Summary(pl.UTF-8):	Domyślny motyw dla systemu splashy
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	splashy-theme

%description theme-default
Default theme for splashy.

%description theme-default -l pl.UTF-8
Domyślny motyw dla systemu splashy.

%package initramfs
Summary:	Splashy support scripts for initramfs-tools
Summary(pl.UTF-8):	Skrypty dla initramfs-tools ze wsparciem dla systemu splashy
Group:		Base
Requires:	%{name} = %{version}-%{release}
Requires:	initramfs-tools

%description initramfs
Splashy support scripts for initramfs-tools.

%description initramfs -l pl.UTF-8
Skrypty dla initramfs-tools ze wsparciem dla systemu splashy.

%prep
%setup -q
%patch0 -p1
sed -i -e 's#-Werror##g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--enable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/splashy
%dir %{_datadir}/splashy/themes
%{_mandir}/man?/*
%dir %{_sysconfdir}/splashy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/splashy/*.xml
%dir %{_sysconfdir}/splashy/themes

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsplashy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsplashy.so.1
%attr(755,root,root) %{_libdir}/libsplashycnf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsplashycnf.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsplashy.so
%attr(755,root,root) %{_libdir}/libsplashycnf.so
%{_libdir}/libsplashy.la
%{_libdir}/libsplashycnf.la
%{_includedir}/splashy*.h
%{_pkgconfigdir}/splashy.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a

%files theme-default
%defattr(644,root,root,755)
%{_datadir}/splashy/themes/default

%if 0
%files initramfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/initramfs-tools/hooks/*
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/init-bottom/*
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/local-premount/*
%{_datadir}/initramfs-tools/modules.d/*
%endif
