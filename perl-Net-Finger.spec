%include	/usr/lib/rpm/macros.perl
Summary:	Net-Finger perl module
Summary(pl):	Modu� perla Net-Finger
Name:		perl-Net-Finger
Version:	1.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Finger-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Finger - a Perl implementation of a finger client.

%description -l pl
Net-Finger - implementacja klienta finger.

%prep
%setup -q -n Net-Finger-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Finger.pm
%{_mandir}/man3/*
