%global optflags %{optflags} -O3

# (tpg) enable PGO build
%bcond_without pgo

Summary:	Parallel implementation of gzip
Name:		pigz
Version:	2.6
Release:	4
Group:		Archiving/Compression
License:	zlib
Url:		http://www.zlib.net/pigz/
Source0:	http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pigz-2.4-Makefile.patch
BuildRequires:	pkgconfig(zlib)
# (tpg) by default use pigz as system-wide gzip
Conflicts:	gzip < 1.9-3

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when compressing data.

%prep
%autosetup -p1

%build
%set_build_flags

%if %{with pgo}
export LD_LIBRARY_PATH="$(pwd)"

CFLAGS="%{optflags} -fprofile-generate -mllvm -vp-counters-per-site=8" \
CXXFLAGS="%{optflags} -fprofile-generate" \
LDFLAGS="%{build_ldflags} -fprofile-generate" \
%make_build

make test ||:

unset LD_LIBRARY_PATH
llvm-profdata merge --output=%{name}-llvm.profdata $(find . -name "*.profraw" -type f)
PROFDATA="$(realpath %{name}-llvm.profdata)"
rm -f *.profraw
make clean

CFLAGS="%{optflags} -fprofile-use=$PROFDATA" \
CXXFLAGS="%{optflags} -fprofile-use=$PROFDATA" \
LDFLAGS="%{build_ldflags} -fprofile-use=$PROFDATA" \
%endif
%make_build

%install
install -p -m755 pigz -D %{buildroot}/bin/pigz
install -p -m755 unpigz -D %{buildroot}/bin/unpigz
install -p -m644 pigz.1 -D %{buildroot}%{_datadir}/man/man1/pigz.1

# (tpg) install replacement files to use pigz instead of gzip
ln -sf /bin/pigz %{buildroot}/bin/gzip
ln -sf /bin/unpigz %{buildroot}/bin/gunzip
mkdir -p %{buildroot}%{_bindir}
ln -sf /bin/unpigz %{buildroot}%{_bindir}/gunzip

%files
%doc README
/bin/pigz
/bin/unpigz
/bin/gzip
/bin/gunzip
%{_bindir}/gunzip
%doc %{_mandir}/man1/pigz.*
