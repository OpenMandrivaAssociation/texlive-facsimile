Name:		texlive-facsimile
Version:	1.0
Release:	1
Summary:	Document class for preparing faxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/facsimile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The facsimile class provides a simple interface for creating a
document for sending as a fax, with LaTeX. The class covers two
areas: - First, a title page is created with a detailed fax
header; - second, every page gets headers and footers so that
the recipient can be sure that every page has been received and
all pages are complete, and in the correct order. The class
evolved from the fax package, and provides much better language
support.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/facsimile/fac-de.cfg
%{_texmfdistdir}/tex/latex/facsimile/fac-en.cfg
%{_texmfdistdir}/tex/latex/facsimile/facsimile.cls
%doc %{_texmfdistdir}/doc/latex/facsimile/README
%doc %{_texmfdistdir}/doc/latex/facsimile/example.tex
%doc %{_texmfdistdir}/doc/latex/facsimile/facsimile.pdf
#- source
%doc %{_texmfdistdir}/source/latex/facsimile/facsimile.dtx
%doc %{_texmfdistdir}/source/latex/facsimile/facsimile.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
