#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
Summary:	Digest Perl module
Summary(pl):	Modu³ perla Digest
Name:		perl-Digest
Version:	1.05
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	e5cc52c6268182719423573ff68f08b0
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is just a simple frontend module for autoloading of various
Digest:: modules.  It also provide documentation of the interface
that all Digest:: modules should provide.

%description -l pl
Ten modu³ jest prostym frontendem do automatycznego wczytywania
ró¿nych modu³ów Digest::. Zawiera tak¿e dokumentacjê do interfejsu
ogólnego dla wszystkich modu³ów Digest::.

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
