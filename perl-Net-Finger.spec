%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Finger
Summary:	Net::Finger perl module
Summary(pl):	Modu³ perla Net::Finger
Name:		perl-Net-Finger
Version:	1.06
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Finger - a Perl implementation of a finger client.

%description -l pl
Net::Finger - implementacja klienta finger.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Net/Finger.pm
%{_mandir}/man3/*
