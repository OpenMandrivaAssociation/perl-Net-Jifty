%define upstream_name    Net-Jifty
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to online Jifty applications
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(Cwd)
BuildRequires: perl(DateTime)
BuildRequires: perl(Email::Address)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(YAML)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
the Jifty manpage is a full-stack web framework. It provides an optional
REST interface for applications. Using this module, you can interact with
that REST interface to write client-side utilities.

You can use this module directly, but you'll be better off subclassing it,
such as what we've done for the Net::Hiveminder manpage.

This module also provides a number of convenient methods for writing short
scripts. For example, passing 'use_config => 1' to 'new' will look at the
config file for the username and password (or SID) of the user. If neither
is available, it will prompt the user for them.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/Net/


