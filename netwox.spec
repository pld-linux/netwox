Summary:	A toolbox for network administrators and network hackers
Summary(pl):	Zestaw narz�dzi dla administrator�w sieci i hacker�w sieciowych
Name:		netwox
Version:	5.12.0
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Networking
Source0:	http://www.laurentconstantin.com/common/netw/netwox/download/v5/%{name}-%{version}-src.tgz
# Source0-md5:	e119443cc5f2ed8fb9a2eb06abb1eeba
Patch0:		%{name}-config.patch
URL:		http://www.laurentconstantin.com/en/netw/netwox/
BuildRequires:	netwib-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netwox is a toolbox for network administrators and network hackers.
Netwox contains over 100 tools using network library netwib.

%description -l pl
Netwox to zestaw narz�dzi dla administrator�w sieci i hacker�w
sieciowych. Zawiera ponad 100 narz�dzi u�ywaj�cych biblioteki
sieciowej netwib.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
cd src
./genemake \
	NETWIBDEF_INSTPREFIX="/usr"
sed -i -e 's#444#644#' -e 's#555#755#g' Makefile
%{__make} \
        CC="%{__cc}" \
        GCCOPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -C src install \
        INSTBIN=$RPM_BUILD_ROOT%{_bindir} \
        INSTMAN1=$RPM_BUILD_ROOT%{_mandir}/man1 \
        INSTUSERGROUP="$(id -u):$(id -g)"

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/netwox.1
echo ".so netwox53.1" > $RPM_BUILD_ROOT%{_mandir}/man1/netwox.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
