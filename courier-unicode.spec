#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Courier Unicode library
Summary(pl.UTF-8):	Biblioteka Courier Unicode
Name:		courier-unicode
Version:	2.3.2
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	https://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	9350a353e762af4d0231b24ce23e9661
URL:		http://www.courier-mta.org/unicode/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Courier Unicode library implements several algorithms related to
the Unicode Standard:
- Look up uppercase, lowercase, and titlecase equivalents of a unicode
  character.
- Implementation of grapheme and word breaking rules.
- Implementation of line breaking rules.
- Several ancillary functions, like looking up the unicode character
  that corresponds to some HTML 4.0 entity (such as "&amp;", for
  example), and determining the normal width or a double-width status of
  a unicode character. Also, an adaptation of the iconv(3) API for this
  unicode library.
- Look up the Unicode script property.
- Look up the category property.

This library also implements C++ bindings for these algorithms.

%description -l pl.UTF-8
Biblioteka Courier Unicode implementuje kilka algorytmów związanych ze
standardem Unicode:
- wyszukiwanie małych, wielkich i tytułowych odpowiedników znaków
  unikodowych,
- implementację reguł łamania słów i grafemów,
- implementację reguł łamania wierszy tekstu,
- kilka funkcji pomocniczych, jak wyszukiwanie znaków unikodowych
  odpowiadających encjom HTML 4.0 (np. "&amp;") oraz określanie
  szerokości (normalna lub podwójna) znaku unikodowego; dostępna jest
  także adaptacja API iconv(3) dla tej biblioteki
- wyszukiwanie własności pisma,
- wyszukiwanie własności kategorii.

Biblioteka zawiera także wiązania C++ do tych algorytmów.

%package devel
Summary:	Development files for the Courier Unicode library
Summary(pl.UTF-8):	Pliki programistyczne dla biblioteki Courier Unicode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Development files for the Courier Unicode library.

%description devel -l pl.UTF-8
Pliki programistyczne dla biblioteki Courier Unicode.

%package static
Summary:	Static Courier Unicode library
Summary(pl.UTF-8):	Statyczna biblioteka Courier Unicode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Courier Unicode library.

%description static -l pl.UTF-8
Statyczna biblioteka Courier Unicode.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies (except libstdc++)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcourier-unicode.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcourier-unicode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcourier-unicode.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcourier-unicode.so
%{_includedir}/courier-unicode*.h
%{_aclocaldir}/courier-unicode*.m4
%{_mandir}/man3/unicode::*.3*
%{_mandir}/man3/unicode_*.3*
%{_mandir}/man7/courier-unicode.7*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcourier-unicode.a
%endif
