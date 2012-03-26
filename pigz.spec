Name:           pigz
Version:        2.2.4
Release:        1
Summary:        Parallel implementation of gzip
Group:          Archiving/Compression
License:        zlib
URL:            http://www.zlib.net/pigz/
Source0:        http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  zlib-devel

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when compressing data.

%prep
%setup -q

%build
%make CFLAGS="%{optflags} -O3" LDFLAGS="%{ldflags}"

%install
install -p -m755 pigz -D %{buildroot}%{_bindir}/pigz
install -p -m755 unpigz -D %{buildroot}%{_bindir}/unpigz
install -p -m644 pigz.1 -D %{buildroot}%{_datadir}/man/man1/pigz.1

%files
%doc pigz.pdf README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_datadir}/man/man1/pigz.*
