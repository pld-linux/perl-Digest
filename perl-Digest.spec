%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
Summary:	Digest Perl module
Summary(pl):	Modu³ perla Digest
Name:		perl-Digest
Version:	1.02
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
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
%{perl_sitelib}/Digest.pm
%{_mandir}/man3/*
