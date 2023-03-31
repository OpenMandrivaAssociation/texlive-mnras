Name:		texlive-mnras
Version:	55729
Release:	2
Summary:	Monthly Notices of the Royal Astronomical Society
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mnras
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnras.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnras.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Package for preparing papers in the journal "Monthly Notices of
the Royal Astronomical Society".

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mnras
%{_texmfdistdir}/bibtex/bst/mnras
%doc %{_texmfdistdir}/doc/latex/mnras

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
