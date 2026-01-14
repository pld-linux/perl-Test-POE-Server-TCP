#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Test
%define	pnam	POE-Server-TCP
Summary:	Test::POE::Server::TCP - A POE Component providing TCP server services for test cases
Name:		perl-Test-POE-Server-TCP
Version:	1.16
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ac6b0c3d4609583e56b7ec21e428eb64
URL:		http://search.cpan.org/dist/Test-POE-Server-TCP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::POE::Server::TCP is a POE component that provides a TCP server
framework for inclusion in client component test cases, instead of
having to roll your own.

Once registered with the component, a session will receive events
related to client connects, disconnects, input and flushed output.
Each of these events will refer to a unique client ID which may be
used in communication with the component when sending data to the
client or disconnecting a client connection.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/POE/Server/*.pm
%dir %{perl_vendorlib}/Test/POE/Server
# or that one to perl-dirs or perl-POE?
%dir %{perl_vendorlib}/Test/POE
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
