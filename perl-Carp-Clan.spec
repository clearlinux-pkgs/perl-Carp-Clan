#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Carp-Clan
Version  : 6.06
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Carp-Clan-6.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Carp-Clan-6.06.tar.gz
Summary  : 'Report errors from perspective of caller of a "clan" of modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Carp-Clan-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Exception)

%description
============================
Package "Carp::Clan"
============================
All rights reserved.

%package dev
Summary: dev components for the perl-Carp-Clan package.
Group: Development
Provides: perl-Carp-Clan-devel = %{version}-%{release}

%description dev
dev components for the perl-Carp-Clan package.


%package license
Summary: license components for the perl-Carp-Clan package.
Group: Default

%description license
license components for the perl-Carp-Clan package.


%prep
%setup -q -n Carp-Clan-6.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Carp-Clan
cp license/Artistic.txt %{buildroot}/usr/share/package-licenses/perl-Carp-Clan/license_Artistic.txt
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Carp/Clan.pm
/usr/lib/perl5/vendor_perl/5.28.0/Carp/Clan.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Carp::Clan.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Carp-Clan/license_Artistic.txt
