#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
Summary:	Digest - Perl modules that calculate message digests
Summary(pl.UTF-8):	Digest - moduły do obliczania skrótów komunikatów
Name:		perl-Digest
Version:	1.15
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	83be88df645ef0981d991f86dcba6da7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is just a simple frontend module for autoloading of various
Digest:: modules.  It also provide documentation of the interface
that all Digest:: modules should provide.

%description -l pl.UTF-8
Ten moduł jest prostym frontendem do automatycznego wczytywania
różnych modułów Digest::. Zawiera także dokumentację do interfejsu
ogólnego dla wszystkich modułów Digest::.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Digest.pm
%{perl_vendorlib}/Digest/*
%{_mandir}/man3/*
