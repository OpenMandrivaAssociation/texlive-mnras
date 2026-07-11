%global tl_name mnras
%global tl_revision 68878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	Monthly Notices of the Royal Astronomical Society
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mnras
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnras.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnras.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Package for preparing papers in the journal "Monthly Notices of the
Royal Astronomical Society".

