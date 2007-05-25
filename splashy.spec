# TODO:
# - init script
# - test everything
Summary:	Next generation boot splashing system
Summary(pl.UTF-8):	System ekranu startowego nowej generacji
Name:		splashy
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://alioth.debian.org/frs/download.php/1832/%{name}_%{version}.tar.gz
# Source0-md5:	9581a5ff78b57c54269d3cda0cdd8b39
Patch0:		%{name}-libs.patch
URL:		http://splashy.alioth.debian.org/
BuildRequires:	DirectFB-static
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-static
BuildRequires:	glib2-static
BuildRequires:	libpng-static
BuildRequires:	pkgconfig
BuildRequires:	sysfsutils-static
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
Summary(pl.UTF-8):	Statyczna biblioteki Splashy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Splashy libraries.

%description static -l pl.UTF-8
Statyczna biblioteki Splashy.

%prep
%setup -q
%patch0 -p1
sed -i -e 's#-Werror##g' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/initramfs-tools
%{_datadir}/splashy
%{_mandir}/man?/*
%dir %{_sysconfdir}/splashy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/splashy/*.xml
%{_sysconfdir}/splashy/themes
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/splashy

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
