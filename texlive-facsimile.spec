%global tl_name facsimile
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Document class for preparing faxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/facsimile
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The facsimile class provides a simple interface for creating a document
for sending as a fax, with LaTeX. The class covers two areas: First, a
title page is created with a detailed fax header; second, every page
gets headers and footers so that the recipient can be sure that every
page has been received and all pages are complete, and in the correct
order. The class evolved from the fax package, and provides much better
language support.

