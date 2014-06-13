# revision 21328
# category Package
# catalog-ctan /macros/latex/contrib/facsimile
# catalog-date 2007-01-03 21:31:08 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-facsimile
Version:	1.0
Release:	7
Summary:	Document class for preparing faxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/facsimile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facsimile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The facsimile class provides a simple interface for creating a
document for sending as a fax, with LaTeX. The class covers two
areas: - First, a title page is created with a detailed fax
header; - second, every page gets headers and footers so that
the recipient can be sure that every page has been received and
all pages are complete, and in the correct order. The class
evolved from the fax package, and provides much better language
support.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751751
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718408
- texlive-facsimile
- texlive-facsimile
- texlive-facsimile
- texlive-facsimile

