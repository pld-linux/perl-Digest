#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
Summary:	Digest - Perl modules that calculate message digests
Summary(pl):	Digest - modu³y do obliczania skrótów komunikatów
Name:		perl-Digest
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	3346c9f3cad3519bd39a044d1900d4ab
BuildRequires:	perl-devel >= 1:5.6.0
BuildRequires:	rpm-perlprov >= 4.0.2-112.1
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
	INSTALLDIRS=site
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
%{perl_sitelib}/Digest.pm
%{perl_sitelib}/Digest/*
%{_mandir}/man3/*
