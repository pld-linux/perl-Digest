%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
Summary:	Digest Perl module
Summary(pl):	Modu� perla Digest
Name:		perl-Digest
Version:	1.02
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is just a simple frontend module for autoloading of various
Digest:: modules.  It also provide documentation of the interface
that all Digest:: modules should provide.

%description -l pl
Ten modu� jest prostym frontendem do automatycznego wczytywania
r�nych modu��w Digest::. Zawiera tak�e dokumentacj� do interfejsu
og�lnego dla wszystkich modu��w Digest::.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

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
%{_mandir}/man3/*
